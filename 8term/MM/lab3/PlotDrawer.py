from __future__ import division
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import matplotlib.pyplot as plt
import numpy as np
from RandomVariableGenerator import *
import Tkinter


class PlotDrawer:
    mainwin = None
    canvas = None
    bar_chart = ()

    def __init__(self, mainwin):
        self.mainwin = mainwin
        self.canvas = FigureCanvasTkAgg(plt.figure(), master=mainwin)
        self.canvas.show()
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky=Tkinter.NSEW)
        toolbar = NavigationToolbar2TkAgg(self.canvas, mainwin)
        toolbar.grid(row=1, column=0)
        toolbar.update()

    def draw(self, selection_size, *args):
        plot_rows = 2
        plot_cols = len(args) / 2 + len(args) % 2
        plot_index = 1
        plt.clf()
        for var_generator, cdf, pdf in args:
            subplt = plt.subplot(plot_rows, plot_cols, plot_index)
            plot_index += 1
            values = [var_generator.next() for _ in range(selection_size)]
            left, heights, width = get_bar_chart(25, min(values), max(values))(values)
            subplt.hist(values, normed=True)
            x = np.linspace(min(values), max(values), 1000)
            y = pdf(x)
            subplt.plot(x, y, color='r', label='theoretical PDF')
            expvalue_confidence = expvalue_confidence_interval(values, 0.95)
            dispersion_confidence = dispersion_confidence_interval(values, 0.95)
            subplt.set_title("M={:.1f} ({:.1f};{:.1f})   D={:.1f} ({:.1f};{:.1f}) {}".format(
                estimate_expvalue(values), expvalue_confidence[0], expvalue_confidence[1],
                estimate_dispersion(values), dispersion_confidence[0], dispersion_confidence[1],
                pearson_criteria(zip(left, heights), width, len(values), 0.6, cdf, 1)[0]
            ))
            subplt.set_xlabel('X')
            subplt.set_ylabel('Density')
        self.canvas.draw()
