import Tkinter

from Solver import Solver

__author__ = 'nik-u'
from Tkinter import *
import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


class PlotDrawer:
    edgefactor = 1.3
    val_quantity_entry = None
    leftborder_entry = None
    rightborder_entry = None
    treeview = None
    mainwin = None
    canvas = None
    leftborder = 0
    rightborder = 0
    precision_entry = None
    probabilities = {}

    def __init__(self, solver, mainwin):
        self.solver = solver
        self.mainwin = mainwin
        self.canvas = FigureCanvasTkAgg(plt.figure(), master=mainwin)
        self.canvas.show()
        self.canvas.get_tk_widget().grid(row=0, column=0, columnspan=8)
        toolbar = NavigationToolbar2TkAgg(self.canvas, mainwin)
        toolbar.grid(row=1, column=0, columnspan=8)
        toolbar.update()

    def update_values(self):
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        func = self.solver.get_function()
        self.leftborder = float(self.leftborder_entry.get())
        self.rightborder = float(self.rightborder_entry.get())
        valueslist = sorted(map(func, self.solver.get_uniform_values(self.leftborder, self.rightborder,
                                                                     int(self.val_quantity_entry.get()))))
        valueslist = [round(x, int(self.precision_entry.get())) for x in valueslist]
        self.probabilities = self.solver.get_probabilities(valueslist)
        freqs = self.solver.get_frequency_series(valueslist)
        for x in sorted(freqs.keys()):
            self.treeview.insert("", 0, values=(str(x), str(freqs.get(x))))
        self.draw_separately()

    def draw_separately(self):
        plt.clf()
        plt.subplot(2, 1, 1)
        plt.xlabel('Y')
        plt.ylabel('F*(Y)')
        plt.title('Empirical function')
        x = sorted(self.probabilities.keys())
        plt.axis([self.edgefactor * x[0], self.edgefactor * x[-1], -0.1, 1.1])
        y = [self.probabilities.get(key) for key in x]
        x.insert(0, self.edgefactor * x[0])
        x.append(self.edgefactor * x[-1])
        y.insert(0, 0)
        y.append(1)
        for i in range(len(x) - 1):
            plt.arrow(x[i + 1], y[i + 1], x[i] - x[i + 1], 0, length_includes_head=True, fc='k', ec='k')
        plt.subplot(2, 1, 2)
        plt.xlabel('Y')
        plt.ylabel('F(Y)=1/4*(y**1/3+2)')
        plt.title('Theoretical function')
        plt.axis([x[0], x[-1], -0.1, 1.1])
        distrib_func = self.solver.get_distrib_func(self.leftborder, self.rightborder)
        plt.plot(x, [distrib_func(a) for a in x])
        self.canvas.draw()

    def draw_together(self):
        plt.clf()
        plt.xlabel('Y')
        plt.ylabel('F(Y)')
        plt.title('Compare function')
        x = sorted(self.probabilities.keys())
        plt.axis([self.edgefactor * x[0], self.edgefactor * x[-1], -0.05, 1.2])
        y = [self.probabilities.get(key) for key in x]
        x.insert(0, self.edgefactor * x[0])
        x.append(self.edgefactor * x[-1])
        y.insert(0, 0)
        y.append(1)
        for i in range(len(x) - 1):
            plt.arrow(x[i + 1], y[i + 1], x[i] - x[i + 1], 0, length_includes_head=True, fc='k', ec='k')
        distrib_func = self.solver.get_distrib_func(self.leftborder, self.rightborder)
        lines = plt.plot(x, [distrib_func(a) for a in x])
        plt.setp(lines, color='r')
        red_patch = mpatches.Patch(color='red', label='theoretical')
        blue_patch = mpatches.Patch(color='blue', label='empirical')
        plt.legend(handles=[red_patch, blue_patch])
        self.canvas.draw()


def quit_wrapper(mainwin):
    def quit():
        mainwin.destroy()
        sys.exit()

    return quit


def main(args):
    mainwin = Tk()
    solver = Solver()
    plotdrawer = PlotDrawer(solver, mainwin)
    # widgets
    val_quantity_entry = Entry(mainwin)
    val_quantity_entry.insert(0, 100)
    plotdrawer.val_quantity_entry = val_quantity_entry
    val_quantity_entry.grid(column=1, row=2)
    val_label = Label(mainwin, text='Values quantity')
    val_label.grid(column=0, row=2)
    leftborder_entry = Entry(mainwin)
    leftborder_entry.insert(0, -2)
    plotdrawer.leftborder_entry = leftborder_entry
    leftborder_entry.grid(column=3, row=2)
    leftborder_label = Label(mainwin, text='Left border')
    leftborder_label.grid(column=2, row=2)
    rightborder_entry = Entry(mainwin)
    rightborder_entry.insert(0, 2)
    plotdrawer.rightborder_entry = rightborder_entry
    rightborder_entry.grid(column=5, row=2)
    rightborder_label = Label(mainwin, text='Right border')
    rightborder_label.grid(column=4, row=2)
    precision_entry = Entry(mainwin)
    precision_entry.insert(0, 2)
    plotdrawer.precision_entry = precision_entry
    precision_entry.grid(column=7, row=2)
    precision_label = Label(mainwin, text='Precision')
    precision_label.grid(column=6, row=2)
    update_button = Button(text='Update', command=plotdrawer.update_values)
    update_button.grid(column=8, row=2)
    draw_separetely_button = Button(text='Draw Separately', command=plotdrawer.draw_separately)
    draw_separetely_button.grid(column=9, row=2)
    quit_func = quit_wrapper(mainwin)
    draw_together_button = Button(text='Draw Together', command=plotdrawer.draw_together)
    draw_together_button.grid(column=10, row=2)
    exit_button = Button(text='Exit', command=quit_func)
    exit_button.grid(column=11, row=2)
    plotdrawer.treeview = ttk.Treeview(mainwin)
    plotdrawer.treeview.grid(column=8, row=0, sticky='ns', columnspan=4)
    plotdrawer.treeview['show'] = 'headings'
    plotdrawer.treeview["columns"] = ("value", "frequency")
    plotdrawer.treeview.heading("value", text="value")
    plotdrawer.treeview.heading("frequency", text="frequency")
    plotdrawer.update_values()
    mainwin.mainloop()


if __name__ == "__main__":
    main(sys.argv)
