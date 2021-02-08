from __future__ import division

from lab1.BasisMatricesHelper import get_basis_matrix, get_cannonical_form, get_basis_c_vector
from lab1.DualSimplexMethod import find_initial_basis_set
from sympy import zeros, Matrix
import bisect


class DualSimplexMethod(object):
    """
    :type matrix_c:Matrix
    :type matrix_A:Matrix
    :type matrix_b:Matrix
    :type eps:float
    """

    def __init__(self, matrix_c, matrix_A, matrix_b, eps, condition_operators=None):
        rows, cols = matrix_A.shape
        assert matrix_b.shape[0] == rows
        assert matrix_c.shape[0] == cols
        self.matrix_c = matrix_c[:, :]
        self._matrix_A = matrix_A[:, :]
        self.matrix_b = matrix_b[:, :]
        self.eps = eps
        self.m, self.n = matrix_A.shape
        if condition_operators is None:
            self.condition_operators = ["="] * self.m
        else:
            self.condition_operators = list(condition_operators)

    def solve(self, maximize, basis_indexes_set=None):
        """
        :type basis_indexes_set: list[int]
        :type not_basis_indexes_set: list[int]
        """
        if not maximize:
            self.matrix_c = -self.matrix_c
        if not basis_indexes_set:
            basis_indexes_set = find_initial_basis_set(self._matrix_A)
        if '<=' in self.condition_operators or '>=' in self.condition_operators:
            self._matrix_A, self.matrix_c, self.condition_operators = get_cannonical_form(self._matrix_A,
                                                                                          self.condition_operators,
                                                                                          self.matrix_c, maximize)
        self.m, self.n = self._matrix_A.shape
        basis_indexes_set.sort()
        not_basis_indexes_set = sorted(set(range(self.n)) - set(basis_indexes_set))
        return self.dual_simplex_algorithm(basis_indexes_set, not_basis_indexes_set)

    def dual_simplex_algorithm(self, basis_indexes_set, not_basis_indexes_set):
        """
        :type basis_indexes_set: list[int]
        :type not_basis_indexes_set: list[int]
        """
        inverse_basis_matrix = get_basis_matrix(self._matrix_A, basis_indexes_set).inv()
        while True:
            vector_u = get_basis_c_vector(self.matrix_c, basis_indexes_set).transpose() * inverse_basis_matrix
            vector_delta = zeros(len(not_basis_indexes_set), 1)
            for i, j in enumerate(not_basis_indexes_set):
                vector_delta[i, 0] = self.matrix_c[j, 0] - (vector_u * self._matrix_A[:, j])[0, 0]
            vector_kappa = inverse_basis_matrix * self.matrix_b
            j_k = -1
            for k, j in enumerate(basis_indexes_set):
                if vector_kappa[k, 0] < -self.eps:
                    j_k = j
                    break
            if j_k == -1:
                basis_plan = zeros(self.n, 1)
                for i, j in enumerate(basis_indexes_set):
                    basis_plan[j, 0] = vector_kappa[i, 0]
                return basis_plan, basis_indexes_set
            k = basis_indexes_set.index(j_k)
            vector_mu = zeros(len(not_basis_indexes_set), 1)
            vector_sigma = zeros(len(not_basis_indexes_set), 1)
            for i, j_nb in enumerate(not_basis_indexes_set):
                vector_mu[i, 0] = (inverse_basis_matrix[k, :] * self._matrix_A[:, j_nb])[0, 0]
            for i, j_nb in enumerate(not_basis_indexes_set):
                if vector_mu[i, 0] < -self.eps:
                    vector_sigma[i, 0] = vector_delta[i, 0] / vector_mu[i, 0]
                else:
                    vector_sigma[i, 0] = float("inf")
            j_0 = -1
            min_sigma = float("inf")
            for i, j_nb in enumerate(not_basis_indexes_set):
                if vector_sigma[i, 0] < min_sigma:
                    min_sigma = vector_sigma[i, 0]
                    j_0 = j_nb
            if j_0 == -1:
                raise Exception("Limitations of direct task are incompatible")
            basis_indexes_set.remove(j_k)
            bisect.insort_left(basis_indexes_set, j_0)
            not_basis_indexes_set.remove(j_0)
            bisect.insort_left(not_basis_indexes_set, j_k)
            inverse_basis_matrix = get_basis_matrix(self._matrix_A, basis_indexes_set).inv()
