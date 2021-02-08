import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

__author__ = 'nik-u'

import matplotlib.pyplot as plt

from solver import Solver
from Tkinter import *


class Controller:
    plot_type = None
    leftborder_entry = None
    rightborder_entry = None
    solver = None
    mainwin = None
    treeview_top = None
    treeview_bottom = None

    def __init__(self, solver, mainwin):
        self.alpha = [1 - i / 100. for i in range(1, 30)]
        self.valuescount = [20, 30, 50, 70, 100, 150]
        self.sub_alpha = [0.99, 0.97, 0.95, 0.94, 0.91, 0.9]
        self.solver = solver
        self.mainwin = mainwin
        self.canvas = FigureCanvasTkAgg(plt.figure(), master=mainwin)
        self.canvas.show()
        self.canvas.get_tk_widget().grid(row=0, column=0, columnspan=6, rowspan=2)
        toolbar = NavigationToolbar2TkAgg(self.canvas, mainwin)
        toolbar.grid(row=2, column=0, columnspan=6)
        toolbar.update()

    def draw_button_clicked(self):
        leftborder = float(self.leftborder_entry.get())
        rightborder = float(self.rightborder_entry.get())
        func = self.solver.get_function()
        plot_cols = len(self.valuescount) / 2 + len(self.valuescount) % 2
        plot_rows = 2
        for i in self.treeview_top.get_children():
            self.treeview_top.delete(i)
        for i in self.treeview_bottom.get_children():
            self.treeview_bottom.delete(i)
        plt.clf()
        values = {}
        for i in self.valuescount:
            values[i] = map(func, self.solver.get_uniform_values(leftborder, rightborder, i))
        if self.plot_type.get() == 1:
            self.treeview_top["columns"] = ("alpha",) + tuple(str(count) for count in self.valuescount)
            self.treeview_bottom["columns"] = ("alpha",) + tuple(str(count) for count in self.valuescount)
            for column_name in self.treeview_top["columns"]:
                self.treeview_top.heading(column_name, text=column_name)
                self.treeview_top.column(column_name, width=100, stretch=NO)
                self.treeview_bottom.heading(column_name, text=column_name)
                self.treeview_bottom.column(column_name, width=100, stretch=NO)
            table_known_dispersion = {}
            table_unknown_dispersion = {}
            for alpha_iter in self.alpha:
                table_known_dispersion[alpha_iter] = [str(alpha_iter)]
                table_unknown_dispersion[alpha_iter] = [str(alpha_iter)]
            self.mainwin.wm_title("Expected value confidence intervals(depending on alpha)")
            for cur_count in self.valuescount:
                confidence_intervals_unknown_dispersion = [
                    self.solver.expvalue_confidence_interval(values[cur_count], x) for x in self.alpha]
                confidence_intervals_known_dispersion = [
                    self.solver.expvalue_confidence_interval_known_dispersion(values[cur_count],
                                                                              self.solver.theor_dispersion, x) for x in
                    self.alpha]
                for alpha_iter in self.alpha:
                    interval = confidence_intervals_unknown_dispersion[self.alpha.index(alpha_iter)]
                    table_unknown_dispersion[alpha_iter].append(str(round(interval[1] - interval[0], 2)))
                    interval = confidence_intervals_known_dispersion[self.alpha.index(alpha_iter)]
                    table_known_dispersion[alpha_iter].append(str(round(interval[1] - interval[0], 2)))
                subplt = plt.subplot(plot_rows, plot_cols, self.valuescount.index(cur_count) + 1)
                plt.title("n={0}".format(cur_count))
                plt.axis([min(self.alpha), max(self.alpha), 0, 0.5])
                subplt.plot(self.alpha, [b - a for a, b in confidence_intervals_unknown_dispersion],
                            label="unknown disp")
                subplt.plot(self.alpha, [b - a for a, b in confidence_intervals_known_dispersion], label="known disp")
                subplt.legend()
            for alpha_iter in self.alpha:
                self.treeview_top.insert("", 0, values=table_known_dispersion[alpha_iter])
                self.treeview_bottom.insert("", 0, values=table_unknown_dispersion[alpha_iter])
        elif self.plot_type.get() == 2:
            self.treeview_top["columns"] = ("alpha",) + tuple(str(count) for count in self.valuescount)
            self.treeview_bottom["columns"] = ("alpha",) + tuple(str(count) for count in self.valuescount)
            for column_name in self.treeview_top["columns"]:
                self.treeview_top.heading(column_name, text=column_name)
                self.treeview_top.column(column_name, width=100, stretch=NO)
                self.treeview_bottom.heading(column_name, text=column_name)
                self.treeview_bottom.column(column_name, width=100, stretch=NO)
            table_known_dispersion = {}
            table_unknown_dispersion = {}
            for alpha_iter in self.sub_alpha:
                table_known_dispersion[alpha_iter] = [str(alpha_iter)]
                table_unknown_dispersion[alpha_iter] = [str(alpha_iter)]
            self.mainwin.wm_title("Expected value confidence intervals(depending on selection size)")
            for cur_alpha in self.sub_alpha:
                confidence_intervals_unknown_dispersion = [
                    self.solver.expvalue_confidence_interval(values[x], cur_alpha) for x in self.valuescount]
                confidence_intervals_known_dispersion = [
                    self.solver.expvalue_confidence_interval_known_dispersion(values[x], self.solver.theor_dispersion,
                                                                              cur_alpha) for x in self.valuescount]
                for alpha_iter in self.sub_alpha:
                    interval = confidence_intervals_unknown_dispersion[self.sub_alpha.index(alpha_iter)]
                    table_unknown_dispersion[alpha_iter].append(str(round(interval[1] - interval[0], 2)))
                    interval = confidence_intervals_known_dispersion[self.sub_alpha.index(alpha_iter)]
                    table_known_dispersion[alpha_iter].append(str(round(interval[1] - interval[0], 2)))
                subplt = plt.subplot(plot_rows, plot_cols, self.sub_alpha.index(cur_alpha) + 1)
                plt.title("alpha={0}".format(cur_alpha))
                plt.axis([min(self.valuescount), max(self.valuescount), 0, 0.5])
                subplt.plot(self.valuescount, [b - a for a, b in confidence_intervals_unknown_dispersion],
                            label="unknown disp")
                subplt.plot(self.valuescount, [b - a for a, b in confidence_intervals_known_dispersion],
                            label="known disp")
                subplt.legend()
            for alpha_iter in self.sub_alpha:
                self.treeview_top.insert("", 0, values=table_known_dispersion[alpha_iter])
                self.treeview_bottom.insert("", 0, values=table_unknown_dispersion[alpha_iter])
        elif self.plot_type.get() == 3:
            self.treeview_top["columns"] = ("alpha",) + tuple(str(count) for count in self.valuescount)
            self.treeview_bottom["columns"] = ("alpha",) + tuple(str(count) for count in self.valuescount)
            for column_name in self.treeview_top["columns"]:
                self.treeview_top.heading(column_name, text=column_name)
                self.treeview_top.column(column_name, width=100, stretch=NO)
                self.treeview_bottom.heading(column_name, text=column_name)
                self.treeview_bottom.column(column_name, width=100, stretch=NO)
            table_known_expvalue = {}
            table_unknown_expvalue = {}
            for alpha_iter in self.alpha:
                table_known_expvalue[alpha_iter] = [str(alpha_iter)]
                table_unknown_expvalue[alpha_iter] = [str(alpha_iter)]
            self.mainwin.wm_title("Dispersion confidence intervals(depending on alpha)")
            for cur_count in self.valuescount:
                confidence_intervals_unknown_expvalue = [
                    self.solver.dispersion_confidence_interval(values[cur_count], x) for x in self.alpha]
                confidence_intervals_known_expvalue = [
                    self.solver.dispersion_confidence_interval_known_expvalue(values[cur_count], x,
                                                                              self.solver.ther_expvalue) for x in
                    self.alpha]
                for alpha_iter in self.alpha:
                    interval = confidence_intervals_known_expvalue[self.alpha.index(alpha_iter)]
                    table_known_expvalue[alpha_iter].append(str(round(interval[1] - interval[0], 2)))
                    interval = confidence_intervals_unknown_expvalue[self.alpha.index(alpha_iter)]
                    table_unknown_expvalue[alpha_iter].append(str(round(interval[1] - interval[0], 2)))
                subplt = plt.subplot(plot_rows, plot_cols, self.valuescount.index(cur_count) + 1)
                plt.title("n={0}".format(cur_count))
                plt.axis([min(self.alpha), max(self.alpha), 0, 0.5])
                subplt.plot(self.alpha, [b - a for a, b in confidence_intervals_unknown_expvalue],
                            label="unknown expvalue")
                subplt.plot(self.alpha, [b - a for a, b in confidence_intervals_known_expvalue], label="known expvalue")
                subplt.legend()
            for alpha_iter in self.alpha:
                self.treeview_top.insert("", 0, values=table_known_expvalue[alpha_iter])
                self.treeview_bottom.insert("", 0, values=table_unknown_expvalue[alpha_iter])
        elif self.plot_type.get() == 4:
            self.treeview_top["columns"] = ("alpha",) + tuple(str(count) for count in self.valuescount)
            self.treeview_bottom["columns"] = ("alpha",) + tuple(str(count) for count in self.valuescount)
            for column_name in self.treeview_top["columns"]:
                self.treeview_top.heading(column_name, text=column_name)
                self.treeview_top.column(column_name, width=100, stretch=NO)
                self.treeview_bottom.heading(column_name, text=column_name)
                self.treeview_bottom.column(column_name, width=100, stretch=NO)
            table_known_expvalue = {}
            table_unknown_expvalue = {}
            for alpha_iter in self.sub_alpha:
                table_known_expvalue[alpha_iter] = [str(alpha_iter)]
                table_unknown_expvalue[alpha_iter] = [str(alpha_iter)]
            self.mainwin.wm_title("Dispersion confidence intervals(depending on selection size)")
            for cur_alpha in self.sub_alpha:
                confidence_intervals_unknown_expvalue = [
                    self.solver.dispersion_confidence_interval(values[x], cur_alpha) for x in self.valuescount]
                confidence_intervals_known_expvalue = [
                    self.solver.dispersion_confidence_interval_known_expvalue(values[x], cur_alpha,
                                                                              self.solver.ther_expvalue) for x in
                    self.valuescount]
                subplt = plt.subplot(plot_rows, plot_cols, self.sub_alpha.index(cur_alpha) + 1)
                plt.title("alpha={0}".format(cur_alpha))
                plt.axis([min(self.valuescount), max(self.valuescount), 0, 0.5])
                for alpha_iter in self.sub_alpha:
                    interval = confidence_intervals_unknown_expvalue[self.sub_alpha.index(alpha_iter)]
                    table_unknown_expvalue[alpha_iter].append(str(round(interval[1] - interval[0], 2)))
                    interval = confidence_intervals_known_expvalue[self.sub_alpha.index(alpha_iter)]
                    table_known_expvalue[alpha_iter].append(str(round(interval[1] - interval[0], 2)))
                subplt.plot(self.valuescount, [b - a for a, b in confidence_intervals_unknown_expvalue],
                            label="unknown expvalue")
                subplt.plot(self.valuescount, [b - a for a, b in confidence_intervals_known_expvalue],
                            label="known expvalue")
                subplt.legend()
            for alpha_iter in self.sub_alpha:
                self.treeview_top.insert("", 0, values=table_known_expvalue[alpha_iter])
                self.treeview_bottom.insert("", 0, values=table_unknown_expvalue[alpha_iter])
        self.canvas.draw()


