from __future__ import division

from sympy import Matrix
from lab3.CuttingPlaneMethod import CuttingPlaneMethod

A = Matrix([[1, 1], [1, 1]])
b = Matrix([[1 / 4], [1 / 2]])
c = Matrix([1, 1])
# solver = CuttingPlaneMethod(A, b, c, condition_operators=[">=", "<="])
# plan = solver.solve(True)

from lab3.WithRemovingConstraint.CuttingPlaneMethod import CuttingPlaneMethod
A_matrix = Matrix([[1,4,2,-6,3,-7,1], [-2,5,1,0,2,6,1], [3,-3,1,0,4,-5,-1]])
b_matrix = Matrix([-2,13,-1])
c_matrix = Matrix([-1,2,4,8,9,-3,7])
solver = CuttingPlaneMethod(A_matrix, b_matrix, c_matrix)
plan = solver.solve(True)
result = (c_matrix.transpose() * plan)[0, 0]
print(plan, result)

A_matrix = Matrix([[1,4,2,-6,3,-7,1], [-2,5,1,0,2,6,1], [3,-3,1,0,4,-5,-1]])
b_matrix = Matrix([-2,13,-1])
c_matrix = Matrix([-1,-2,-4,-8,-9,-3,-7])
solver = CuttingPlaneMethod(A_matrix, b_matrix, c_matrix)
plan = solver.solve(True)
result = (c_matrix.transpose() * plan)[0, 0]
print(plan, result)
