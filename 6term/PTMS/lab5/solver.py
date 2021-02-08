__author__ = 'nik-u'
import math
import random
import scipy.stats


class Solver:
    def __init__(self):
        self.theor_dispersion = 1. / 7
        self.ther_expvalue = 0

    def get_uniform_values(self, a, b, n):
        return [random.uniform(a, b) for x in range(n)]

    def get_function(self):
        def func(x):
            return math.pow(x, 3)

        return func

    def estimate_expvalue(self, values):
        return sum(values) / 1. / len(values)

    def estimate_dispersion(self, values):
        expvalue = self.estimate_expvalue(values)
        dispersion = 0
        for x in values:
            dispersion += (x - expvalue) ** 2
        dispersion /= 1. * (len(values) - 1)
        return dispersion

    def expvalue_confidence_interval(self, values, alpha):
        expvalue = self.estimate_expvalue(values)
        dispersion = self.estimate_dispersion(values)
        studvalue = scipy.stats.t.ppf(1 - (1 - alpha) / 2.0, len(values))
        return (expvalue - studvalue * math.sqrt(dispersion) / math.sqrt(len(values)),
                expvalue + studvalue * math.sqrt(dispersion) / math.sqrt(len(values)))

    def expvalue_confidence_interval_known_dispersion(self, values, dispersion, alpha):
        laplasvalue = scipy.stats.norm.ppf(1 - (1 - alpha) / 2.0)
        expvalue = self.estimate_expvalue(values)
        return (expvalue - laplasvalue * math.sqrt(dispersion) / math.sqrt(len(values)),
                expvalue + laplasvalue * math.sqrt(dispersion) / math.sqrt(len(values)))

    def dispersion_confidence_interval(self, values, alpha):
        leftchi = scipy.stats.chi2.ppf(1 - (1 - alpha) / 2., len(values) - 1)
        rightchi = scipy.stats.chi2.ppf(1 - (1 + alpha) / 2., len(values) - 1)
        dispersion = self.estimate_dispersion(values)
        return (len(values) * dispersion / leftchi, len(values) * dispersion / rightchi)

    def dispersion_confidence_interval_known_expvalue(self, values, alpha, expvalue):
        selective_dispersion = 0
        for x in values:
            selective_dispersion += (x - expvalue) ** 2
        selective_dispersion /= 1. * len(values)
        leftchi = scipy.stats.chi2.ppf(1 - (1 - alpha) / 2., len(values) - 1)
        rightchi = scipy.stats.chi2.ppf(1 - (1 + alpha) / 2., len(values) - 1)
        return (len(values) * selective_dispersion / leftchi, len(values) * selective_dispersion / rightchi)