def quit_wrapper(mainwin):
    def quit():
        mainwin.destroy()
        sys.exit()

    return quit


def main(args):
    mainwin = Tk()
    solver = Solver()
    plot_type = IntVar()
    controller = Controller(solver, mainwin)
    controller.plot_type = plot_type
    rbutton1 = Radiobutton(mainwin, text="Expected value confidence intervals(depending on alpha)", variable=plot_type,
                           value=1)
    rbutton2 = Radiobutton(mainwin, text="Expected value confidence interval(unknown dispersion)", variable=plot_type,
                           value=2)
    rbutton3 = Radiobutton(mainwin, text="Dispersion confidence intervals(depending on alpha)", variable=plot_type,
                           value=3)
    rbutton4 = Radiobutton(mainwin, text="Dispersion confidence interval(unknown expected value)", variable=plot_type,
                           value=4)
    plot_type.set(1)
    rbutton1.grid(row=3, column=0, sticky=W)
    rbutton2.grid(row=4, column=0, sticky=W)
    rbutton3.grid(row=5, column=0, sticky=W)
    rbutton4.grid(row=6, column=0, sticky=W)
    leftborder_entry = Entry(mainwin)
    leftborder_entry.insert(0, -1)
    controller.leftborder_entry = leftborder_entry
    leftborder_entry.grid(column=2, row=3)
    leftborder_label = Label(mainwin, text='Left border')
    leftborder_label.grid(column=1, row=3)
    rightborder_entry = Entry(mainwin)
    rightborder_entry.insert(0, 1)
    controller.rightborder_entry = rightborder_entry
    rightborder_entry.grid(column=2, row=4)
    rightborder_label = Label(mainwin, text='Right border')
    rightborder_label.grid(column=1, row=4)
    controller.treeview_top = ttk.Treeview(mainwin)
    controller.treeview_top.grid(column=6, row=0, sticky='ns', columnspan=5)
    controller.treeview_top['show'] = 'headings'
    controller.treeview_bottom = ttk.Treeview(mainwin)
    controller.treeview_bottom.grid(column=6, row=1, sticky='ns', columnspan=5)
    controller.treeview_bottom['show'] = 'headings'
    quit_func = quit_wrapper(mainwin)
    exit_button = Button(text='Exit', command=quit_func)
    exit_button.grid(column=3, row=4)
    draw_button = Button(text='Draw', command=controller.draw_button_clicked)
    draw_button.grid(column=3, row=3)
    mainwin.mainloop()


if __name__ == "__main__":
    main(sys.argv)
