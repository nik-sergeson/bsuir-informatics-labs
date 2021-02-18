import math
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

    def func_average_value(self, a, b):
        interval_func = self.get_distrib_func(a, b)
        def func(leftborder, rightborder):
            return (interval_func(rightborder)-interval_func(leftborder))/(rightborder-leftborder)
        return func

    def getbarchart(self, n, values):
        if n <= 100:
            intcount = int(math.sqrt(n))
        else:
            intcount = int(4 * math.log10(n))
        h = (values[-1] - values[0]) / intcount
        barchart = []
        for i in range(intcount):
            a = values[0] + i * h
            b = a + h
            v = 0
            for x in values:
                if x > b:
                    break
                elif x > a and x < b:
                    v += 1
                elif x == a:
                    v += 0.5
                elif x == b:
                    v += 0.5
            barchart.append((a, b, v / (n * h)))
        return barchart