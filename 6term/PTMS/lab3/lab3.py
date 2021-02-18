from solver import Solver

import sys
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
    bar_chart = ()

    def __init__(self, solver, mainwin):
        self.solver = solver
        self.mainwin = mainwin
        self.canvas = FigureCanvasTkAgg(plt.figure(), master=mainwin)
        self.canvas.show()
        self.canvas.get_tk_widget().grid(row=0, column=0, columnspan=6)
        toolbar = NavigationToolbar2TkAgg(self.canvas, mainwin)
        toolbar.grid(row=1, column=0, columnspan=6)
        toolbar.update()

    def update_values(self):
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        func = self.solver.get_function()
        self.leftborder = float(self.leftborder_entry.get())
        self.rightborder = float(self.rightborder_entry.get())
        valueslist = sorted(map(func, self.solver.get_uniform_values(self.leftborder, self.rightborder,
                                                                     int(self.val_quantity_entry.get()))))
        self.bar_chart = self.solver.getbarchart(len(valueslist), valueslist)
        for a, b, f in self.bar_chart:
            self.treeview.insert("", 0, values=(str(a), str(b), str(f)))
        self.draw_emperical()

    def draw_emperical(self):
        plt.clf()
        x_pol = []
        y_pol = []
        for a, b, f in self.bar_chart:
            plt.bar(a, f, width=b - a)
            x_pol.append((a + b) / 2.)
            y_pol.append(f)
        lines = plt.plot(x_pol, y_pol)
        plt.setp(lines, color='r')
        x_theor_density = [self.bar_chart[0][0] * self.edgefactor, self.bar_chart[0][0]] + list(x_pol) + [
            self.bar_chart[-1][1], self.bar_chart[-1][1] * self.edgefactor]
        y_theor_density = [0, 0]
        average_func_value = self.solver.func_average_value(self.leftborder, self.rightborder)
        for a, b, f in self.bar_chart:
            y_theor_density.append(average_func_value(a, b))
        y_theor_density += [0, 0]
        plt.axis([self.bar_chart[0][0] * self.edgefactor, self.bar_chart[-1][1] * self.edgefactor, -0.01,
                  max(y_theor_density + y_pol) * self.edgefactor])
        lines = plt.plot(x_theor_density, y_theor_density)
        plt.setp(lines, color='g')
        plt.title('Empirical bars, density func')
        plt.xlabel('Y')
        plt.ylabel('Density')
        self.canvas.draw()

    def draw_together(self):
        plt.clf()
        x_pol = []
        y_pol = []
        for a, b, f in self.bar_chart:
            x_pol.append((a + b) / 2.)
            y_pol.append(f)
        plt.xlabel('Y')
        plt.ylabel('f(Y)')
        plt.title('Compare function')
        lines = plt.plot(x_pol, y_pol)
        plt.setp(lines, color='b')
        x_theor_density = [self.bar_chart[0][0] * self.edgefactor, self.bar_chart[0][0]] + list(x_pol) + [
            self.bar_chart[-1][1], self.bar_chart[-1][1] * self.edgefactor]
        y_theor_density = [0, 0]
        average_func_value = self.solver.func_average_value(self.leftborder, self.rightborder)
        for a, b, f in self.bar_chart:
            y_theor_density.append(average_func_value(a, b))
        y_theor_density += [0, 0]
        plt.axis([self.bar_chart[0][0] * self.edgefactor, self.bar_chart[-1][1] * self.edgefactor, -0.01,
                  max(y_theor_density + y_pol) * self.edgefactor])
        lines = plt.plot(x_theor_density, y_theor_density)
        plt.setp(lines, color='r')
        red_patch = mpatches.Patch(color='red', label='theoretical,f=1/(12*y**2/3)')
        blue_patch = mpatches.Patch(color='blue', label='empirical')
        plt.legend(handles=[red_patch, blue_patch])
        self.canvas.draw()

    def draw_distribution_function(self):
        plt.clf()
        y_emper_distrib = [0]
        for a, b, f in self.bar_chart:
            y_emper_distrib.append(y_emper_distrib[-1] + (b - a) * f)
        x_emper_distrib = [self.bar_chart[0][0] * self.edgefactor] + [a[0] for a in self.bar_chart[1:]] + [
            self.bar_chart[-1][1], self.bar_chart[-1][1] * self.edgefactor]
        y_emper_distrib.append(1)
        plt.axis([self.bar_chart[0][0] * self.edgefactor, self.bar_chart[-1][1] * self.edgefactor, -0.01, 1.1])
        for i in range(len(x_emper_distrib) - 1):
            plt.arrow(x_emper_distrib[i + 1], y_emper_distrib[i], x_emper_distrib[i] - x_emper_distrib[i + 1], 0,
                      length_includes_head=True, fc='k', ec='k')
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
    val_quantity_entry.insert(0, 30)
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
    update_button = Button(text='Update', command=plotdrawer.update_values)
    update_button.grid(column=6, row=2)
    draw_emperical_button = Button(text='Emperical', command=plotdrawer.draw_emperical)
    draw_emperical_button.grid(column=7, row=2)
    draw_separetely_button = Button(text='Draw Together', command=plotdrawer.draw_together)
    draw_separetely_button.grid(column=8, row=2)
    quit_func = quit_wrapper(mainwin)
    draw_together_button = Button(text='Distribution func', command=plotdrawer.draw_distribution_function)
    draw_together_button.grid(column=9, row=2)
    exit_button = Button(text='Exit', command=quit_func)
    exit_button.grid(column=10, row=2)
    plotdrawer.treeview = ttk.Treeview(mainwin)
    plotdrawer.treeview.grid(column=6, row=0, sticky='ns', columnspan=5)
    plotdrawer.treeview['show'] = 'headings'
    plotdrawer.treeview["columns"] = ("a", "b", "frequency")
    plotdrawer.treeview.heading("a", text="a")
    plotdrawer.treeview.heading("b", text="b")
    plotdrawer.treeview.heading("frequency", text="frequency")
    plotdrawer.update_values()
    mainwin.mainloop()


if __name__ == "__main__":
    main(sys.argv)
