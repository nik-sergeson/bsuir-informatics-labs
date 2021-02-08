from __future__ import division


def estimate_expvalue(values):
    if isinstance(values, list):
        return sum(values) / 1. / len(values)
    elif isinstance(values, dict):
        sum_val = 0
        quantity = 0
        for val, quant in values.items():
            sum_val += val * quant
            quantity += quant
        return sum_val / quantity


def estimate_dispersion(values):
    expvalue = estimate_expvalue(values)
    dispersion = 0
    for x in values:
        dispersion += (x - expvalue) ** 2
    dispersion /= 1. * (len(values) - 1)
    return dispersion
