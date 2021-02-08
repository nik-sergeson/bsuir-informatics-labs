from __future__ import division


def get_x_distribution_series(x_values, probabilites):
    distr_series = {}
    for i, x in enumerate(x_values):
        prob_sum = 0
        for prob in probabilites[i]:
            prob_sum += prob
        distr_series[x] = prob_sum
    return distr_series


def get_x_distribution_function(distribution_series):
    """
    :type distribution_series:dict
    """
    distrib_func = {}
    prob = 0
    for x in sorted(distribution_series.keys()):
        distrib_func[x] = prob
        prob += distribution_series[x]
    return distrib_func


def get_conditional_distribution_series(probabilities, x_values, y_values, x_distr_series):
    series = {}
    for j, y in enumerate(y_values):
        series[y] = {}
        for i, x in enumerate(x_values):
            series[y][x] = probabilities[i][j] / x_distr_series[x]
    return series


def get_y_distribution_function(x_values, y_values, conditional_distribution_series):
    distrib_func = {}
    for x in x_values:
        distrib_func[x] = {}
        prob = 0
        for y in sorted(y_values):
            distrib_func[x][y] = prob
            prob += conditional_distribution_series[y][x]
    return distrib_func


def two_dim_value_generator(x_values, y_values, x_distribution_func, y_distrib_func, uniform_generator):
    """
    :type x_distribution_func:dict
    :type y_distrib_func:dict
    """
    while True:
        xi = uniform_generator.next()
        for i in range(len(x_values) - 1):
            if x_distribution_func[x_values[i]] < xi <= x_distribution_func[x_values[i + 1]]:
                x = x_values[i]
                break
        else:
            x = x_values[-1]
        xi = uniform_generator.next()
        for i in range(len(y_values) - 1):
            if y_distrib_func[x][y_values[i]] < xi <= y_distrib_func[x][y_values[i + 1]]:
                y = y_values[i]
                break
        else:
            y = y_values[-1]
        yield x, y


def get_expected_value_x(probabilities, x_values):
    exp_value_x = 0
    for i, x in enumerate(x_values):
        for prob in probabilities[i]:
            exp_value_x += x * prob
    return exp_value_x


def get_expected_value_y(probabilities, y_values):
    exp_value_y = 0
    for j, y in enumerate(y_values):
        for i in range(len(probabilities)):
            exp_value_y += y * probabilities[i][j]
    return exp_value_y


def get_dispersion_x(probabilities, x_values, exp_value_x):
    disp_x = 0
    for i, x in enumerate(x_values):
        for prob in probabilities[i]:
            disp_x += prob * (x - exp_value_x) ** 2
    return disp_x


def get_dispersion_y(probabilities, y_values, exp_value_y):
    disp_y = 0
    for i, y in enumerate(y_values):
        for j in range(len(probabilities)):
            disp_y += probabilities[i][j] * (y - exp_value_y) ** 2
    return disp_y


def get_correlation_coefficient(probabilities, x_values, y_values):
    exp_value_x = get_expected_value_x(probabilities, x_values)
    exp_value_y = get_expected_value_y(probabilities, y_values)
    disp_x = get_dispersion_x(probabilities, x_values, exp_value_x)
    disp_y = get_dispersion_y(probabilities, y_values, exp_value_y)
    covariance_coefficient = 0
    for i, x in enumerate(x_values):
        for j, y in enumerate(y_values):
            covariance_coefficient += (x - exp_value_x) * (y - exp_value_y) * probabilities[i][j]
    return covariance_coefficient / (disp_x ** (1 / 2) * disp_y ** (1 / 2))


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
        barchart = []
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
            barchart.append((a_i, b_i, v / value_quantity))
        return barchart

    return func


def cleared_values(values):
    clr_values = []
    for x in values:
        if x not in clr_values:
            clr_values.append(x)
    clr_values.sort()
    return clr_values

def get_conditional_distribution(x_values_inp, y_values_inp, gener_values):
    cond_distrib={}
    pair_quantity=len(gener_values)
    for x, y in gener_values:
        if x not in cond_distrib:
            cond_distrib[x]={}
            for y_in in y_values_inp:
                cond_distrib[x][y_in]=0
        cond_distrib[x][y]+=1/pair_quantity
    distrib_list=[]
    for x in x_values_inp:
        distrib_list.append([])
        for y in y_values_inp:
            distrib_list[-1].append(cond_distrib[x][y])
    return distrib_list
