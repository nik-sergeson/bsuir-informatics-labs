from sympy import zeros


def get_basis_matrix(A_matrix, J_basis):
    """
    :type A_matrix:MutableDenseMatrix
    :type J_basis:list
    """
    basis_matrix = zeros(A_matrix.shape[0], len(J_basis))
    for i, j in enumerate(J_basis):
        basis_matrix[:, i] = A_matrix[:, j]
    return basis_matrix


def get_basis_c_vector(c_matrix, J_basis):
    """
    :type c_matrix:MutableDenseMatrix
    :type J_basis:list
    """
    basis_c = zeros(len(J_basis), 1)
    for i, j in enumerate(J_basis):
        basis_c[i, 0] = c_matrix[j, 0]
    return basis_c

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
    cur_column=0
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
        extended_matrix[i, n + cur_column] = value
        cur_column+=1
    extended_matrix_c=zeros(extended_matrix.shape[1], 1)
    for i in xrange(matrix_c.shape[0]):
        if maximize:
            extended_matrix_c[i, 0]=matrix_c[i, 0]
        else:
            extended_matrix_c[i, 0]=-matrix_c[i, 0]
    return extended_matrix, extended_matrix_c, ['=']*len(condition_operators)
