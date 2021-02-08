from __future__ import division
import math
import scipy.stats


def discrete_random_variable_simulator(discr_distrib, values_quantity):
    """
    :rtype variable_values:dict
    """
    values=discr_distrib.rvs(size=values_quantity).tolist()
    random_variable={}
    for x in values:
        if x not in random_variable:
            random_variable[x]=values.count(x)/len(values)
    values = sorted(random_variable.keys())
    probabilities = [random_variable[x] for x in values]
    lower = 0
    upper = probabilities[0]
    segments = []
    for i in range(1, len(probabilities)):
        segments.append((lower, upper))
        lower = upper
        upper += probabilities[i]
    segments.append((lower, 1))
    while True:
        x = scipy.stats.uniform.rvs(loc=0, scale=1, size=1)[0]
        for i, (lower, upper) in enumerate(segments):
            if lower < x <= upper:
                yield values[i]
                break


def estimate_expvalue(values):
    return sum(values) / 1. / len(values)


def estimate_dispersion(values):
    expvalue = estimate_expvalue(values)
    dispersion = 0
    for x in values:
        dispersion += (x - expvalue) ** 2
    dispersion /= 1. * (len(values) - 1)
    return dispersion


def expvalue_confidence_interval(values, alpha):
    expvalue = estimate_expvalue(values)
    dispersion = estimate_dispersion(values)
    studvalue = scipy.stats.t.ppf(1 - (1 - alpha) / 2.0, len(values))
    return (expvalue - studvalue * math.sqrt(dispersion) / math.sqrt(len(values)),
            expvalue + studvalue * math.sqrt(dispersion) / math.sqrt(len(values)))


def dispersion_confidence_interval(values, alpha):
    leftchi = scipy.stats.chi2.ppf(1 - (1 - alpha) / 2., len(values) - 1)
    rightchi = scipy.stats.chi2.ppf(1 - (1 + alpha) / 2., len(values) - 1)
    dispersion = estimate_dispersion(values)
    return (len(values) * dispersion / leftchi, len(values) * dispersion / rightchi)


def get_bar_chart(k, a, b):
    """
    :type values:list
    :type a,b:float
    :type k:int
    """

    def func(values):
        h = (b - a) / k
        b_i = a
        values.sort()
        left = []
        heights = []
        value_quantity = len(values)
        for i in range(k):
            a_i = b_i
            b_i = a_i + h
            v = 0
            for x in values:
                if x > b_i:
                    break
                elif a_i < x <= b_i:
                    v += 1
            left.append(a_i)
            heights.append(v / value_quantity)
        return left, heights, h

    return func


def pearson_criteria(intervals, width, n, alpha, distribution_function, param_count):
    chi = 0
    for a, prob in intervals:
        b=a+width
        theor = distribution_function(b) - distribution_function(a)
        if theor == 0:
            return "rejected", 0, 0
        chi += (prob - theor) ** 2 / theor
    chi *= n
    freedom_degrees = len(intervals) - 1 - param_count
    q = scipy.stats.chi2.ppf(1 - alpha, freedom_degrees)
    if chi < q:
        return "accepted", chi, q
    else:
        return "rejected", chi, q
