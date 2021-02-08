from sympy.matrices import Matrix
from lab1.DualSimplexMethod import DualSimplexMethod

A_matrix = Matrix([[2, 1, -1, 0, 0, 1], [1, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 0]])
b_matrix = Matrix([2, 5, 0])
c_matrix = Matrix([3, 2, 0, 3, -2, -4])
d_lower = Matrix([0, -1, 2, 1, -1, 0])
d_upper = Matrix([2, 4, 4, 3, 3, 5])
solver = DualSimplexMethod(A_matrix, b_matrix, c_matrix, d_lower, d_upper)
sol = solver.solve([3, 4, 5])
print(sol)
