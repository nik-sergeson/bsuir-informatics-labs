__author__ = 'nik-u'

from Tkinter import *

from solver import Solver


class Controller:
    normal_check=None
    uniform_check=None
    exponential_check=None
    theoretical_check=None
    chosen_criteria=None
    leftborder_entry=None
    rightborder_entry=None
    alpha_entry=None
    selection_size_entry=None
    solver=None
    out_text=None

    def __init__(self, solver):
        self.solver=solver

    def pearson_chosen(self):
        self.selection_size_entry.delete(0, END)
        self.selection_size_entry.insert(0, 200)

    def kolmogorov_chosen(self):
        self.selection_size_entry.delete(0, END)
        self.selection_size_entry.insert(0, 30)

    def mises_chosen(self):
        self.selection_size_entry.delete(0, END)
        self.selection_size_entry.insert(0, 50)

    def test_button_clicked(self):
        self.out_text.delete('0.0',END)
        leftborder=int(self.leftborder_entry.get())
        rightborder=int(self.rightborder_entry.get())
        alpha=float(self.alpha_entry.get())
        func=self.solver.get_function()
        if self.chosen_criteria.get()==1:
            values_pearson = sorted(map(func,self.solver.get_uniform_values(leftborder, rightborder, int(self.selection_size_entry.get()))))
            intervals=self.solver.getbarchart(len(values_pearson), values_pearson)
            exp_value=self.solver.estimate_expvalue(values_pearson)
            dispersion=self.solver.estimate_dispersion(values_pearson)
            if self.normal_check.get()==1:
                normal_distr=self.solver.get_normal_distribution_func(exp_value, dispersion)
                answ, chi, q=self.solver.pearson_criteria(intervals, len(values_pearson), alpha, normal_distr, 2)
                self.out_text.insert(INSERT,"Normal distribution: {0}; criteria={1}; table={2}\n".format(answ, round(chi,2), round(q,2)))
            if self.uniform_check.get()==1:
                uniform_distr=self.solver.get_uniform_distribution_func(exp_value, dispersion)
                answ, chi, q=self.solver.pearson_criteria(intervals, len(values_pearson), alpha, uniform_distr, 0)
                self.out_text.insert(INSERT,"Uniform distribution: {0}; criteria={1}; table={2}\n".format(answ, round(chi,2), round(q,2)))
            if self.exponential_check.get()==1:
                exponential_distr=self.solver.get_exponential_distribution_func(exp_value)
                answ, chi, q=self.solver.pearson_criteria(intervals, len(values_pearson), alpha, exponential_distr, 1)
                self.out_text.insert(INSERT,"Exponential distribution: {0}; criteria={1}; table={2}\n".format(answ, round(chi,2), round(q,2)))
            if self.theoretical_check.get()==1:
                theor_distr=self.solver.get_distrib_func(leftborder, rightborder)
                answ, chi, q=self.solver.pearson_criteria(intervals, len(values_pearson), alpha, theor_distr, 0)
                self.out_text.insert(INSERT,"Theoretical distribution: {0}; criteria={1}; table={2}\n".format(answ, round(chi,2), round(q,2)))
        elif self.chosen_criteria.get()==2:
            values_kolmogorov = sorted(map(func,self.solver.get_uniform_values(leftborder, rightborder, int(self.selection_size_entry.get()))))
            exp_value=self.solver.estimate_expvalue(values_kolmogorov)
            dispersion=self.solver.estimate_dispersion(values_kolmogorov)
            if self.normal_check.get()==1:
                normal_distr=self.solver.get_normal_distribution_func(exp_value, dispersion)
                answ, l, critical=self.solver.kolmogorov_criteria(values_kolmogorov,alpha, normal_distr)
                self.out_text.insert(INSERT,"Normal distribution: {0}; criteria={1}; critical={2}\n".format(answ, l, critical))
            if self.uniform_check.get()==1:
                uniform_distr=self.solver.get_uniform_distribution_func(exp_value, dispersion)
                answ, l, critical=self.solver.kolmogorov_criteria(values_kolmogorov, alpha, uniform_distr)
                self.out_text.insert(INSERT,"Uniform distribution: {0}; criteria={1}; critical={2}\n".format(answ, l, critical))
            if self.exponential_check.get()==1:
                exponential_distr=self.solver.get_exponential_distribution_func(exp_value)
                answ, l, critical=self.solver.kolmogorov_criteria(values_kolmogorov, alpha, exponential_distr)
                self.out_text.insert(INSERT,"Exponential distribution: {0}; criteria={1}; critical={2}\n".format(answ, l, critical))
            if self.theoretical_check.get()==1:
                theor_distr=self.solver.get_distrib_func(leftborder, rightborder)
                answ, l, critical=self.solver.kolmogorov_criteria(values_kolmogorov, alpha, theor_distr)
                self.out_text.insert(INSERT,"Theoretical distribution: {0}; criteria={1}; critical={2}\n".format(answ, l, critical))
        elif self.chosen_criteria.get()==3:
            values_mises = sorted(map(func,self.solver.get_uniform_values(leftborder, rightborder, int(self.selection_size_entry.get()))))
            exp_value=self.solver.estimate_expvalue(values_mises)
            dispersion=self.solver.estimate_dispersion(values_mises)
            if self.normal_check.get()==1:
                normal_distr=self.solver.get_normal_distribution_func(exp_value, dispersion)
                answ, omega, critical=self.solver.mises_criteria(values_mises, alpha, normal_distr)
                self.out_text.insert(INSERT,"Normal distribution: {0}; criteria={1}; critical={2}\n".format(answ, omega, critical))
            if self.uniform_check.get()==1:
                uniform_distr=self.solver.get_uniform_distribution_func(exp_value, dispersion)
                answ, omega, critical=self.solver.mises_criteria(values_mises, alpha, uniform_distr)
                self.out_text.insert(INSERT,"Uniform distribution: {0}; criteria={1}; critical={2}\n".format(answ, omega, critical))
            if self.exponential_check.get()==1:
                exponential_distr=self.solver.get_exponential_distribution_func(exp_value)
                answ, omega, critical=self.solver.mises_criteria(values_mises, alpha, exponential_distr)
                self.out_text.insert(INSERT,"Exponential distribution: {0}; criteria={1}; critical={2}\n".format(answ, omega, critical))
            if self.theoretical_check.get()==1:
                theor_distr=self.solver.get_distrib_func(leftborder, rightborder)
                answ, omega, critical=self.solver.mises_criteria(values_mises, alpha, theor_distr)
                self.out_text.insert(INSERT,"Theoretical distribution: {0}; criteria={1}; critical={2}\n".format(answ, omega, critical))

