from __future__ import division

from ..lab1.Solver import Solver
from ..lab2.SimplexMethod import get_basis_matrix, get_cannonical_form, get_basis_cost_vector
from sympy import zeros, Matrix
from sympy.functions import transpose
import bisect


class DualSimplexMethod(object):
    """
    :type matrix_c:Matrix
    :type matrix_A:Matrix
    :type matrix_b:Matrix
    :type precision:float
    """

    def __init__(self, matrix_c, matrix_A, matrix_b, precision, condition_operators=None):
        self.matrix_c = matrix_c
        self._matrix_A = matrix_A
        self.matrix_b = matrix_b
        self.precision = precision
        self.m, self.n = matrix_A.shape
        if condition_operators is None:
            self.condition_operators = ["="] * self.m
        else:
            self.condition_operators = condition_operators
        self.solver = Solver(self.precision)

    def solve(self, basis_indexes_set, maximize, vector_y=None):
        """
        :type basis_indexes_set: list[int]
        :type not_basis_indexes_set: list[int]
        """
        self._matrix_A, self.matrix_c = get_cannonical_form(self._matrix_A, self.condition_operators, self.matrix_c, maximize)
        self.m, self.n=self._matrix_A.shape
        basis_indexes_set.sort()
        not_basis_indexes_set = sorted(set(range(self.n)) - set(basis_indexes_set))
        if vector_y is None:
            vector_y=transpose(get_basis_cost_vector(basis_indexes_set, self.matrix_c))*get_basis_matrix(basis_indexes_set, self._matrix_A).inv()
        vector_kaplan=zeros(self.m+self.n, 1)
        for j in not_basis_indexes_set:
            vector_kaplan[j, 0]=(vector_y*self._matrix_A[:, j])[0,0]-self.matrix_c[j, 0]
        return self.dual_simplex_algorithm(basis_indexes_set, not_basis_indexes_set, vector_kaplan)

    def dual_simplex_algorithm(self, basis_indexes_set, not_basis_indexes_set, vector_kaplan):
        """
        :type basis_indexes_set: list[int]
        :type not_basis_indexes_set: list[int]
        """
        basis_matrix = zeros(self.m, len(basis_indexes_set))
        for i, j in enumerate(basis_indexes_set):
            basis_matrix[:, i] = self._matrix_A[:, j]
        inverse_basis_matrix = basis_matrix.inv()
        while True:
            vector_kappa = inverse_basis_matrix * self.matrix_b
            for j in range(vector_kappa.shape[0]):
                if vector_kappa[j, 0] < 0:
                    break
            else:
                basis_plan = zeros(self.n, 1)
                for i, j in enumerate(basis_indexes_set):
                    basis_plan[j, 0] = vector_kappa[i, 0]
                return basis_plan, basis_indexes_set
            for k, j in enumerate(basis_indexes_set):
                if vector_kappa[k, 0] < 0:
                    vector_mu = zeros(self.n, 1)
                    vector_sigma = []
                    for j_nb in not_basis_indexes_set:
                        vector_mu[j_nb, 0] = inverse_basis_matrix[k, :] * self._matrix_A[:, j_nb]
                        if vector_mu[j_nb, 0] < 0:
                            vector_sigma.append(-vector_kaplan[j_nb, 0] / vector_mu[j_nb, 0])
                        else:
                            vector_sigma.append(None)
                    min_sigma_index = 0
                    min_sigma = vector_sigma[0]
                    for i, sigma in enumerate(vector_sigma):
                        if sigma is None:
                            continue
                        elif min_sigma is None or sigma < min_sigma:
                            min_sigma = sigma
                            min_sigma_index = i
                    if min_sigma is None:
                        raise Exception("Limitations of direct task are incompatible")
                    min_sigma_index = not_basis_indexes_set[min_sigma_index]
                    basis_indexes_set.pop(k)
                    bisect.insort_left(basis_indexes_set, min_sigma_index)
                    not_basis_indexes_set.remove(min_sigma_index)
                    bisect.insort_left(not_basis_indexes_set, j)
                    vector_kaplan[min_sigma_index, 0]=0
                    for j_nb in not_basis_indexes_set:
                        vector_kaplan[j_nb, 0]=vector_kaplan[j_nb, 0]+min_sigma*vector_mu[j_nb, 0]
                    vector_kaplan[j] = min_sigma
                    inverse_basis_matrix = get_basis_matrix(basis_indexes_set, self._matrix_A)
                    break
