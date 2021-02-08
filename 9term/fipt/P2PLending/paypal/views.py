import datetime
import logging

from django.conf import settings
from django.http import HttpResponseForbidden, HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import redirect, reverse, get_object_or_404
from django.views import View
from moneyed import Money
import paypalrestsdk

from P2PLending.users.models import User

FRACTIONAL_PART_LENGTH = 2

class WithdrawMoneyView(View):
    def get(self, request, user_id):
        profile_page = reverse("profile")
        user = get_object_or_404(User, pk=user_id)
        if user != request.user:
            return HttpResponseForbidden("Вы можете снимать средства только со своего собственного счета.")
        now = datetime.datetime.now()
        email = request.GET.get('email')
        amount = request.GET.get('amount')
        try:
            amount = validate(amount, user.usermoney.balance.amount)
        except ValueError as exc:
            return HttpResponseBadRequest('{} <a href="{}">Вернуться на страницу пользователя</a>'.format(exc.args[0], profile_page))
        payout = paypalrestsdk.Payout({
            "sender_batch_header": {
                "sender_batch_id": str(user_id) + '%' + str(now),
                "email_subject": "Creditosha"
            },
            "items": [
                {
                    "recipient_type": "EMAIL",
                    "amount": {
                        "value": amount,
                        "currency": "RUB"
                    },
                    "receiver": email,
                    "note": "You are withdrawing funds from creditosha.",
                    "sender_item_id": "item_1"
                }
            ]
        })
        if payout.create(sync_mode=True):
            if payout.items[0].transaction_status == 'SUCCESS':
                currency_amount = Money(amount=amount, currency=settings.DEFAULT_CURRENCY)
                user.usermoney.withdraw_money(currency_amount)
                return redirect(profile_page)
            if payout.items[0].errors.name == 'RECEIVER_UNCONFIRMED' or \
               payout.items[0].errors.name == 'RECEIVER_UNREGISTERED':
                return HttpResponseBadRequest('Пользователя Paypal с таким аккаунтом не существует. ' +
                                              '<a href="{}">Вернуться на страницу пользователя</a>'
                                              .format(profile_page))
        logging.error("Error executing payout.", payout)
        return redirect(profile_page)


class PutMoneyView(View):
    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        profile_page = reverse("profile")
        if user != request.user:
            return HttpResponseForbidden("Вы можете пополнять баланс только своего собственного счета.")
        amount = request.GET.get('amount')
        try:
            amount = validate(amount)
        except ValueError as exc:
            return HttpResponseBadRequest('{} <a href="{}">Вернуться на страницу пользователя</a>'.format(exc.args[0], profile_page))
        host = request.build_absolute_uri('/')[:-1]
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"},
            "redirect_urls": {
                "return_url": host + reverse("paypal:proceed", kwargs={"user_id": user_id}),
                "cancel_url": host + reverse("paypal:cancel", kwargs={"user_id": user_id}),
            },
            "transactions": [{
                "amount": {
                    "total": str(amount),
                    "currency": "RUB"},
                "description": 'Пополнить счет на сервисе "Кредитоша"'}]})
        if payment.create():
            for link in payment.links:
                if link.rel == 'approval_url':
                    redirect_url = str(link.href)
                    return redirect(redirect_url)
            logging.error("There is no approval url.", payment)
        else:
            logging.error("Payment error.", payment)
        return HttpResponseBadRequest('Случилась непредвиденная ошибка. Обратитесь, пожалуйста, в техподдержку.')


class CancelPutMoneyView(View):
    def get(self, request, user_id):
        return redirect(reverse("profile", kwargs={"user_id": user_id}))


class ProceedPutMoneyView(View):
    def get(self, request, user_id):
        profile_page = reverse("profile")
        payer_id = request.GET.get("PayerID")
        payment_id = request.GET.get("paymentId")
        if not (payer_id and payment_id):
            print(request, user_id, payer_id, payment_id)
            logging.error("Invalid request.", request)
            return HttpResponseServerError()
        payment = paypalrestsdk.Payment.find(payment_id)
        if payment.state == "approved":
            logging.info("Payment is already approved.", payment)
            return redirect(profile_page)
        if payment.execute({"payer_id": payer_id}):
            amount = float(payment.transactions[0].amount.total)
            amount = Money(amount=amount, currency=settings.DEFAULT_CURRENCY)
            user = get_object_or_404(User, pk=user_id)
            user.usermoney.put_money(amount)
            return redirect(profile_page)
        else:
            logging.error("Error executing payment", payment)
            return HttpResponseServerError()


def validate(amount, max_value=None):
    amount = float(amount)
    amount = round(amount, FRACTIONAL_PART_LENGTH)
    if amount <= 0:
        raise ValueError("Сумма должна быть положительна.")
    if max_value is not None and amount > max_value:
        raise ValueError("Недостаточно средств.")
    return amount
