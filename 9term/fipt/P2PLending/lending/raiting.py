import os
import pandas as pd

from django.conf import settings
from django.db import transaction
from sklearn.linear_model import LogisticRegression
from P2PLending.lending.models import MoneyRequestAd

_LENDING_PREDICT_MODEL = None
_FEATURES = ["home_ownership", "annual_inc", "loan_amnt", "term"]
_HOME_OWNERSHIP = None


def is_poor_coverage(row):
    pct_null = float(row.isnull().sum()) / row.count()
    return pct_null < 0.8


def fit_model():
    """
    Fit model that predicts return of credit
    """
    global _HOME_OWNERSHIP
    _HOME_OWNERSHIP = {x: i for i, x in enumerate(["rent", "own", "mortgage", "other"])}
    df = pd.read_csv(os.path.join(settings.BASE_DIR, "LoanStats3a.csv"), skiprows=1).head(5000)
    df = df[df.apply(is_poor_coverage, axis=1)]
    df['year_issued'] = df.issue_d.apply(lambda x: int(x.split("-")[0]))
    df_term = df[df.year_issued < 2012]

    bad_indicators = [
        "Late (16-30 days)",
        "Late (31-120 days)",
        "Default",
        "Charged Off"
    ]
    df_term['is_rent'] = df_term.home_ownership == "RENT"
    df_term = df_term[df_term.home_ownership.apply(lambda x: x is not None and x != 'NONE')]
    df_term['is_bad'] = df_term.loan_status.apply(lambda x: x in bad_indicators)
    df_term['term'] = df_term.term.apply(lambda x: x.split()[0])
    df_term['home_ownership'] = df_term.home_ownership.apply(lambda x: _HOME_OWNERSHIP[x.lower()])
    global _LENDING_PREDICT_MODEL
    _LENDING_PREDICT_MODEL = LogisticRegression()
    _LENDING_PREDICT_MODEL.fit(df_term[_FEATURES], df_term.is_bad)


def get_user_return_probs(user, loan_amount, term):
    if user.income is not None and user.home_ownership is not None:
        ownership_mapping = {"own": "own", "rnt": "rent", "mrtg": "mortgage"}
        data = {
            "home_ownership": _HOME_OWNERSHIP[ownership_mapping[user.home_ownership]],
            "annual_inc": user.income,
            "loan_amnt": loan_amount,
            "term": term
        }
        data['is_rent'] = data['home_ownership'] == "RENT"
        data = {k: [v] for k, v in data.items()}
        data = pd.DataFrame(data)
        data = data[_FEATURES]
        probs = _LENDING_PREDICT_MODEL.predict_proba(data)
        prob = probs[0][1]
        return 1 - prob
    return None


def get_request_return_prob(user, request):
    amount = request.amount.amount / 2  # some cheating here
    term = request.term.days
    return get_user_return_probs(user, amount, term)


def update_user_requests_return_prob(user):
    with transaction.atomic():
        for request in MoneyRequestAd.objects.filter(user=user):
            request.return_probability = get_request_return_prob(user, request)
            request.save()
