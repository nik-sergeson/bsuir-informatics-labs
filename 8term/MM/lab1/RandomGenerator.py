from __future__ import division
import random


def square_middle_method(n, number=None):
    if number is None:
        number = random.randint(10 ** (n - 1), 10 ** n - 1)
    while True:
        num_sqr = str(number ** 2)
        num_sqr = (2 * n - len(num_sqr)) * "0" + num_sqr
        number_trunc = num_sqr[n // 2:-n // 2]
        if len(number_trunc) > n // 2:
            number_trunc = number_trunc[1:]
        yield float("." + number_trunc)
        number = int(number_trunc)


def gcd(a, b):
    if b > a:
        a, b = b, a
    while b:
        a %= b
        a, b = b, a
    return a


def get_k_by_m(m):
    k = m // 2
    while gcd(k, m) != 1 and k != m:
        k += 1
    return k


def multiplicative_congruental_method(A_0, m, k):
    A_i = A_0
    while True:
        A_i = (k * A_i) % m
        yield A_i / m


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
        left=[]
        heights=[]
        value_quantity = len(values)
        for i in range(k):
            a_i = b_i
            b_i = a_i + h
            v = 0
            for x in values:
                if x > b_i:
                    break
                elif a_i < x < b_i:
                    v += 1
                elif x == a_i:
                    v += 0.5
                elif x == b_i:
                    v += 0.5
            left.append(a_i)
            heights.append(v / value_quantity)
        return left,heights,h

    return func


def get_expected_value(values):
    return sum(values) / len(values)


def get_dispersion(values, expected_value):
    sum = 0
    for val in values:
        sum += val ** 2
    sum /= len(values)
    return sum - expected_value ** 2


def estimate_correlation(values, s):
    n = len(values)
    product_sum = 0
    for i in range(n - s):
        product_sum += values[i] * values[i + s]
    return 12 * product_sum / (n - s) - 3
