from __future__ import division
import itertools
from sympy.matrices.dense import zeros, MutableDenseMatrix
from BasisMatricesHelper import *
from MatricesHelper import *
import bisect


class DualSimplexMethod(object):
    def __init__(self, A_matrix, b_matrix, c_matrix, d_lower, d_upper, eps=0.000001):
        """
        :type A_matrix:MutableDenseMatrix
        :type b_matrix:MutableDenseMatrix
        :type c_matrix:MutableDenseMatrix
        :type d_lower:MutableDenseMatrix
        :type d_upper:MutableDenseMatrix
        """
        rows, cols=A_matrix.shape
        assert b_matrix.shape[0]==rows
        assert c_matrix.shape[0]==cols
        assert d_lower.shape[0]==cols
        assert d_upper.shape[0]==cols
        self.A_matrix = A_matrix
        self.b_matrix = b_matrix
        self.c_matrix = c_matrix
        self.d_lower = d_lower
        self.d_upper = d_upper
        self.var_quantity = self.A_matrix.shape[1]
        self.eps=eps

    def solve(self, J_basis=None):
        """
        :type J_basis:list
        """
        if J_basis is None:
            J_basis=find_initial_basis_set(self.A_matrix)
        J_not_basis = sorted(set(range(self.var_quantity)) - set(J_basis))
        c_basis = get_basis_c_vector(self.c_matrix, J_basis)
        basis_matrix = get_basis_matrix(self.A_matrix, J_basis)
        inv_basis_matrix = get_inverse_matrix(basis_matrix)
        vector_y = c_basis.transpose() * inv_basis_matrix
        vector_delta = zeros(self.var_quantity, 1)
        for j in xrange(self.var_quantity):
            vector_delta[j, 0] = (vector_y * self.A_matrix[:, j])[0, 0] - self.c_matrix[j, 0]
        J_not_basis_min = []
        J_not_basis_plus = []
        for j in J_not_basis:
            if vector_delta[j, 0] >= 0:
                J_not_basis_plus.append(j)
            else:
                J_not_basis_min.append(j)
        while True:
            vector_aleph = zeros(self.var_quantity, 1)
            for j in J_not_basis_plus:
                vector_aleph[j, 0] = self.d_lower[j, 0]
            for j in J_not_basis_min:
                vector_aleph[j, 0] = self.d_upper[j, 0]
            A_aleph_sum = zeros(*self.b_matrix.shape)
            for j in J_not_basis:
                A_aleph_sum += self.A_matrix[:, j] * vector_aleph[j, 0]
            aleph_basis = inv_basis_matrix * (self.b_matrix - A_aleph_sum)
            for i, j in enumerate(J_basis):
                vector_aleph[j, 0] = aleph_basis[i, 0]
            j_k = 0
            for j in J_basis:
                if self.d_lower[j, 0] - vector_aleph[j, 0]>self.eps or vector_aleph[j, 0] - self.d_upper[j, 0]>self.eps:
                    j_k = j
                    break
            else:
                return vector_aleph, sorted(J_basis)
            mu_j_k = 0
            k_index = J_basis.index(j_k)
            if self.d_lower[j_k, 0] > vector_aleph[j_k, 0]:
                mu_j_k = 1
            else:
                mu_j_k = -1
            delta_y = mu_j_k * inv_basis_matrix[k_index, :]
            vector_mu = zeros(len(J_not_basis), 1)
            for i, j in enumerate(J_not_basis):
                vector_mu[i, 0] = delta_y * self.A_matrix[:, j]
            vector_sigma = zeros(len(J_not_basis), 1)
            for i, j in enumerate(J_not_basis):
                if (j in J_not_basis_plus and vector_mu[i, 0] < 0) or (j in J_not_basis_min and vector_mu[i, 0] > 0):
                    vector_sigma[i, 0] = -vector_delta[j, 0] / vector_mu[i, 0]
                else:
                    vector_sigma[i, 0] = float("inf")
            sigma_0 = float("inf")
            j_asterisk = -1
            for i, j in enumerate(J_not_basis):
                if vector_sigma[i, 0] < sigma_0:
                    sigma_0 = vector_sigma[i, 0]
                    j_asterisk = j
            if j_asterisk == -1:
                raise Exception("No plans can be found")
            for i, j in enumerate(J_not_basis):
                vector_delta[j, 0] += sigma_0 * vector_mu[i, 0]
            vector_delta[j_k, 0] += sigma_0 * mu_j_k
            for j in set(J_basis) - set([j_k]):
                vector_delta[j, 0] = 0
            J_basis[k_index] = j_asterisk
            inv_basis_matrix = get_matrix_B_with_wave(self.A_matrix[:, j_asterisk], inv_basis_matrix, k_index)
            basis_matrix = get_basis_matrix(self.A_matrix, J_basis)
            J_not_basis.remove(j_asterisk)
            bisect.insort_left(J_not_basis, j_k)
            if j_asterisk in J_not_basis_plus:
                if mu_j_k == 1:
                    J_not_basis_plus.remove(j_asterisk)
                    bisect.insort_left(J_not_basis_plus, j_k)
                else:
                    J_not_basis_plus.remove(j_asterisk)
            else:
                if mu_j_k == 1:
                    bisect.insort_left(J_not_basis_plus, j_k)
            J_not_basis_min = sorted(set(J_not_basis) - set(J_not_basis_plus))

def find_initial_basis_set(A_matrix):
    """
    :rtype A_matrix:MutableDenseMatrix
    """
    rows, cols=A_matrix.shape
    comb=itertools.combinations(range(cols),rows)
    for c in comb:
        a=get_basis_matrix(A_matrix, c)
        if a.det()!=0:
            return list(c)