def quit_wrapper(mainwin):
    def quit():
        mainwin.destroy()
        sys.exit()
    return quit

def main(args):
    mainwin=Tk()
    solver = Solver()
    controller=Controller(solver)
    normal_check = IntVar()
    Checkbutton(mainwin, text="Normal distribution", variable=normal_check,onvalue = 1, offvalue = 0).grid(row=0,column=0, sticky=W)
    normal_check.set(1)
    controller.normal_check=normal_check
    uniform_check = IntVar()
    Checkbutton(mainwin, text="Uniform distribution", variable=uniform_check,onvalue = 1, offvalue = 0).grid(row=1, column=0, sticky=W)
    uniform_check.set(1)
    controller.uniform_check=uniform_check
    exponential_check = IntVar()
    Checkbutton(mainwin, text="Exponential distribution", variable=exponential_check,onvalue = 1, offvalue = 0).grid(row=2, column=0, sticky=W)
    exponential_check.set(1)
    controller.exponential_check=exponential_check
    theoretical_check = IntVar()
    Checkbutton(mainwin, text="Theoretical distribution", variable=theoretical_check,onvalue = 1, offvalue = 0).grid(row=3, column=0, sticky=W)
    theoretical_check.set(1)
    controller.theoretical_check=theoretical_check
    chosen_criteria=IntVar()
    controller.chosen_criteria=chosen_criteria
    rbutton1=Radiobutton(mainwin,text="Pearson criteria",variable=chosen_criteria,value=1, command=controller.pearson_chosen)
    rbutton2=Radiobutton(mainwin,text="Kolmogorov criteria",variable=chosen_criteria,value=2, command=controller.kolmogorov_chosen)
    rbutton3=Radiobutton(mainwin,text="Mises criteria",variable=chosen_criteria,value=3, command=controller.mises_chosen)
    chosen_criteria.set(1)
    rbutton1.grid(row=0, column=1,sticky=W)
    rbutton2.grid(row=1, column=1,sticky=W)
    rbutton3.grid(row=2, column=1, sticky=W)
    leftborder_entry = Entry(mainwin)
    leftborder_entry.insert(0, -1)
    controller.leftborder_entry=leftborder_entry
    leftborder_entry.grid(column=3, row=0)
    leftborder_label = Label(mainwin, text='Left border')
    leftborder_label.grid(column=2, row=0)
    rightborder_entry = Entry(mainwin)
    rightborder_entry.insert(0, 1)
    controller.rightborder_entry=rightborder_entry
    rightborder_entry.grid(column=3, row=1)
    rightborder_label = Label(mainwin, text='Right border')
    rightborder_label.grid(column=2, row=1)
    alpha_entry = Entry(mainwin)
    alpha_entry.insert(0, 0.05)
    controller.alpha_entry=alpha_entry
    alpha_entry.grid(column=3, row=2)
    alpha_label = Label(mainwin, text='Alpha')
    alpha_label.grid(column=2, row=2)
    selection_size_entry = Entry(mainwin)
    selection_size_entry.insert(0, 200)
    controller.selection_size_entry=selection_size_entry
    selection_size_entry.grid(column=3, row=3)
    selection_size_label = Label(mainwin, text='Selection size')
    selection_size_label.grid(column=2, row=3)
    test_button = Button(text='Test', command=controller.test_button_clicked)
    test_button.grid(column=5, row=0)
    quit_func = quit_wrapper(mainwin)
    exit_button = Button(text='Exit', command=quit_func)
    exit_button.grid(column=6, row=0)
    out_text = Text( mainwin)
    controller.out_text=out_text
    out_text.grid(column=0, row=5, columnspan=7)
    mainwin.mainloop()

if __name__ == "__main__":
    main(sys.argv)