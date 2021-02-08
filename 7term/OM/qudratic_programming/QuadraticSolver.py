from __future__ import division
from sympy import Matrix, zeros, transpose
import bisect
from simplex_method.lab2.SimplexMethod import SimplexMethod
import math


class QuadraticSolver(object):
    """
    :type matrix_A:Matrix
    :type matrix_b:Matrix
    :type matrix_c:matrix_c
    :type matrix_D:matrix_D
    :type eps:float
    """

    def __init__(self, matrix_A, matrix_b, matrix_c, matrix_D, eps):
        self.matrix_A = matrix_A
        self.matrix_b = matrix_b
        self.matrix_c = matrix_c
        self.matrix_D = matrix_D
        self.eps = eps

    def solve(self):
        simplex_solver = SimplexMethod(self.matrix_c, self.matrix_A, self.matrix_b, self.eps)
        vector_x, supporting_set = simplex_solver.solve(False)
        J_asterisk = list(supporting_set)
        not_J_asterisk = sorted(set(range(vector_x.shape[0])) - set(supporting_set))
        while True:
            vector_c_x = self.matrix_c + self.matrix_D * vector_x
            A_supporting = zeros(self.matrix_A.shape[0], len(supporting_set))
            c_x_supporting = zeros(len(supporting_set), 1)
            for i, index in enumerate(supporting_set):
                A_supporting[:, i] = self.matrix_A[:, index]
                c_x_supporting[i, 0] = vector_c_x[index, 0]
            vector_u_x = -transpose(c_x_supporting) * A_supporting.inv()
            vector_delta = zeros(1, len(not_J_asterisk))
            for i, j in enumerate(not_J_asterisk):
                vector_delta[0, i] = (vector_u_x * self.matrix_A[:, j])[0, 0] + vector_c_x[j]
            for i, j in enumerate(not_J_asterisk):
                if vector_delta[0, i] < 0:
                    j_0 = j
                    break
            else:
                return vector_x, supporting_set
            j_0_index = not_J_asterisk.index(j_0)
            while True:
                l_direction, vector_y = self.get_l_direction(J_asterisk, j_0, vector_x.shape[0])
                min_theta = float("inf")
                min_theta_index = -1
                for j in J_asterisk:
                    if l_direction[j, 0] < 0:
                        curr_theta = -vector_x[j, 0] / l_direction[j, 0]
                        if curr_theta < min_theta:
                            min_theta = curr_theta
                            min_theta_index = j
                theta_j_0, delta_j_0 = self.get_theta_j_0(J_asterisk, j_0, j_0_index, vector_delta, l_direction,
                                                          vector_y)
                if theta_j_0 < min_theta:
                    min_theta = theta_j_0
                    min_theta_index = j_0
                if min_theta == float("inf"):
                    raise Exception("Unlimited function")
                vector_x = vector_x + min_theta * l_direction
                if min_theta_index == j_0:
                    bisect.insort_left(J_asterisk, j_0)
                    not_J_asterisk.remove(j_0)
                    break
                elif min_theta_index not in supporting_set:
                    J_asterisk.remove(min_theta_index)
                    bisect.insort_left(not_J_asterisk, min_theta_index)
                    vector_delta[0, j_0_index] += min_theta * delta_j_0
                    continue
                else:
                    j_plus = self.find_j_plus(J_asterisk, supporting_set, min_theta_index)
                    if j_plus != -1:
                        supporting_set.remove(min_theta_index)
                        bisect.insort_left(supporting_set, j_plus)
                        J_asterisk.remove(min_theta_index)
                        bisect.insort_left(not_J_asterisk, min_theta_index)
                        vector_delta[0, j_0_index] += min_theta * delta_j_0
                        continue
                    else:
                        supporting_set.remove(min_theta_index)
                        bisect.insort_left(supporting_set, j_0)
                        J_asterisk.remove(min_theta_index)
                        bisect.insort_left(J_asterisk, j_0)
                        not_J_asterisk.remove(j_0)
                        bisect.insort_left(not_J_asterisk, min_theta_index)
                        break

    def find_j_plus(self, J_asterisk, support_set, min_theta_index):
        """
        :type J_asterisk:list
        :type support_set:list
        """
        s_index = support_set.index(min_theta_index)
        search_set = set(J_asterisk) - set(support_set)
        A_support = zeros(self.matrix_A.shape[0], len(support_set))
        for i, j in enumerate(support_set):
            A_support[:, i] = self.matrix_A[:, j]
        A_support_inv = A_support.inv()
        for j_plus in search_set:
            if math.fabs(A_support_inv * self.matrix_A[:, j_plus][s_index, 0]) > self.eps:
                return j_plus
        return -1

    def get_l_direction(self, J_asterisk, j_0, variable_quantity):
        """
        :type J_asterisk:list
        """
        matrix_A_asterisk = zeros(self.matrix_A.shape[0], len(J_asterisk))
        matrix_D_aster_j_0 = zeros(len(J_asterisk), 1)
        matrix_D_aster = zeros(len(J_asterisk), len(J_asterisk))
        for i, j in enumerate(J_asterisk):
            matrix_A_asterisk[:, i] = self.matrix_A[:, j]
            matrix_D_aster_j_0[i, 0] = self.matrix_D[j, j_0]
            for sub_i, sub_j in enumerate(J_asterisk):
                matrix_D_aster[i, sub_i] = self.matrix_D[j, sub_j]
        matrix_H = zeros(matrix_D_aster.shape[0] + matrix_A_asterisk.shape[0],
                         matrix_D_aster.shape[1] + matrix_A_asterisk.shape[0])
        matrix_H[0:matrix_D_aster.shape[0], 0:matrix_D_aster.shape[1]] = matrix_D_aster[:, :]
        matrix_H[0:matrix_A_asterisk.shape[1], matrix_D_aster.shape[1]:] = transpose(matrix_A_asterisk)[:, :]
        matrix_H[matrix_D_aster.shape[0]:, 0:matrix_A_asterisk.shape[1]] = matrix_A_asterisk[:, :]
        matrix_b = zeros(matrix_D_aster_j_0.shape[0] + self.matrix_A.shape[0], 1)
        matrix_b[:matrix_D_aster_j_0.shape[0], :] = matrix_D_aster_j_0[:, :]
        matrix_b[matrix_D_aster_j_0.shape[0]:, :] = self.matrix_A[:, j_0]
        l_asterisk_y = -matrix_H.inv() * matrix_b
        l_direction = zeros(variable_quantity, 1)
        l_direction[j_0, 0] = 1
        for i, j in enumerate(J_asterisk):
            l_direction[j, 0] = l_asterisk_y[i, 0]
        return l_direction, l_asterisk_y[len(J_asterisk):, :]

    def get_theta_j_0(self, J_asterisk, j_0, j_0_index, vector_delta, l_direction, vector_y):
        l_asterisk = zeros(len(J_asterisk), 1)
        for i, j in enumerate(J_asterisk):
            l_asterisk[i, 0] = l_direction[j, 0]
        matrix_D_aster_j_0 = zeros(len(J_asterisk), 1)
        for i, j in enumerate(J_asterisk):
            matrix_D_aster_j_0[i, 0] = self.matrix_D[j, j_0]
        delta = (transpose(matrix_D_aster_j_0) * l_asterisk + transpose(self.matrix_A[:, j_0]) * vector_y)[0, 0] + \
                self.matrix_D[j_0, j_0]
        if delta == 0:
            return float("inf"), delta
        elif delta > 0:
            return math.fabs(vector_delta[0, j_0_index]) / delta, delta
