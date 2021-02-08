from __future__ import division
 
from sympy import zeros, eye
from sympy.matrices import Matrix
import bisect
 
 
class SimplexMethod:
    """
    :type matrix_c:Matrix
    :type matrix_A:Matrix
    :type matrix_b:Matrix
    :type eps:float
    """
 
    def __init__(self, matrix_c, matrix_A, matrix_b, eps, condition_operators=None):
        self.matrix_c = matrix_c[:,:]
        self._matrix_A = matrix_A[:,:]
        self.matrix_b = matrix_b[:,:]
        self.eps = eps
        self.m, self.n = matrix_A.shape
        if condition_operators is None:
            self.condition_operators = ["="] * self.m
        else:
            self.condition_operators = list(condition_operators)
 
    @property
    def matrix_A(self):
        return self._matrix_A
 
    @matrix_A.setter
    def matrix_A(self, matrix):
        self._matrix_A=matrix
        self.m, self.n=matrix.shape
 
    @staticmethod
    def get_index_with_negative_estimate(not_basis_index_set, estimates_vector, eps):
        """
        :type not_basis_index_set: list
        :type estimates_vector: Matrix
        :rtype: int
        """
        for i, j in enumerate(not_basis_index_set):
            if estimates_vector[i, 0] < -eps:
                return j
        return -1
 
    @staticmethod
    def get_theta_0(basis_indexes_set, vector_z, basis_plan, eps):
        """
        :type basis_indexes_set: list
        :type vector_z: Matrix
        :type basis_plan: Matix
        :rtype: tuple
        """
        theta_indexes=[j for j in basis_indexes_set if vector_z[basis_indexes_set.index(j), 0]>eps]
        vector_theta=[basis_plan[j, 0] / vector_z[basis_indexes_set.index(j), 0] for j in theta_indexes]
        j_s=theta_indexes[0]
        theta_0=vector_theta[0]
        for j, theta in zip(theta_indexes[1:], vector_theta[1:]):
            if theta<theta_0 or (theta==theta_0 and j<j_s):
                theta_0=theta
                j_s=j
        return j_s, theta_0
 
    def find_optimum_plan(self, basis_plan, basis_indexes_set, matrix_A=None, matrix_c=None):
        """
        :type basis_plan: Matrix
        :type basis_indexes_set: list
        :type matrix_A: Matrix
        :type matrix_c: Matrix
        :rtype: Matrix
        """
        if matrix_A is None:
            matrix_A = self._matrix_A
        if matrix_c is None:
            matrix_c = self.matrix_c
        basis_plan=basis_plan.copy()
        basis_indexes_set=list(basis_indexes_set)
        m, n = matrix_A.shape
        basis_indexes_set.sort()
        not_basis_index_set = sorted(set(range(n)) - set(basis_indexes_set))
        basis_inverse_matrix = get_basis_matrix(matrix_A,basis_indexes_set).inv()
        basis_cost_vector = get_basis_cost_vector(matrix_c,basis_indexes_set)
        while True:
            potentials_vector = basis_cost_vector.transpose() * basis_inverse_matrix
            estimates_vestor = zeros(len(not_basis_index_set), 1)
            for i, j in enumerate(not_basis_index_set):
                estimates_vestor[i, 0] = (potentials_vector * matrix_A[:,j] - matrix_c[j, :])[0, 0]
            for i in xrange(len(not_basis_index_set)):
                if estimates_vestor[i, 0] < -self.eps:
                    break
            else:
                return basis_plan, basis_indexes_set
            j_0 = SimplexMethod.get_index_with_negative_estimate(not_basis_index_set, estimates_vestor, self.eps)
            vector_z = basis_inverse_matrix * matrix_A[:,j_0]
            for i in xrange(vector_z.shape[0]):
                if vector_z[i, 0] > self.eps:
                    break
            else:
                raise Exception("Function is unlimited")
            j_s,theta_0 = SimplexMethod.get_theta_0(basis_indexes_set, vector_z, basis_plan, self.eps)
            basis_plan[j_0, 0] = theta_0
            for i, j in enumerate(basis_indexes_set):
                basis_plan[j, 0] -= theta_0 * vector_z[i, 0]
            basis_indexes_set.remove(j_s)
            bisect.insort_left(basis_indexes_set, j_0)
            not_basis_index_set.remove(j_0)
            bisect.insort_left(not_basis_index_set, j_s)
            basis_inverse_matrix = get_basis_matrix(matrix_A,basis_indexes_set).inv()
            basis_cost_vector = get_basis_cost_vector(matrix_c,basis_indexes_set)
 
    @staticmethod
    def remove_negative_rows(matrix_b, matrix_A):
        """
        :type matrix_b: Matrix
        :type matrix_A: Matrix
        :rtype:None
        """
        for i in xrange(matrix_b.shape[0]):
            if matrix_b[i, 0] < 0:
                matrix_b[i, 0] = -matrix_b[i, 0]
                matrix_A[i, :] = -matrix_A[i, :]
 
    def get_basis_plan(self):
        """
        :rtype:tuple
        """
        SimplexMethod.remove_negative_rows(self.matrix_b, self._matrix_A)
        matrix_A = SimplexMethod.get_extended_matrix_A(self._matrix_A)
        matrix_c = zeros(self.n + self.m, 1)
        variable_quantity=self.n
        for i in xrange(self.n, self.m + self.n):
            matrix_c[i, 0] = -1
        basis_plan = zeros(self.n + self.m, 1)
        for i in xrange(self.n, self.m + self.n):
            basis_plan[i, 0] = self.matrix_b[i - self.n, 0]
        j_u_indexes_set = range(self.n, self.n + self.m)
        j_indexes_set = range(self.n)
        basis_plan, basis_indexes_set = self.find_optimum_plan(basis_plan, j_u_indexes_set, matrix_A, matrix_c)
        for i in j_u_indexes_set:
            if abs(basis_plan[i,0]) >= self.eps:
                raise Exception("No plans can be found")
        basis_matrix = get_basis_matrix(matrix_A, basis_indexes_set)
        inverse_basis_matrix = basis_matrix.inv()
        while True:
            j_k = SimplexMethod.get_synthetic_index(basis_indexes_set, j_u_indexes_set)
            if j_k == -1:
                return basis_plan[:variable_quantity, :], basis_indexes_set
            j_0 = SimplexMethod.find_index_with_non_zero_alpha(sorted(set(j_indexes_set)-set(basis_indexes_set)), basis_indexes_set.index(j_k),
                                                      inverse_basis_matrix, matrix_A, self.eps)
            if j_0 != -1:
                basis_indexes_set.remove(j_k)
                bisect.insort_left(basis_indexes_set, j_0)
                inverse_basis_matrix = get_basis_matrix(matrix_A,basis_indexes_set).inv()
            else:
                i_0 = j_k - self.n
                k = basis_indexes_set.index(j_k)
                self._matrix_A.row_del(i_0)
                self.matrix_b.row_del(i_0)
                matrix_A = self.get_extended_matrix_A(self._matrix_A)
                matrix_c.row_del(j_k)
                basis_matrix.row_del(i_0)
                basis_matrix.col_del(k)
                inverse_basis_matrix.row_del(k)
                inverse_basis_matrix.col_del(i_0)
                basis_indexes_set.remove(j_k)
                j_u_indexes_set.remove(j_k)
                basis_plan.row_del(j_k)
                decrease_more_than_j_k=lambda x: x - 1 if x > j_k else x
                basis_indexes_set = map(decrease_more_than_j_k, basis_indexes_set)
                j_u_indexes_set = map(decrease_more_than_j_k, j_u_indexes_set)
 
    @staticmethod
    def get_synthetic_index(basis_indexes_set, j_u_indexes_set):
        """
        :type basis_indexes_set: list
        :type j_u_indexes_set: list
        :rtype: int
        """
        j_u_in_basis=set(basis_indexes_set).intersection(set(j_u_indexes_set))
        if j_u_in_basis:
            return min(j_u_in_basis)
        return -1
 
    @staticmethod
    def find_index_with_non_zero_alpha(not_basis_index_set, k, inverse_basis_matrix, matrix_A, eps):
        """
        :type not_basis_index_set: list
        :type inverse_basis_matrix: Matrix
        :type matrix_A:Matrix
        :rtype: int
        """
        for j in not_basis_index_set:
            if abs((inverse_basis_matrix[k, :] * matrix_A[:, j])[0,0]) > eps:
                return j
        return -1
 
    @staticmethod
    def get_extended_matrix_A(matrix_A):
        """
        :type matrix_A: Matrix
        :rtype: Matrix
        """
        m, n = matrix_A.shape
        extended_matrix = zeros(m, n + m)
        for i in xrange(n):
            extended_matrix[:, i] = matrix_A[:, i]
        for i in xrange(m):
            extended_matrix[i, n + i] = 1
        return extended_matrix
 
    @staticmethod
    def get_extended_matrix_c(matrix_c, variable_count):
        """
        :type matrix_A: Matrix
        :rtype: Matrix
        """
        extended_matrix = zeros(variable_count, 1)
        for i in xrange(matrix_c.shape[0]):
            extended_matrix[i, 0] = matrix_c[i, 0]
        for i in xrange(matrix_c.shape[0], variable_count):
            extended_matrix[i, 0] = 0
        return extended_matrix
 
    def solve(self, maximize):
        self._matrix_A, self.matrix_c=get_cannonical_form(self.matrix_A, self.condition_operators,self.matrix_c, maximize)
        self.m, self.n=self.matrix_A.shape
        basis_plan, basis_indexes_set = self.get_basis_plan()
        basis_plan, basis_indexes_set= self.find_optimum_plan(basis_plan, basis_indexes_set)
        return basis_plan, basis_indexes_set
 
