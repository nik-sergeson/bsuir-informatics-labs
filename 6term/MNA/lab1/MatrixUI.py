from Tkinter import *
from sympy import Matrix
from sympy.core.numbers import Integer, Float
from sympy.core.symbol import Symbol


class MatrixUI:
    mainwin = None
    columnspan = 0
    rowspan = 0
    row = 0
    col = 0
    cell_width = 6
    cells = None
    precision = 0
    state = 'normal'
    cleared = True

    def __init__(self, mainwin, row, col, rowspan, columnspan, precision=0, state=None):
        self.mainwin = mainwin
        self.col = col
        self.row = row
        self.rowspan = rowspan
        self.columnspan = columnspan
        self.cells = []
        self.precision = precision
        if state is not None:
            self.state = state
        for i in range(rowspan):
            self.cells.append([])
            for j in range(columnspan):
                self.cells[i].append(Entry(mainwin, width=self.cell_width))
                self.cells[i][j].configure(state=self.state)
                self.cells[i][j].grid(column=col + j, row=row + i, columnspan=1, rowspan=1)

    def resize(self, rowspan, columnspan):
        if columnspan > self.columnspan:
            for i in range(min(self.rowspan, rowspan)):
                for j in range(self.columnspan, columnspan):
                    self.cells[i].append(Entry(self.mainwin, width=self.cell_width))
                    self.cells[i][j].configure(state=self.state)
                    self.cells[i][j].grid(column=self.col + j, row=self.row + i)
        elif columnspan < self.columnspan:
            for i in range(min(self.rowspan, rowspan)):
                for j in range(columnspan, self.columnspan):
                    self.cells[i][j].destroy()
                del self.cells[i][columnspan:]
        if rowspan > self.rowspan:
            for i in range(self.rowspan, rowspan):
                self.cells.append([])
                for j in range(columnspan):
                    self.cells[i].append(Entry(self.mainwin, width=self.cell_width))
                    self.cells[i][j].configure(state=self.state)
                    self.cells[i][j].grid(column=self.col + j, row=self.row + i)
        elif rowspan < self.rowspan:
            for i in range(rowspan, self.rowspan):
                for j in range(self.columnspan):
                    self.cells[i][j].destroy()
            del self.cells[rowspan:]
        self.columnspan = columnspan
        self.rowspan = rowspan

    def move(self, row, col):
        for i in range(self.rowspan):
            for j in range(self.columnspan):
                self.cells[i][j].grid(column=col + j, row=row + i)
        self.row = row
        self.col = col

    def export_matrix(self):
        res_matrix = []
        for i in range(len(self.cells)):
            res_matrix.append([float(x.get()) for x in self.cells[i]])
        return Matrix(res_matrix)

    def import_matrix(self, matrix):
        self.cleared = False
        row_count, col_count = matrix.shape
        if row_count != self.rowspan or col_count != self.columnspan:
            self.resize(col_count, row_count)
        for i in range(row_count):
            for j in range(col_count):
                self.cells[i][j].configure(state='normal')
                self.cells[i][j].delete(0, END)
                element_str = ''
                if isinstance(matrix[i, j], Integer) or isinstance(matrix[i, j], Float):
                    element_str = '{0:.{1}f}'.format(float(matrix[i, j]), self.precision)
                elif isinstance(matrix[i, j], Symbol):
                    element_str = str(matrix[i, j])
                else:
                    summands = matrix[i, j].args
                    last_number = False
                    for summand in summands:
                        if isinstance(summand, Float) or isinstance(summand, Integer):
                            num = summand
                            if num > 0 and len(element_str) > 0:
                                element_str += '+'
                            element_str += '{0:.{1}f}'.format(summand, self.precision)
                            last_number = True
                        elif isinstance(summand, Symbol):
                            if len(element_str) > 0:
                                if not last_number:
                                    element_str += '+'
                                else:
                                    element_str += '*'
                            element_str += str(summand)
                            last_number = False
                        else:
                            num, var = summand.args
                            if num > 0 and len(element_str) > 0:
                                element_str += '+'
                            element_str += '{0:.{1}f}*{2}'.format(num, self.precision, var)
                            last_number = False
                self.cells[i][j].insert(0, element_str)
                self.cells[i][j].configure(state=self.state)

    def hide(self):
        for i in range(self.rowspan):
            for j in range(self.columnspan):
                self.cells[i][j].grid_forget()

    def show(self):
        for i in range(self.rowspan):
            for j in range(self.columnspan):
                self.cells[i][j].grid(column=self.col + j, row=self.row + i)

    def clear(self):
        if not self.cleared:
            for i in range(self.rowspan):
                for j in range(self.columnspan):
                    self.cells[i][j].configure(state='normal')
                    self.cells[i][j].delete(0, END)
                    self.cells[i][j].configure(state=self.state)
            self.cleared = True
