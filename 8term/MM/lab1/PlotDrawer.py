from __future__ import division
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from RandomGenerator import get_expected_value, get_dispersion, estimate_correlation
import matplotlib.pyplot as plt
import Tkinter


class PlotDrawer:
    mainwin = None
    canvas = None
    n_arr = [100, 1000]
    bar_chart = ()

    def __init__(self, mainwin):
        self.mainwin = mainwin
        self.canvas = FigureCanvasTkAgg(plt.figure(), master=mainwin)
        self.canvas.show()
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky=Tkinter.NSEW)
        toolbar = NavigationToolbar2TkAgg(self.canvas, mainwin)
        toolbar.grid(row=1, column=0)
        toolbar.update()

    def draw(self, get_bar_chart, *args):
        plot_rows = len(args)
        plot_cols = len(self.n_arr)
        plot_index = 1
        plt.clf()
        for random_generator in args:
            for n in self.n_arr:
                subplt = plt.subplot(plot_rows, plot_cols, plot_index)
                plot_index += 1
                values = [random_generator.next() for i in range(n)]
                left,heights, width = get_bar_chart(values)
                subplt.bar(left, heights, width=width)
                expected_value = get_expected_value(values)
                plt.title("n={}, M={:.3f}, D={:.3f}, R={:.3f}".format(n, expected_value,
                                                                      get_dispersion(values, expected_value),
                                                                      estimate_correlation(values, 2)))
                plt.axis([0, 1, 0, 1])
                plt.xlabel('X')
                plt.ylabel('Density')
        self.canvas.draw()
