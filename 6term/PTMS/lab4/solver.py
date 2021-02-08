import numpy

__author__ = 'nik-u'
import math
import scipy.stats
import scipy.special
import random


class Solver:
    def get_uniform_values(self, a, b, n):
        return [random.uniform(a, b) for x in range(n)]

    def get_function(self):
        def func(x):
            return math.pow(x, 3)

        return func

    def get_density_func(self, a, b):
        y_func = self.get_function()

        def func(x):
            if x < y_func(a) or x >= y_func(b):
                return 0
            else:
                return 1 / (3 * (b - a) * math.pow(math.fabs(x), 2 / 3.0))

        return func

    def get_distrib_func(self, a, b):
        y_func = self.get_function()

        def func(x):
            if x < y_func(a):
                return 0
            elif x >= y_func(b):
                return 1
            else:
                return 1.0 / (b - a) * (
                    math.copysign(1, x) * math.pow(math.fabs(x), 1 / 3.0) - a)

        return func

    def get_emperic_ungroup_func(self, values):
        probs = {}
        for i in range(len(values)):
            if not values[i] in probs:
                probs[values[i]] = i / 1. / len(values)
        sorted_keys = sorted(probs.keys())

        def func(x):
            if x > sorted_keys[-1]:
                return 1
            else:
                i = 0;
                while i < len(sorted_keys) and x > sorted_keys[i]:
                    i += 1;
                return probs[sorted_keys[i]]

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

    def func_average_value(self, a, b):
        interval_func = self.get_distrib_func(a, b)

        def func(leftborder, rightborder):
            return (interval_func(rightborder) - interval_func(leftborder)) / (rightborder - leftborder)

        return func

    def get_uniform_distribution_func(self, expValue, dispersion):
        b = math.sqrt(dispersion) + expValue
        a = 2 * expValue - b

        def func(x):
            if x < a:
                return 0
            elif x >= b:
                return 1
            else:
                return 1.0 * (x - a) / (b - a)

        return func

    def get_exponential_distribution_func(self, expValue):
        l = 1. / expValue

        def func(x):
            if x >= 0:
                return 1 - math.exp(-l * x)
            else:
                return 0

        return func

    def get_normal_distribution_func(self, mu, dispersion):
        sigma = math.sqrt(dispersion)

        def func(x):
            return scipy.stats.norm.cdf(x, loc=mu, scale=sigma)

        return func

    def getbarchart(self, n, values):
        if n <= 100:
            intcount = int(math.sqrt(n))
        else:
            intcount = int(4 * math.log10(n))
        while n % intcount != 0:
            intcount -= 1
        v = n / intcount
        barchart = []
        h = (values[v - 1] + values[v]) / 2 - values[0]
        barchart.append((values[0], (values[v - 1] + values[v]) / 2, v / (n * h)))
        for i in range(2, intcount + 1):
            a = (values[(i - 1) * v - 1] + values[(i - 1) * v]) / 2
            if i * v >= n:
                b = values[i * v - 1]
            else:
                b = (values[i * v - 1] + values[i * v]) / 2
            barchart.append((a, b, 1. / intcount))
        return barchart

    def pearson_criteria(self, intervals, n, alpha, distribution_function, param_count):
        chi = 0
        emperic_prob = 1. / len(intervals)
        for a, b, prob in intervals:
            theor = distribution_function(b) - distribution_function(a)
            if theor == 0:
                return ("rejected", 0, 0)
            chi += (emperic_prob - theor) ** 2 / theor
        chi *= n
        freedom_degrees = len(intervals) - 1 - param_count
        q = scipy.stats.chi2.ppf(1 - alpha, freedom_degrees)
        if chi < q:
            return ("accepted", chi, q)
        else:
            return ("rejected", chi, q)

    def kolmogorov_criteria(self, values, alpha, distribution_function):
        max_diff = -1
        empiric_func = self.get_emperic_ungroup_func(values)
        for x in values:
            max_diff = max(max_diff, abs(distribution_function(x) - empiric_func(x)))
        max_diff *= math.sqrt(len(values))
        critical = scipy.special.kolmogi(alpha)
        if max_diff > critical:
            return ("rejected", max_diff, critical)
        else:
            return ("accepted", max_diff, critical)

    def mises_criteria(self, values, alpha, distribution_function):
        n = len(values)
        omega = 1. / 12 / n
        for i in range(1, n + 1):
            omega += (distribution_function(values[i - 1]) - (i - 0.5) / n) ** 2
        d = {0.9: 0.3473, 0.95: 0.4614, 0.99: 0.7435, 0.995: 0.8694, 0.999: 1.1679}
        critical = d[1 - alpha]
        if omega <= critical:
            return ("accepted", omega, critical)
        else:
            return ("rejected", omega, critical)
