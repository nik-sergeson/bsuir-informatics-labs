__author__ = 'nik-u'

from MatrixUI import MatrixUI
from Tkinter import *
from sympy import Matrix
from Solver import Solver
import tkMessageBox


class Controller:
    rowspan_enrty = None
    colspan_entry = None
    precision_entry = None
    example = None
    top_row = 3
    top_col = 2
    mul_label = None
    equal_label = None
    matrix_A = None
    matrix_b = None
    matrix_X = None
    transformed_matrix_A = None
    solution_method = None
    mainwin = None
    matrix_info_label = None
    determinant_entry = None

    def resize_button_clicked(self):
        rowspan = int(self.rowspan_enrty.get())
        colspan = int(self.colspan_entry.get())
        self.transformed_matrix_A.clear()
        self.matrix_X.clear()
        self.matrix_A.resize(rowspan, colspan)
        self.matrix_X.resize(colspan, 1)
        self.matrix_b.resize(rowspan, 1)
        self.transformed_matrix_A.resize(rowspan, colspan)
        self.matrix_X.move(self.top_row, self.top_col + colspan + 1)
        self.mul_label.grid(column=self.top_col + colspan, row=self.top_row + rowspan / 2)
        self.equal_label.grid(column=self.top_col + colspan + 2, row=self.top_row + rowspan / 2)
        self.matrix_b.move(self.top_row, self.top_col + colspan + 3)
        self.transformed_matrix_A.move(self.top_row + rowspan + 1, self.top_col)
        self.determinant_entry.grid(column=self.top_col, row=self.top_row + rowspan)
        self.matrix_info_label.grid(column=self.top_col - 1, row=self.top_row + rowspan)
        self.method_selected()

    def example_selected(self):
        example_no = self.example.get()
        self.transformed_matrix_A.clear()
        self.matrix_X.clear()
        if self.solution_method.get() == 4:
            self.determinant_entry.configure(state='normal')
            self.determinant_entry.delete(0, END)
            self.determinant_entry.configure(state='readonly')
        if example_no == 1:
            self.colspan_entry.delete(0, END)
            self.colspan_entry.insert(0, 3)
            self.rowspan_enrty.delete(0, END)
            self.rowspan_enrty.insert(0, 3)
            self.resize_button_clicked()
            self.matrix_A.import_matrix(Matrix([[3, 2, -5], [2, -1, 3], [1, 2, -1]]))
            self.matrix_b.import_matrix(Matrix([-1, 13, 9]))
        elif example_no == 2:
            self.colspan_entry.delete(0, END)
            self.colspan_entry.insert(0, 3)
            self.rowspan_enrty.delete(0, END)
            self.rowspan_enrty.insert(0, 3)
            self.resize_button_clicked()
            self.matrix_A.import_matrix(Matrix([[4, 2, -1], [5, 3, -2], [3, 2, -3]]))
            self.matrix_b.import_matrix(Matrix([1, 2, 0]))
        elif example_no == 3:
            self.colspan_entry.delete(0, END)
            self.colspan_entry.insert(0, 3)
            self.rowspan_enrty.delete(0, END)
            self.rowspan_enrty.insert(0, 3)
            self.resize_button_clicked()
            self.matrix_A.import_matrix(Matrix([[8, 7, 3], [-7, -4, -4], [-6, 5, -4]]))
            self.matrix_b.import_matrix(Matrix([18, -11, -15]))
        elif example_no == 4:
            self.colspan_entry.delete(0, END)
            self.colspan_entry.insert(0, 4)
            self.rowspan_enrty.delete(0, END)
            self.rowspan_enrty.insert(0, 2)
            self.resize_button_clicked()
            self.matrix_A.import_matrix(Matrix([[1, 2, 3, 4], [1, -1, 1, -1]]))
            self.matrix_b.import_matrix(Matrix([5, 1]))
        elif example_no == 5:
            self.colspan_entry.delete(0, END)
            self.colspan_entry.insert(0, 3)
            self.rowspan_enrty.delete(0, END)
            self.rowspan_enrty.insert(0, 2)
            self.resize_button_clicked()
            self.matrix_A.import_matrix(Matrix([[1, -2, 4], [2, -3, 5]]))
            self.matrix_b.import_matrix(Matrix([0, 0]))

    def method_selected(self):
        self.transformed_matrix_A.clear()
        self.matrix_X.clear()
        if self.solution_method.get() in (1, 2, 3, 6):
            self.matrix_b.show()
            self.transformed_matrix_A.show()
            self.matrix_X.show()
            self.determinant_entry.grid_forget()
            self.matrix_info_label['text'] = 'Transformed:'
            self.equal_label.grid(column=self.matrix_A.col + self.matrix_A.columnspan + 2,
                                  row=self.matrix_A.row + self.matrix_A.rowspan / 2)
            self.mul_label.grid(column=self.matrix_A.col + self.matrix_A.columnspan,
                                row=self.matrix_A.row + self.matrix_A.rowspan / 2)
            if self.solution_method.get() == 6:
                self.transformed_matrix_A.hide()
                self.matrix_info_label.grid_forget()
            else:
                self.matrix_info_label.grid(column=self.top_col - 1, row=self.top_row + self.matrix_A.rowspan)
        else:
            self.matrix_b.hide()
            self.matrix_X.hide()
            self.equal_label.grid_forget()
            self.mul_label.grid_forget()
            self.matrix_info_label.grid(column=self.top_col - 1, row=self.top_row + self.matrix_A.rowspan)
            if self.solution_method.get() == 4:
                self.transformed_matrix_A.hide()
                self.matrix_info_label['text'] = 'Determinant=:'
                self.determinant_entry.configure(state='normal')
                self.determinant_entry.delete(0, END)
                self.determinant_entry.configure(state='readonly')
                self.determinant_entry.grid(column=self.top_col, row=self.top_row + self.matrix_A.columnspan)
            else:
                self.transformed_matrix_A.show()
                self.matrix_info_label['text'] = 'Transformed:'
                self.determinant_entry.grid_forget()

    def solve_button_clicked(self):
        solver = Solver(int(self.precision_entry.get()))
        self.transformed_matrix_A.precision = int(self.precision_entry.get())
        self.matrix_X.precision = int(self.precision_entry.get())
        try:
            if self.solution_method.get() == 1:
                transformed_A, solutions = solver.gauss(self.matrix_A.export_matrix(), self.matrix_b.export_matrix())
                self.matrix_X.import_matrix(solutions)
                self.transformed_matrix_A.import_matrix(transformed_A)
            elif self.solution_method.get() == 2:
                transformed_A, solutions = solver.gauss_selection(self.matrix_A.export_matrix(),
                                                                  self.matrix_b.export_matrix())
                self.matrix_X.import_matrix(solutions)
                self.transformed_matrix_A.import_matrix(transformed_A)
            elif self.solution_method.get() == 3:
                transformed_A, solutions = solver.jordan(self.matrix_A.export_matrix(), self.matrix_b.export_matrix())
                self.matrix_X.import_matrix(solutions)
                self.transformed_matrix_A.import_matrix(transformed_A)
            elif self.solution_method.get() == 4:
                self.determinant_entry.configure(state='normal')
                self.determinant_entry.delete(0, END)
                self.determinant_entry.insert(0, '{0:.{1}f}'.format(
                    solver.gauss_determinant(self.matrix_A.export_matrix()), int(self.precision_entry.get())))
                self.determinant_entry.configure(state='readonly')
            elif self.solution_method.get() == 5:
                transformed_A = solver.reverse_matrix(self.matrix_A.export_matrix())
                self.transformed_matrix_A.import_matrix(transformed_A)
            elif self.solution_method.get() == 6:
                solutions = solver.solve_matrix_method(self.matrix_A.export_matrix(), self.matrix_b.export_matrix())
                self.matrix_X.import_matrix(solutions)
        except ValueError as ve:
            tkMessageBox.showerror(title="error", message=ve.message, parent=self.mainwin)


