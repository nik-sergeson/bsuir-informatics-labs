import random
import math

__author__ = 'nik-u'


class Solver:
    def get_uniform_values(self, a, b, n):
        return [random.uniform(a, b) for x in range(n)]

    def get_function(self):
        def func(x):
            return math.pow(x, 3)

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

    def get_frequency_series(self, values):
        freqs = {}
        for item in values:
            if item in freqs:
                freqs[item] += 1
            else:
                freqs[item] = 1
        return freqs

    def get_probabilities(self, values):
        freqs = {}
        i = 0
        valuelistlen = len(values)
        for item in values:
            if item in freqs:
                freqs[item] += 1.0 / valuelistlen
            else:
                freqs[item] = ((1.0 * i) / valuelistlen)
            i += 1
        return freqs
