from __future__ import division
from lab1.RandomGenerator import square_middle_method
from lab3.PlotDrawer import PlotDrawer
from scipy.stats import expon, uniform, norm, gamma, triang
from Tkinter import *
from lab3.RandomVariableGenerator import *
import math


def quit_wrapper(mainwin):
    def quit():
        mainwin.destroy()
        sys.exit()

    return quit


def distribution_func(x):
    if x >= 0:
        return 1 - math.exp(-x / 5)
    else:
        return 0


def main(args):
    mainwin = Tk()
    mainwin.columnconfigure(0, weight=1)
    mainwin.rowconfigure(0, weight=1)
    plotdrawer = PlotDrawer(mainwin)
    var_generators = []
    rv = expon(scale=5)
    var_generators.append((get_exponential_distr(square_middle_method(8, 17856392), 1 / 5), rv.cdf, rv.pdf))
    rv = uniform(loc=-1, scale=2)
    var_generators.append((get_uniform_distr(square_middle_method(8, 17856392), -1, 1), rv.cdf, rv.pdf))
    rv = norm(loc=0, scale=2)
    var_generators.append((get_gauss_distr(square_middle_method(8, 17856392), 0, 2), rv.cdf, rv.pdf))
    rv = gamma(3, loc=0., scale=1 / 2)
    var_generators.append((get_gamma_distr(square_middle_method(8, 17856392), 3, 2), rv.cdf, rv.pdf))
    rv = triang(1, loc=0, scale=2)
    var_generators.append((get_triang_distr(square_middle_method(8, 17856392), 0, 2), rv.cdf, rv.pdf))
    rv = triang(1 / 2, loc=0, scale=2)
    var_generators.append((get_simpson_distr(0, 2), rv.cdf, rv.pdf))
    plotdrawer.draw(1000, *var_generators)
    mainwin.mainloop()


if __name__ == "__main__":
    main(sys.argv)
