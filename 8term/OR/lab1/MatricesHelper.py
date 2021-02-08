from __future__ import division

from sympy import zeros, eye


def matrix_C_determinant_is_null(vector_c_k_with_wave, matrix_C_inverse, k):
    row_count, col_count = vector_c_k_with_wave.shape
    e_k = zeros(1, row_count)
    e_k[0, k] = 1
    return e_k * matrix_C_inverse * vector_c_k_with_wave == 0


def get_matrix_B_with_wave(vector_c_k_with_wave, matrix_B, k):
    row_count, col_count = vector_c_k_with_wave.shape
    matrix_D = eye(row_count)
    matrix_z = matrix_B * vector_c_k_with_wave
    z_k = matrix_z[k, 0]
    matrix_z[k, 0] = -1
    matrix_d = (-1 / z_k) * matrix_z
    matrix_D[:, k] = matrix_d
    return matrix_D * matrix_B


def get_inverse_matrix(matrix_C):
    row_count, col_count = matrix_C.shape
    i = 0
    matrix_C_construction = eye(row_count)
    matrix_B_construction = eye(row_count)
    set_J = set(range(row_count))
    permutation = range(row_count)
    while i < row_count:
        all_alpha_j_zeros = False
        non_zero_alpha_index = -1
        for j in set_J:
            e_i_1 = zeros(1, row_count)
            e_i_1[0, i] = 1
            alpha_j = e_i_1 * matrix_B_construction * matrix_C[:, j]
            if alpha_j[0, 0] != 0:
                non_zero_alpha_index = j
                break
        else:
            all_alpha_j_zeros = True
        if not all_alpha_j_zeros:
            c_i_with_wave = matrix_C[:, non_zero_alpha_index]
            set_J.remove(non_zero_alpha_index)
            permutation[non_zero_alpha_index] = i
            matrix_C_construction[:, i] = c_i_with_wave
            matrix_D = eye(row_count)
            matrix_z = matrix_B_construction * c_i_with_wave
            z_k = matrix_z[i, 0]
            matrix_z[i, 0] = -1
            matrix_d = (-1 / z_k) * matrix_z
            matrix_D[:, i] = matrix_d
            matrix_B_construction = matrix_D * matrix_B_construction
            i += 1
        else:
            raise ArithmeticError("Determinant is null")
    else:
        matrix_B_output = zeros(row_count, row_count)
        for j in xrange(row_count):
            matrix_B_output[j, :] = matrix_B_construction[permutation[j], :]
        return matrix_B_output


def matrices_equal(a, b, eps=0.01):
    assert a.shape == b.shape
    rows, cols = a.shape
    for i in xrange(rows):
        for j in xrange(cols):
            if a[i, j] ==float("inf") and  b[i, j]==float("inf"):
                continue
            if abs(a[i, j] - b[i, j]) > eps:
                return False
    return True