def get_cannonical_form(matrix_A, condition_operators, matrix_c, maximize):
    """
    :type matrix_A: Matrix
    :rtype: Matrix
    """
    m, n = matrix_A.shape
    synthetic_variables_count=0
    for var in condition_operators:
        if var!='=':
            synthetic_variables_count+=1
    extended_matrix = zeros(m, n + synthetic_variables_count)
    for i in xrange(n):
        extended_matrix[:, i] = matrix_A[:, i]
    synt_variable_index=0
    for i in xrange(len(condition_operators)):
        value = 0
        if condition_operators[i] == "<=":
            value = 1
        elif condition_operators[i] == ">=":
            value = -1
        elif condition_operators[i] == '=':
            continue
        else:
            raise Exception("Syntax error in conditions")
        extended_matrix[i, n + synt_variable_index] = value
        synt_variable_index+=1
    extended_matrix_c=zeros(extended_matrix.shape[1], 1)
    for i in xrange(matrix_c.shape[0]):
        if maximize:
            extended_matrix_c[i, 0]=matrix_c[i, 0]
        else:
            extended_matrix_c[i, 0]=-matrix_c[i, 0]
    return extended_matrix, extended_matrix_c
 
def get_basis_matrix(matrix_A,basis_indexes_set):
    """
    :type basis_indexes_set:list
    :type matrix_A:Matrix
    :rtype:Matrix
    """
    m, n = matrix_A.shape[0], len(basis_indexes_set)
    assert m==n
    basis_matrix = zeros(m, n)
    for i, basis_index in enumerate(basis_indexes_set):
        basis_matrix[:, i] = matrix_A[:, basis_index]
    return basis_matrix
 
def get_basis_cost_vector(matrix_c, basis_indexes_set):
    """
    :type basis_indexes_set: list
    :rtype:Matrix
    """
    basis_cost_vector = zeros(len(basis_indexes_set), 1)
    for i, basis_index in enumerate(basis_indexes_set):
        basis_cost_vector[i, 0] = matrix_c[basis_index, 0]
    return basis_cost_vector