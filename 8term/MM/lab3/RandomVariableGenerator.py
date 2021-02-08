from  __future__ import division
import numpy
import scipy.stats
import math


def get_exponential_distr(uniform_random_generator, lambda_param):
    while True:
        x = uniform_random_generator.next()
        yield -numpy.log(1 - x) / lambda_param


def get_uniform_distr(uniform_random_generator, a, b):
    while True:
        x = uniform_random_generator.next()
        yield a + (b - a) * x


def get_gauss_distr(uniform_random_generator, loc, scale):
    while True:
        x = sum(scipy.stats.uniform.rvs(loc=0, scale=1, size=12))
        yield loc + scale * (x - 6)


def get_gamma_distr(uniform_random_generator, nu_param, lambda_param):
    while True:
        x = sum(numpy.log(scipy.stats.uniform.rvs(loc=0, scale=1, size=nu_param)))
        yield -x / lambda_param


def get_triang_distr(uniform_random_generator, a, b):
    while True:
        x1 = scipy.stats.uniform.rvs(loc=0, scale=1, size=1)[0]
        x2 = scipy.stats.uniform.rvs(loc=0, scale=1, size=1)[0]
        yield a + (b - a) * max(x1, x2)


def get_simpson_distr(a, b):
    while True:
        yield sum(scipy.stats.uniform.rvs(loc=a/2, scale=(b-a)/2, size=2))


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
