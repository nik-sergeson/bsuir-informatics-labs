from __future__ import division
from sympy import Matrix
from simplex_method.lab2.SimplexMethod import SimplexMethod

test_second_phase = True
test_simplex_method = True

if __name__ == "__main__":
    if test_second_phase:
        A = Matrix([[1, 4, 4, 1], [1, 7, 8, 2]])
        C = Matrix([1, -3, -5, -1])
        b = Matrix([[5], [9]])
        x = Matrix([1, 0, 1, 0])
        Jb = [0, 2]
        simplmethod = SimplexMethod(C, A, b, 0.001)
        basis_plan, basis_indexes_set = simplmethod.find_optimum_plan(x, Jb)
        assert basis_plan.equals(Matrix([[1], [0], [0], [4]]))
        A = Matrix([[3, 1, 2, 6, 9, 3], [1, 2, -1, 2, 3, 1]])
        C = Matrix([-2, 1, 1, -1, 4, 1])
        b = Matrix([[15], [5]])
        x = Matrix([5, 0, 0, 0, 0, 0])
        Jb = [0, 1]
        simplmethod = SimplexMethod(C, A, b, 0.001)
        basis_plan, basis_indexes_set = simplmethod.find_optimum_plan(x, Jb)
        assert basis_plan.equals(Matrix([[0], [5], [5], [0], [0], [0]]))
        A = Matrix([[3.0, 1, 1, 0], [1, -2, 0, 1]])
        C = Matrix([1.0, 4, 1, -1])
        b = Matrix([[1.0], [1]])
        x = Matrix([0, 0, 1, 1])
        Jb = [2, 3]
        simplmethod = SimplexMethod(C, A, b, 0.001)
        basis_plan, basis_indexes_set = simplmethod.find_optimum_plan(x, Jb)
        assert basis_plan.equals(Matrix([[0], [1], [0], [3]]))
        A = Matrix([[2, 0, -1, 1], [3, 3, 0, 3]])
        C = Matrix([1, 1, 1, 1])
        b = Matrix([[1], [6]])
        x = Matrix([0, 1, 0, 1])
        Jb = [1, 3]
        simplmethod = SimplexMethod(C, A, b, 0.001)
        basis_plan, basis_indexes_set = simplmethod.find_optimum_plan(x, Jb)
        assert basis_plan.equals(Matrix([[2], [0], [3], [0]]))
    if test_simplex_method:
        conditions = ['<=', '<=']
        A = Matrix([[1, 4, 4, 1], [1, 7, 8, 2]])
        C = Matrix([1, -3, -5, -1])
        b = Matrix([[5], [9]])
        simplmethod = SimplexMethod(C, A, b, 0.001, conditions)
        basis_plan, basis_indexes_set = simplmethod.solve(True)
        assert basis_plan.equals(Matrix([[5], [0], [0], [0], [0], [4]]))
        conditions = ['<=', '<=']
        A = Matrix([[3, 1, 2, 6, 9, 3], [1, 2, -1, 2, 3, 1]])
        C = Matrix([-2, 1, 1, -1, 4, 1])
        b = Matrix([[15], [5]])
        simplmethod = SimplexMethod(C, A, b, 0.001, conditions)
        basis_plan, basis_indexes_set = simplmethod.solve(True)
        assert basis_plan.equals(Matrix([[0], [5], [5], [0], [0], [0], [0], [0]]))
        conditions = ['<=', '<=']
        A = Matrix([[3.0, 1, 1, 0], [1, -2, 0, 1]])
        C = Matrix([1.0, 4, 1, -1])
        b = Matrix([[1.0], [1]])
        simplmethod = SimplexMethod(C, A, b, 0.001, conditions)
        basis_plan, basis_indexes_set = simplmethod.solve(True)
        assert basis_plan.equals(Matrix([[0], [1.00000000000000], [0], [0], [0], [3.00000000000000]]))
    conditions = ['>=', '<=', '<=']
    A = Matrix([[1, -1], [1, -2], [1, 1]])
    C = Matrix([1, 2])
    b = Matrix([[1], [1], [3]])
    simplmethod = SimplexMethod(C, A, b, 0.001, conditions)
    basis_plan, basis_indexes_set = simplmethod.solve(True)
    print(basis_plan, basis_indexes_set)