def main():
    mainwin = Tk()
    mainwin.minsize(800, 400)
    controller = Controller()
    controller.mainwin = mainwin
    matrix_A = MatrixUI(mainwin, 3, 2, 3, 3, 0, 'normal')
    controller.matrix_A = matrix_A
    matrix_x = MatrixUI(mainwin, 3, 7, 3, 1, 2, 'readonly')
    controller.matrix_X = matrix_x
    matrix_b = MatrixUI(mainwin, 3, 9, 3, 1, 0, 'normal')
    controller.matrix_b = matrix_b
    transformed_matrix_A = MatrixUI(mainwin, 6, 2, 3, 3, 2, 'readonly')
    controller.transformed_matrix_A = transformed_matrix_A
    rowspan_entry = Entry(mainwin, width=6)
    rowspan_entry.insert(0, 3)
    rowspan_entry.grid(column=1, row=0)
    rowspan_label = Label(mainwin, text='Rows')
    rowspan_label.grid(column=0, row=0)
    controller.rowspan_enrty = rowspan_entry
    colspan_entry = Entry(mainwin, width=6)
    colspan_entry.insert(0, 3)
    colspan_entry.grid(column=1, row=1)
    colspan_label = Label(mainwin, text='Cols')
    colspan_label.grid(column=0, row=1)
    controller.colspan_entry = colspan_entry
    precision_entry = Entry(mainwin, width=6)
    precision_entry.insert(0, 2)
    precision_entry.grid(column=1, row=2)
    precision_label = Label(mainwin, text='Precision')
    precision_label.grid(column=0, row=2)
    controller.precision_entry = precision_entry
    multiply_label = Label(mainwin, text='*')
    multiply_label.grid(column=6, row=4)
    controller.mul_label = multiply_label
    equal_label = Label(mainwin, text='=')
    equal_label.grid(column=8, row=4)
    matrix_type_label = Label(mainwin, text='Transformed:')
    controller.matrix_info_label = matrix_type_label
    controller.equal_label = equal_label
    determinant_entry = Entry(mainwin, width=6)
    determinant_entry.configure(state='readonly')
    controller.determinant_entry = determinant_entry
    resize_button = Button(text='Resize', command=controller.resize_button_clicked)
    resize_button.grid(column=0, row=14)
    solve_button = Button(text='Solve', command=controller.solve_button_clicked)
    solve_button.grid(column=1, row=14)
    example = IntVar()
    example_rbutton1 = Radiobutton(mainwin, text="Example no 1", variable=example, value=1,
                                   command=controller.example_selected)
    example_rbutton2 = Radiobutton(mainwin, text="Example no 2", variable=example, value=2,
                                   command=controller.example_selected)
    example_rbutton3 = Radiobutton(mainwin, text="Example no 3", variable=example, value=3,
                                   command=controller.example_selected)
    example_rbutton4 = Radiobutton(mainwin, text="Example no 4", variable=example, value=4,
                                   command=controller.example_selected)
    example_rbutton5 = Radiobutton(mainwin, text="Example no 5", variable=example, value=5,
                                   command=controller.example_selected)
    example_rbutton1.grid(row=3, column=0, sticky=W)
    example_rbutton2.grid(row=4, column=0, sticky=W)
    example_rbutton3.grid(row=5, column=0, sticky=W)
    example_rbutton4.grid(row=6, column=0, sticky=W)
    example_rbutton5.grid(row=7, column=0, sticky=W)
    example.set(1)
    solution_method = IntVar()
    method_rbutton1 = Radiobutton(mainwin, text="Gauss", variable=solution_method, value=1,
                                  command=controller.method_selected)
    method_rbutton2 = Radiobutton(mainwin, text="Gauss(with selection)", variable=solution_method, value=2,
                                  command=controller.method_selected)
    method_rbutton3 = Radiobutton(mainwin, text="Jordan-Gauss", variable=solution_method, value=3,
                                  command=controller.method_selected)
    method_rbutton4 = Radiobutton(mainwin, text="Determinant", variable=solution_method, value=4,
                                  command=controller.method_selected)
    method_rbutton5 = Radiobutton(mainwin, text="Reverse matrix", variable=solution_method, value=5,
                                  command=controller.method_selected)
    method_rbutton6 = Radiobutton(mainwin, text="Matrix method", variable=solution_method, value=6,
                                  command=controller.method_selected)
    method_rbutton1.grid(row=8, column=0, sticky=W)
    method_rbutton2.grid(row=9, column=0, sticky=W)
    method_rbutton3.grid(row=10, column=0, sticky=W)
    method_rbutton4.grid(row=11, column=0, sticky=W)
    method_rbutton5.grid(row=12, column=0, sticky=W)
    method_rbutton6.grid(row=13, column=0, sticky=W)
    solution_method.set(1)
    controller.example = example
    controller.solution_method = solution_method
    controller.example_selected()
    mainwin.mainloop()

if __name__ == "__main__":
    main()
