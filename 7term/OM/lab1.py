from simplex_method.lab1.MatrixUI import MatrixUI
from Tkinter import *
from sympy import Matrix
from simplex_method.lab1.Solver import Solver
import tkMessageBox


class Controller:
    rowspan_enrty = None
    colspan_entry = None
    precision_entry = None
    row_no_entry = None
    top_row = 3
    top_col = 2
    matrix_B_label = None
    matrix_C = None
    vector_c_k_with_wave = None
    matrix_B = None
    matrix_B_with_wave = None
    matrix_C_label = None
    matrix_B_label = None
    vector_c_k_with_wave_label = None
    matrix_B_with_wave_label = None
    solution_method = None
    mainwin = None

    def resize_button_clicked(self):
        rowspan = int(self.rowspan_enrty.get())
        colspan = int(self.colspan_entry.get())
        self.matrix_B_with_wave.clear()
        self.matrix_B.clear()
        self.matrix_C.resize(rowspan, colspan)
        self.vector_c_k_with_wave.resize(rowspan, 1)
        self.matrix_B.resize(rowspan, colspan)
        self.matrix_B_with_wave.resize(rowspan, colspan)
        self.matrix_C_label.grid(column=self.top_col, row=self.top_row + rowspan / 2)
        self.matrix_B_label.grid(column=self.top_col + colspan + 1, row=self.top_row + rowspan / 2)
        self.matrix_B.move(self.top_row, self.top_col + colspan + 2)
        self.vector_c_k_with_wave_label.grid(column=self.top_col, row=self.top_row + rowspan + rowspan / 2)
        self.vector_c_k_with_wave.move(self.top_row + rowspan, self.top_col + 1)
        self.matrix_B_with_wave_label.grid(column=self.top_col + colspan + 1, row=self.top_row + rowspan + rowspan / 2)
        self.matrix_B_with_wave.move(self.top_row + rowspan, self.top_col + colspan + 2)
        self.method_selected()

    def method_selected(self):
        if self.solution_method.get() == 1:
            self.matrix_B_with_wave.clear()
            self.matrix_B.show()
            self.matrix_B_with_wave.show()
            self.vector_c_k_with_wave.show()
            self.matrix_B_with_wave_label.grid(column=self.top_col + self.matrix_C.columnspan + 1,
                                               row=self.matrix_C.row + self.matrix_C.rowspan + self.matrix_C.rowspan / 2)
            self.vector_c_k_with_wave_label.grid(column=self.top_col,
                                                 row=self.matrix_C.row + self.matrix_C.rowspan + self.matrix_C.rowspan / 2)
        elif self.solution_method.get() == 2:
            self.vector_c_k_with_wave.hide()
            self.matrix_B_with_wave.hide()
            self.vector_c_k_with_wave_label.grid_forget()
            self.matrix_B_with_wave_label.grid_forget()

    def solve_button_clicked(self):
        solver = Solver(int(self.precision_entry.get()))
        self.matrix_B_with_wave.precision = int(self.precision_entry.get())
        self.matrix_B.precision = int(self.precision_entry.get())
        try:
            if self.solution_method.get() == 1:
                matrix_c_k_with_wave = self.vector_c_k_with_wave.export_matrix()
                matrix_B = self.matrix_B.export_matrix()
                row_no = int(self.row_no_entry.get())
                matrix_B_with_wave = solver.get_matrix_B_with_wave(matrix_c_k_with_wave, matrix_B, row_no)
                self.matrix_B_with_wave.import_matrix(matrix_B_with_wave)
            elif self.solution_method.get() == 2:
                matrix_C = self.matrix_C.export_matrix()
                matrix_B = solver.get_inverse_matrix(matrix_C)
                self.matrix_B.import_matrix(matrix_B)
        except ArithmeticError as ae:
            tkMessageBox.showerror(title="error", message=ae.message, parent=self.mainwin)


def main():
    mainwin = Tk()
    mainwin.minsize(800, 400)
    controller = Controller()
    controller.mainwin = mainwin
    matrix_C = MatrixUI(mainwin, 3, 3, 3, 3, 0, 'normal')
    matrix_C.import_matrix(Matrix([[0, 2, 1], [0, 1, 1], [1, 1, 1]]))
    controller.matrix_C = matrix_C
    matrix_C_label = Label(mainwin, text='C=')
    matrix_C_label.grid(column=2, row=4)
    controller.matrix_C_label = matrix_C_label
    matrix_B = MatrixUI(mainwin, 3, 7, 3, 3, 0, 'normal')
    controller.matrix_B = matrix_B
    matrix_B_label = Label(mainwin, text='B=')
    matrix_B_label.grid(column=6, row=4)
    controller.matrix_B_label = matrix_B_label
    vector_c_k_with_wave = MatrixUI(mainwin, 6, 3, 3, 1, 0, 'normal')
    controller.vector_c_k_with_wave = vector_c_k_with_wave
    vector_c_k_with_wave_label = Label(mainwin, text='c_k_with_wave=')
    vector_c_k_with_wave_label.grid(column=2, row=7)
    controller.vector_c_k_with_wave_label = vector_c_k_with_wave_label
    matrix_B_with_wave = MatrixUI(mainwin, 6, 7, 3, 3, 0, 'normal')
    controller.matrix_B_with_wave = matrix_B_with_wave
    matrix_B_with_wave_label = Label(mainwin, text='B_with_wave=')
    matrix_B_with_wave_label.grid(column=6, row=7)
    controller.matrix_B_with_wave_label = matrix_B_with_wave_label
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
    row_no_entry = Entry(mainwin, width=6)
    row_no_entry.insert(0, 2)
    row_no_entry.grid(column=1, row=3)
    row_no_label = Label(mainwin, text='Row no.')
    row_no_label.grid(column=0, row=3)
    controller.row_no_entry = row_no_entry
    solution_method = IntVar()
    method_rbutton1 = Radiobutton(mainwin, text="Find B with wave", variable=solution_method, value=1,
                                  command=controller.method_selected)
    method_rbutton2 = Radiobutton(mainwin, text="Find B", variable=solution_method, value=2,
                                  command=controller.method_selected)
    method_rbutton1.grid(row=4, column=0, sticky=W)
    method_rbutton2.grid(row=5, column=0, sticky=W)
    solution_method.set(1)
    controller.solution_method = solution_method
    controller.precision_entry = precision_entry
    resize_button = Button(text='Resize', command=controller.resize_button_clicked)
    resize_button.grid(column=0, row=6)
    solve_button = Button(text='Solve', command=controller.solve_button_clicked)
    solve_button.grid(column=1, row=6)
    mainwin.mainloop()


if __name__ == "__main__":
    main()
