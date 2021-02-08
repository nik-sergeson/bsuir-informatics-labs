from __future__ import division

import unittest
from sympy.matrices import Matrix
from lab1.DualSimplexMethod import DualSimplexMethod, find_initial_basis_set
from MatricesHelper import matrices_equal


class TestExamples(unittest.TestCase):
    def test_example1(self):
        A_matrix = Matrix([[2, 1, -1, 0, 0, 1], [1, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 0]])
        b_matrix = Matrix([2, 5, 0])
        c_matrix = Matrix([3, 2, 0, 3, -2, -4])
        d_lower = Matrix([0, -1, 2, 1, -1, 0])
        d_upper = Matrix([2, 4, 4, 3, 3, 5])
        solver = DualSimplexMethod(A_matrix, b_matrix, c_matrix, d_lower, d_upper)
        plan, J_basis = solver.solve([3, 4, 5])
        c_x = c_matrix.transpose() * plan
        self.assertTrue(matrices_equal(plan, Matrix([[3 / 2], [1], [2], [3 / 2], [-1], [0]])))
        self.assertLess(abs(c_x[0, 0] - 13), 0.01)

    def test_example2(self):
        A_matrix = Matrix([[1, -5, 3, 1, 0, 0], [4, -1, 1, 0, 1, 0], [2, 4, 2, 0, 0, 1]])
        b_matrix = Matrix([-7, 22, 30])
        c_matrix = Matrix([7, -2, 6, 0, 5, 2])
        d_lower = Matrix([2, 1, 0, 0, 1, 1])
        d_upper = Matrix([6, 6, 5, 2, 4, 6])
        solver = DualSimplexMethod(A_matrix, b_matrix, c_matrix, d_lower, d_upper)
        plan, J_basis = solver.solve([3, 4, 5])
        c_x = c_matrix.transpose() * plan
        self.assertTrue(plan, Matrix([[5], [3], [1], [0], [4], [6]]))
        self.assertLess(abs(c_x[0, 0] - 67), 0.01)

    def test_example3(self):
        A_matrix = Matrix([[1, 0, 2, 2, -3, 3], [0, 1, 0, -1, 0, 1], [1, 0, 1, 3, 2, 1]])
        b_matrix = Matrix([15, 0, 13])
        c_matrix = Matrix([3, 0.5, 4, 4, 1, 5])
        d_lower = Matrix([0, 0, 0, 0, 0, 0])
        d_upper = Matrix([3, 5, 4, 3, 3, 4])
        solver = DualSimplexMethod(A_matrix, b_matrix, c_matrix, d_lower, d_upper)
        plan, J_basis = solver.solve([0, 1, 2])
        c_x = c_matrix.transpose() * plan
        self.assertTrue(matrices_equal(plan, Matrix([[3], [0], [4], [1.1818], [0.6364], [1.1818]])))
        self.assertLess(abs(c_x[0, 0] - 36.2727), 0.01)

    def test_example4(self):
        A_matrix = Matrix([[1, 0, 0, 12, 1, -3, 4, -1], [0, 1, 0, 11, 12, 3, 5, 3], [0, 0, 1, 1, 0, 22, -2, 1]])
        b_matrix = Matrix([40, 107, 61])
        c_matrix = Matrix([2, 1, -2, -1, 4, -5, 5, 5])
        d_lower = Matrix([0, 0, 0, 0, 0, 0, 0, 0])
        d_upper = Matrix([3, 5, 5, 3, 4, 5, 6, 3])
        solver = DualSimplexMethod(A_matrix, b_matrix, c_matrix, d_lower, d_upper)
        plan, J_basis = solver.solve([0, 1, 2])
        c_x = c_matrix.transpose() * plan
        self.assertTrue(matrices_equal(plan, Matrix([[3], [5], [0], [1.8779], [2.7545], [3.0965], [6], [3]])))
        self.assertLess(abs(c_x[0, 0] - 49.6577), 0.01)

    def test_example5(self):
        A_matrix = Matrix(
            [[1, -3, 2, 0, 1, -1, 4, -1, 0], [1, -1, 6, 1, 0, -2, 2, 2, 0], [2, 2, -1, 1, 0, -3, 8, -1, 1],
             [4, 1, 0, 0, 1, -1, 0, -1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]])
        b_matrix = Matrix([3, 9, 9, 5, 9])
        c_matrix = Matrix([-1, 5, -2, 4, 3, 1, 2, 8, 3])
        d_lower = Matrix([0, 0, 0, 0, 0, 0, 0, 0, 0])
        d_upper = Matrix([5, 5, 5, 5, 5, 5, 5, 5, 5])
        solver = DualSimplexMethod(A_matrix, b_matrix, c_matrix, d_lower, d_upper)
        plan, J_basis = solver.solve([0, 1, 2, 3, 4])
        c_x = c_matrix.transpose() * plan
        self.assertTrue(
            matrices_equal(plan, Matrix([[1.1579], [0.6942], [0], [0], [2.8797], [0], [1.0627], [3.2055], [0]])))
        self.assertLess(abs(c_x[0, 0] - 38.7218), 0.01)

    def test_example6(self):
        A_matrix = Matrix([[1, 7, 2, 0, 1, -1, 4], [0, 5, 6, 1, 0, -3, -2], [3, 2, 2, 1, 1, 1, 5]])
        b_matrix = Matrix([1, 4, 7])
        c_matrix = Matrix([1, 2, 1, -3, 3, 1, 0])
        d_lower = Matrix([-1, 1, -2, 0, 1, 2, 4])
        d_upper = Matrix([3, 2, 2, 5, 3, 4, 5])
        solver = DualSimplexMethod(A_matrix, b_matrix, c_matrix, d_lower, d_upper)
        self.assertRaises(Exception, solver.solve, [0, 1, 2])

    def test_example7(self):
        A_matrix = Matrix([[2, -1, 1, 0, 0, -1, 3], [0, 4, -1, 2, 3, -2, 2], [3, 1, 0, 1, 0, 1, 4]])
        b_matrix = Matrix([1.5, 9, 2])
        c_matrix = Matrix([0, 1, 2, 1, -3, 4, 7])
        d_lower = Matrix([0, 0, -3, 0, -1, 1, 0])
        d_upper = Matrix([3, 3, 4, 7, 5, 3, 2])
        solver = DualSimplexMethod(A_matrix, b_matrix, c_matrix, d_lower, d_upper)
        plan, J_basis = solver.solve([0, 1, 2])
        c_x = c_matrix.transpose() * plan
        self.assertTrue(matrices_equal(plan, Matrix([[0], [1], [3.5], [0], [3.5], [1], [0]])))
        self.assertLess(abs(c_x[0, 0] - 1.5), 0.01)

    def test_example8(self):
        A_matrix = Matrix([[2, 1, 0, 3, -1, -1], [0, 1, -2, 1, 0, 3], [3, 0, 1, 1, 1, 1]])
        b_matrix = Matrix([2, 2, 5])
        c_matrix = Matrix([0, -1, 1, 0, 4, 3])
        d_lower = Matrix([2, 0, -1, -3, 2, 1])
        d_upper = Matrix([7, 3, 2, 3, 4, 5])
        solver = DualSimplexMethod(A_matrix, b_matrix, c_matrix, d_lower, d_upper)
        self.assertRaises(Exception, solver.solve, [0, 1, 2])

    def test_example9(self):
        A_matrix = Matrix([[1, 3, 1, -1, 0, -3, 2, 1], [2, 1, 3, -1, 1, 4, 1, 1], [-1, 0, 2, -2, 2, 1, 1, 1]])
        b_matrix = Matrix([4, 12, 4])
        c_matrix = Matrix([2, -1, 2, 3, -2, 3, 4, 1])
        d_lower = Matrix([-1, -1, -1, -1, -1, -1, -1, -1])
        d_upper = Matrix([2, 3, 1, 4, 3, 2, 4, 4])
        solver = DualSimplexMethod(A_matrix, b_matrix, c_matrix, d_lower, d_upper)
        plan, J_basis = solver.solve([0, 1, 2])
        c_x = c_matrix.transpose() * plan
        self.assertTrue(matrices_equal(plan, Matrix([[-1], [0.4074], [1], [4], [-0.3704], [1.7407], [4], [4]])))
        self.assertLess(abs(c_x[0, 0] - 37.5556), 0.01)


if __name__ == "__main__":
    unittest.main()
