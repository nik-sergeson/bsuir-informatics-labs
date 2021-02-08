from __future__ import division
from lab3.PlotDrawer import PlotDrawer
from Tkinter import *
from lab4.DiscreteRandomVariable import *
from scipy.stats import expon, uniform, norm, gamma, triang


def quit_wrapper(mainwin):
    def quit():
        mainwin.destroy()
        sys.exit()

    return quit

def get_distribution_function(scale):
    def distribution_func(x):
        if x>=0:
            return 1-math.exp(-x*scale)
        else:
            return 0
    return distribution_func


def main(args):
    mainwin = Tk()
    mainwin.columnconfigure(0, weight=1)
    mainwin.rowconfigure(0, weight=1)
    plotdrawer = PlotDrawer(mainwin)
    var_generators = []
    rv = expon(scale=5)
    var_generators.append((discrete_random_variable_simulator(rv, 1000), rv.cdf, rv.pdf))
    rv = uniform(loc=-1, scale=2)
    var_generators.append((discrete_random_variable_simulator(rv, 1000), rv.cdf, rv.pdf))
    rv = norm(loc=0, scale=2)
    var_generators.append((discrete_random_variable_simulator(rv, 1000), rv.cdf, rv.pdf))
    rv = gamma(3, loc=0., scale=1 / 2)
    var_generators.append((discrete_random_variable_simulator(rv, 1000), rv.cdf, rv.pdf))
    rv = triang(1, loc=0, scale=2)
    var_generators.append((discrete_random_variable_simulator(rv, 1000), rv.cdf, rv.pdf))
    rv = triang(1 / 2, loc=0, scale=2)
    var_generators.append((discrete_random_variable_simulator(rv, 1000), rv.cdf, rv.pdf))
    plotdrawer.draw(1000, *var_generators)
    mainwin.mainloop()


if __name__ == "__main__":
    main(sys.argv)
