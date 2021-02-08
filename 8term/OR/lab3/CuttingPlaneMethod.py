from __future__ import division

import bisect
from lab1.BasisMatricesHelper import get_basis_matrix, get_basis_c_vector
from math import floor
from sympy.matrices import Matrix, zeros
from SimplexMethod import SimplexMethod
from DualSimplexMethod import DualSimplexMethod


class CuttingPlaneMethod(object):
    """
    :rtype A_matrix:MutableDenseMatrix
    """

    def __init__(self, A_matrix, b_matrix, c_matrix, condition_operators=None, eps=0.000001):
        rows, cols = A_matrix.shape
        assert b_matrix.shape[0] == rows
        assert c_matrix.shape[0] == cols
        self.A_matrix = A_matrix
        self.b_matrix = b_matrix
        self.c_matrix = c_matrix
        if condition_operators is None:
            self.condition_operators = ["="] * self.b_matrix.shape[0]
        else:
            self.condition_operators = condition_operators
        self.eps = eps
        self.var_quantity = self.A_matrix.shape[1]

    def solve(self, maximize):
        J_synt = []
        J_synt_limitations = {}
        solver = SimplexMethod(self.c_matrix, self.A_matrix, self.b_matrix, self.eps, self.condition_operators)
        plan, J_basis = solver.solve(maximize)
        self.A_matrix, self.b_matrix, self.c_matrix = solver._matrix_A, solver.matrix_b, solver.matrix_c
        if not maximize:
            maximize = True
        while True:
            J_not_basis = sorted(set(range(plan.shape[0])) - set(J_basis))
            j_0 = -1
            for i in J_basis:
                if abs(plan[i, 0] - round(plan[i, 0])) > self.eps:
                    j_0 = i
                    break
            if j_0 == -1:
                return plan[:self.var_quantity, :]
            k = J_basis.index(j_0)
            inverse_basis_matrix = get_basis_matrix(self.A_matrix, J_basis).inv()
            vector_a = zeros(self.A_matrix.shape[1], 1)
            for j in J_not_basis:
                a_j = (inverse_basis_matrix * self.A_matrix[:, j])[k, 0]
                vector_a[j, 0] = a_j - floor(a_j)
            beta = Matrix([plan[j_0, 0] - floor(plan[j_0, 0])])
            A_matrix = zeros(self.A_matrix.shape[0] + 1, self.A_matrix.shape[1] + 1)
            A_matrix[:-1, :-1] = self.A_matrix[:, :]
            A_matrix[-1, :-1] = vector_a.transpose()
            A_matrix[-1, -1] = -1
            self.A_matrix = A_matrix
            self.b_matrix = self.b_matrix.row_insert(self.b_matrix.shape[0], beta)
            self.c_matrix = self.c_matrix.row_insert(self.c_matrix.shape[0], zeros(1, 1))
            self.condition_operators.append('=')
            new_var = self.A_matrix.shape[1] - 1
            J_synt_limitations[new_var] = self.A_matrix.shape[0] - 1
            bisect.insort_left(J_synt, new_var)
            bisect.insort_left(J_basis, new_var)
            inverse_basis_matrix = get_basis_matrix(self.A_matrix, J_basis).inv()
            solver = DualSimplexMethod(self.c_matrix, self.A_matrix, self.b_matrix, self.eps, self.condition_operators)
            plan, J_basis = solver.solve(maximize, J_basis)