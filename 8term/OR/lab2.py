from sympy import Matrix
from lab2.BranchnBound import BranchnBound

A_matrix = Matrix([[1, 4, 2, -6, 3, -7, 1], [-2, 5, 1, 0, 2, 6, 1], [3, -3, 1, 0, 4, -5, -1]])
b_matrix = Matrix([-2, 13, -1])
c_matrix = Matrix([-1, 2, 4, 8, 9, -3, 7])
d_lower = Matrix([-1, -2, 0, -3, -1, -2, -1])
d_upper = Matrix([4, 3, 2, 4, 6, 4, 2])
solver = BranchnBound(A_matrix, b_matrix, c_matrix, d_lower, d_upper)
plan, record = solver.solve()
print(plan, record)
