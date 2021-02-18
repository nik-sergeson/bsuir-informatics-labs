import math
from sympy import Matrix, eye, Symbol


class Solver:
    def __init__(self, precision):
        self.precision = precision

    def gauss(self, matrix_A, matrix_b):
        extended_matrix = matrix_A.col_insert(matrix_A.shape[1], matrix_b)
        rank_A = matrix_A.rank()
        if rank_A == extended_matrix.rank():
            row_count, col_count = matrix_A.shape
            for i in range(row_count):
                if matrix_A[i, i] == 0:
                    raise ValueError("Zero main element")
                for j in range(i + 1, row_count):
                    factor = 1.0 * matrix_A[j, i] / matrix_A[i, i]
                    matrix_A[j, i:] -= factor * matrix_A[i, i:]
                    matrix_b[j, 0] -= matrix_b[i, 0] * factor
            matrix_A_transformed = Matrix(matrix_A)
            for i in range(matrix_A_transformed.shape[0]):
                for j in range(matrix_A_transformed.shape[1]):
                    matrix_A_transformed[i, j] = round(matrix_A_transformed[i, j], self.precision)
            if rank_A == col_count:
                solutions = Matrix([0] * col_count)
                for i in reversed(range(col_count)):
                    tempsumm = 0
                    for j in range(i + 1, col_count):
                        tempsumm += matrix_A[i, j] * solutions[j, 0]
                    solutions[i, 0] = (1.0 * matrix_b[i, 0] - tempsumm) / matrix_A[i, i]
                for i in range(solutions.shape[0]):
                    solutions[i, 0] = round(solutions[i, 0], self.precision)
            else:
                solutions = Matrix([[0] * (col_count - rank_A + 1)] * col_count)
                for i in range(row_count, col_count):
                    solutions[i, i - row_count] = 1
                factor = matrix_A[row_count - 1, row_count - 1] * 1.0
                solutions[row_count - 1, 0:] = [
                    [(-x) / factor for x in matrix_A[row_count - 1, row_count:]] + [matrix_b[row_count - 1] / factor]]
                for i in reversed(range(row_count - 1)):
                    factor = matrix_A[i, i] * 1.0
                    variable_vector = Matrix(
                        [[(-x) / factor for x in matrix_A[i, row_count:]] + [matrix_b[i] / factor]])
                    for j in range(i + 1, row_count):
                        variable_vector += (-matrix_A[i, j] / factor) * solutions[j, 0:]
                    solutions[i, 0:] = variable_vector
                symbolic_vars = []
                for i in range(solutions.shape[1] - 1):
                    symbolic_vars.append(Symbol('C' + str(i)))
                symbolic_solutions = Matrix([[0]] * solutions.shape[0])
                for i in range(solutions.shape[0]):
                    for j in range(solutions.shape[1]):
                        solutions[i, j] = round(solutions[i, j], self.precision)
                    for k in range(solutions.shape[1] - 1):
                        symbolic_solutions[i, 0] += symbolic_vars[k] * solutions[i, k]
                    symbolic_solutions[i, 0] += solutions[i, solutions.shape[1] - 1]
                solutions = symbolic_solutions
            return (matrix_A_transformed, solutions)
        else:
            raise ValueError("No solution")

    def gauss_selection(self, matrix_A, matrix_b):
        extended_matrix = matrix_A.col_insert(matrix_A.shape[1], matrix_b)
        rank_A = matrix_A.rank()
        if rank_A == extended_matrix.rank():
            row_count, col_count = matrix_A.shape
            for i in range(row_count):
                max_row_index = i
                for k in range(i + 1, row_count):
                    if math.fabs(matrix_A[k, i]) > math.fabs(matrix_A[max_row_index, i]):
                        max_row_index = k
                matrix_A[max_row_index, 0:], matrix_A[i, 0:] = matrix_A[i, 0:], matrix_A[max_row_index, 0:]
                matrix_b[max_row_index, 0], matrix_b[i, 0] = matrix_b[i, 0], matrix_b[max_row_index, 0]
                for j in range(i + 1, row_count):
                    factor = 1.0 * matrix_A[j, i] / matrix_A[i, i]
                    matrix_A[j, i:] -= factor * matrix_A[i, i:]
                    matrix_b[j, 0] -= matrix_b[i, 0] * factor
            matrix_A_transformed = Matrix(matrix_A)
            for i in range(matrix_A_transformed.shape[0]):
                for j in range(matrix_A_transformed.shape[1]):
                    matrix_A_transformed[i, j] = round(matrix_A_transformed[i, j], self.precision)
            if rank_A == col_count:
                solutions = Matrix([0] * col_count)
                for i in reversed(range(col_count)):
                    tempsumm = 0
                    for j in range(i + 1, col_count):
                        tempsumm += matrix_A[i, j] * solutions[j, 0]
                    solutions[i, 0] = (1.0 * matrix_b[i, 0] - tempsumm) / matrix_A[i, i]
                    for i in range(solutions.shape[0]):
                        solutions[i, 0] = round(solutions[i, 0], self.precision)
            else:
                solutions = Matrix([[0] * (col_count - rank_A + 1)] * col_count)
                for i in range(row_count, col_count):
                    solutions[i, i - row_count] = 1
                factor = matrix_A[row_count - 1, row_count - 1] * 1.0
                solutions[row_count - 1, 0:] = [
                    [(-x) / factor for x in matrix_A[row_count - 1, row_count:]] + [matrix_b[row_count - 1] / factor]]
                for i in reversed(range(row_count - 1)):
                    factor = matrix_A[i, i] * 1.0
                    variable_vector = Matrix(
                        [[(-x) / factor for x in matrix_A[i, row_count:]] + [matrix_b[i] / factor]])
                    for j in range(i + 1, row_count):
                        variable_vector += (-matrix_A[i, j] / factor) * solutions[j, 0:]
                    solutions[i, 0:] = variable_vector
                symbolic_vars = []
                for i in range(solutions.shape[1] - 1):
                    symbolic_vars.append(Symbol('C' + str(i)))
                symbolic_solutions = Matrix([[0]] * solutions.shape[0])
                for i in range(solutions.shape[0]):
                    for j in range(solutions.shape[1]):
                        solutions[i, j] = round(solutions[i, j], self.precision)
                    for k in range(solutions.shape[1] - 1):
                        symbolic_solutions[i, 0] += symbolic_vars[k] * solutions[i, k]
                    symbolic_solutions[i, 0] += solutions[i, solutions.shape[1] - 1]
                solutions = symbolic_solutions
            return (matrix_A_transformed, solutions)
        else:
            raise ValueError("No solution")

    def jordan(self, matrix_A, matrix_b):
        extended_matrix = matrix_A.col_insert(matrix_A.shape[1], matrix_b)
        rank_A = matrix_A.rank()
        if rank_A == extended_matrix.rank():
            row_count, col_count = matrix_A.shape
            for i in range(row_count):
                max_row_index = i
                for k in range(i + 1, row_count):
                    if math.fabs(matrix_A[k, i]) > math.fabs(matrix_A[max_row_index, i]):
                        max_row_index = k
                matrix_A[max_row_index, 0:], matrix_A[i, 0:] = matrix_A[i, 0:], matrix_A[max_row_index, 0:]
                matrix_b[max_row_index, 0], matrix_b[i, 0] = matrix_b[i, 0], matrix_b[max_row_index, 0]
                factor = 1.0 * matrix_A[i, i]
                matrix_A[i, i:] /= factor
                matrix_b[i, 0] /= factor
                for j in range(i + 1, row_count):
                    factor = matrix_A[j, i]
                    matrix_A[j, i:] -= matrix_A[i, i:] * factor
                    matrix_b[j, 0] -= matrix_b[i, 0] * factor
            matrix_A_transformed = Matrix(matrix_A)
            for i in range(matrix_A_transformed.shape[0]):
                for j in range(matrix_A_transformed.shape[1]):
                    matrix_A_transformed[i, j] = round(matrix_A_transformed[i, j], self.precision)
            for i in reversed(range(1, row_count)):
                for j in reversed(range(i)):
                    factor = matrix_A[j, i]
                    matrix_A[j, i:] -= matrix_A[i, i:] * factor
                    matrix_b[j, 0] -= matrix_b[i, 0] * factor
            solutions = Matrix([[0] * (col_count - rank_A + 1)] * col_count)
            for i in range(row_count):
                for j in range(rank_A, col_count):
                    solutions[i, j - rank_A] = round(matrix_A[i, j], self.precision)
                solutions[i, col_count - rank_A] = round(matrix_b[i, 0], self.precision)
            for i in range(row_count, col_count):
                solutions[i, i - row_count] = 1
            symbolic_vars = []
            for i in range(solutions.shape[1] - 1):
                symbolic_vars.append(Symbol('C' + str(i)))
            symbolic_solutions = Matrix([[0]] * solutions.shape[0])
            for i in range(solutions.shape[0]):
                for k in range(solutions.shape[1] - 1):
                    symbolic_solutions[i, 0] += symbolic_vars[k] * solutions[i, k]
                symbolic_solutions[i, 0] += solutions[i, solutions.shape[1] - 1]
            solutions = symbolic_solutions
            return (matrix_A_transformed, solutions)
        else:
            raise ValueError("No solution")

    def gauss_determinant(self, matrix, round_result=True):
        row_count, col_count = matrix.shape
        if row_count != col_count:
            raise ValueError("Dimensions don't match")
        for i in range(row_count):
            for j in range(i + 1, row_count):
                factor = 1.0 * matrix[j, i] / matrix[i, i]
                matrix[j, i:] -= factor * matrix[i, i:]
        determinant = 1
        for i in range(row_count):
            determinant *= matrix[i, i]
        if round_result:
            return round(determinant, self.precision)
        else:
            return determinant

    def reverse_matrix(self, matrix, round_result=True):
        row_count, col_count = matrix.shape
        identity_matrix = eye(row_count)
        if row_count == col_count and self.gauss_determinant(matrix.copy(), round_result) != 0:
            for i in range(row_count):
                max_row_index = i
                for k in range(i + 1, row_count):
                    if math.fabs(matrix[k, i]) > math.fabs(matrix[max_row_index, i]):
                        max_row_index = k
                matrix[max_row_index, 0:], matrix[i, 0:] = matrix[i, 0:], matrix[max_row_index, 0:]
                identity_matrix[max_row_index, 0:], identity_matrix[i, 0:] = identity_matrix[i, 0:], identity_matrix[
                                                                                                     max_row_index, 0:]
                factor = matrix[i, i]
                matrix[i, i:] /= factor
                identity_matrix[i, 0:] /= factor
                for j in range(i + 1, row_count):
                    factor = matrix[j, i]
                    matrix[j, i:] -= matrix[i, i:] * factor
                    identity_matrix[j, 0:] -= identity_matrix[i, 0:] * factor
            for i in reversed(range(1, row_count)):
                for k in reversed(range(i)):
                    factor = matrix[k, i]
                    matrix[k, i] -= matrix[i, i] * factor
                    identity_matrix[k, 0:] -= identity_matrix[i, 0:] * factor
            if round_result:
                for i in range(row_count):
                    for j in range(col_count):
                        identity_matrix[i, j] = round(identity_matrix[i, j], self.precision)
            return identity_matrix
        else:
            raise ValueError("Can't find reverse matrix")

    def solve_matrix_method(self, matrix_A, matrix_b):
        reverse_matrix = self.reverse_matrix(matrix_A.copy(), False)
        solutions = reverse_matrix * matrix_b
        for i in range(solutions.shape[0]):
            for j in range(solutions.shape[1]):
                solutions[i, j] = round(solutions[i, j], self.precision)
        return solutions
