from __future__ import division

from simplex_method.lab3.DualSimplexMethod import DualSimplexMethod
from sympy import Matrix

if __name__ == "__main__":
    matrix_c = Matrix([1, 1, 2])
    matrix_A = Matrix([[1, 1, 1], [1, -1, 0], [1, 1, 0]])
    matrix_b = Matrix([8, 4, 6])
    conditions_operators = ['<=', '=']
    basis_indexes_set = [0, 1, 2]
    dual_simplex = DualSimplexMethod(matrix_c, matrix_A, matrix_b, 0.01, conditions_operators)
    basis_plan, indexes_set = dual_simplex.solve(basis_indexes_set, False)
    assert basis_plan == Matrix([[5], [1], [2], [0]])
    matrix_c = Matrix([-19, 21, 0, 0])
    matrix_A = Matrix([[2, 5, -1, 0], [4, 1, 0, -1]])
    matrix_b = Matrix([20, 20])
    conditions_operators = ['=', '=']
    basis_indexes_set = [0, 1]
    dual_simplex = DualSimplexMethod(matrix_c, matrix_A, matrix_b, 0.01, conditions_operators)
    basis_plan, indexes_set = dual_simplex.solve(basis_indexes_set, True)
    assert basis_plan == Matrix([[40 / 9], [20 / 9], [0], [0]])
    matrix_c = Matrix([1, 1])
    matrix_A = Matrix([[1, -2], [2, -1]])
    matrix_b = Matrix([6, -2])
    conditions_operators = ['<=', '=']
    basis_indexes_set = [0, 1]
    dual_simplex = DualSimplexMethod(matrix_c, matrix_A, matrix_b, 0.01, conditions_operators)
    try:
        basis_plan, indexes_set = dual_simplex.solve(basis_indexes_set, True)
    except Exception as exc:
        print(exc)
    matrix_c = Matrix([1, 1, -2, -3])
    matrix_A = Matrix([[1, -1, 3, -2], [1, -5, 11, -6]])
    matrix_b = Matrix([1, 9])
    conditions_operators = ['=', '=']
    basis_indexes_set = [0, 1]
    dual_simplex = DualSimplexMethod(matrix_c, matrix_A, matrix_b, 0.01, conditions_operators)
    try:
        basis_plan, indexes_set = dual_simplex.solve(basis_indexes_set, True)
    except Exception as exc:
        print(exc)
