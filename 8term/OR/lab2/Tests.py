from __future__ import division

import unittest
from sympy.matrices import Matrix
from lab1.MatricesHelper import matrices_equal
from BranchnBound import BranchnBound


class TestExamples(unittest.TestCase):
    def setUp(self):
        self.eps = 0.01

    def test_example1(self):
        A_matrix = Matrix([[1, -5, 3, 1, 0, 0], [4, -1, 1, 0, 1, 0], [2, 4, 2, 0, 0, 1]])
        b_matrix = Matrix([-8, 22, 30])
        c_matrix = Matrix([7, -2, 6, 0, 5, 2])
        d_lower = Matrix([2, 1, 0, 0, 1, 1])
        d_upper = Matrix([6, 6, 5, 2, 4, 6])
        solver = BranchnBound(A_matrix, b_matrix, c_matrix, d_lower, d_upper)
        plan, record = solver.solve()
        self.assertTrue(matrices_equal(plan, Matrix([[6], [3], [0], [1], [1], [6]])))
        self.assertLess(abs(record - 53), self.eps)

    def test_example2(self):
        A_matrix = Matrix([[1, 0, 3, 1, 0, 0], [0, -1, 1, 1, 1, 2], [-2, 4, 2, 0, 0, 1]])
        b_matrix = Matrix([10, 8, 10])
        c_matrix = Matrix([7, -2, 6, 0, 5, 2])
        d_lower = Matrix([0, 1, -1, 0, -2, 1])
        d_upper = Matrix([3, 3, 6, 2, 4, 6])
        solver = BranchnBound(A_matrix, b_matrix, c_matrix, d_lower, d_upper)
        plan, record = solver.solve()
        self.assertTrue(matrices_equal(plan, Matrix([[1], [1], [3], [0], [2], [2]])))
        self.assertLess(abs(record - 37), self.eps)

    def test_example3(self):
        A_matrix = Matrix([[1, 0, 1, 0, 0, 1], [1, 2, -1, 1, 1, 2], [-2, 4, 1, 0, 1, 0]])
        b_matrix = Matrix([-3, 3, 13])
        c_matrix = Matrix([-3, 2, 0, -2, -5, 2])
        d_lower = Matrix([-2, -1, -2, 0, 1, -4])
        d_upper = Matrix([2, 3, 1, 5, 4, -1])
        solver = BranchnBound(A_matrix, b_matrix, c_matrix, d_lower, d_upper)
        plan, record = solver.solve()
        self.assertTrue(matrices_equal(plan, Matrix([[-2], [2], [0], [2], [1], [-1]])))
        self.assertLess(abs(record - (-1)), self.eps)

    def test_example4(self):
        A_matrix = Matrix([[1, 0, 0, 12, 1, -3, 4, -1], [0, 1, 0, 11, 12, 3, 5, 3], [0, 0, 1, 1, 0, 22, -2, 1]])
        b_matrix = Matrix([40, 107, 61])
        c_matrix = Matrix([2, 1, -2, -1, 4, -5, 5, 5])
        d_lower = Matrix([0, 0, 0, 0, 0, 0, 0, 0])
        d_upper = Matrix([3, 5, 5, 3, 4, 5, 6, 3])
        solver = BranchnBound(A_matrix, b_matrix, c_matrix, d_lower, d_upper)
        plan, record = solver.solve()
        self.assertTrue(matrices_equal(plan, Matrix([[1], [1], [2], [2], [3], [3], [6], [3]])))
        self.assertLess(abs(record - 39), self.eps)

    def test_example5(self):
        A_matrix = Matrix(
            [[1, -3, 2, 0, 1, -1, 4, -1, 0], [1, -1, 6, 1, 0, -2, 2, 2, 0], [2, 2, -1, 1, 0, -3, 8, -1, 1],
             [4, 1, 0, 0, 1, -1, 0, -1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]])
        b_matrix = Matrix([3, 9, 9, 5, 9])
        c_matrix = Matrix([-1, 5, -2, 4, 3, 1, 2, 8, 3])
        d_lower = Matrix([0, 0, 0, 0, 0, 0, 0, 0, 0])
        d_upper = Matrix([5, 5, 5, 5, 5, 5, 5, 5, 5])
        solver = BranchnBound(A_matrix, b_matrix, c_matrix, d_lower, d_upper)
        plan, record = solver.solve()
        self.assertTrue(matrices_equal(plan, Matrix([[1], [1], [1], [1], [1], [1], [1], [1], [1]])))
        self.assertLess(abs(record - 23), self.eps)

    def test_example6(self):
        A_matrix = Matrix([[1, 0, 0, 12, 1, -3, 4, -1, 2.5, 3], [0, 1, 0, 11, 12, 3, 5, 3, 4, 5.1],
                           [0, 0, 1, 1, 0, 22, -2, 1, 6.1, 7]])
        b_matrix = Matrix([43.5, 107.3, 106.3])
        c_matrix = Matrix([2, 1, -2, -1, 4, -5, 5, 5, 1, 2])
        d_lower = Matrix([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        d_upper = Matrix([2, 4, 5, 3, 4, 5, 4, 4, 5, 6])
        solver = BranchnBound(A_matrix, b_matrix, c_matrix, d_lower, d_upper)
        plan, record = solver.solve()
        self.assertTrue(matrices_equal(plan, Matrix([[1], [1], [2], [2], [2], [3], [3], [3], [3], [3]])))
        self.assertLess(abs(record - 29), self.eps)

    def test_example7(self):
        A_matrix = Matrix(
            [[4, 0, 0, 0, 0, -3, 4, -1, 2, 3], [0, 1, 0, 0, 0, 3, 5, 3, 4, 5], [0, 0, 1, 0, 0, 22, -2, 1, 6, 7],
             [0, 0, 0, 1, 0, 6, -2, 7, 5, 6], [0, 0, 0, 0, 1, 5, 5, 1, 6, 7]])
        b_matrix = Matrix([8, 5, 4, 7, 8])
        c_matrix = Matrix([2, 1, -2, -1, 4, -5, 5, 5, 1, 2])
        d_lower = Matrix([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        d_upper = Matrix([10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
        solver = BranchnBound(A_matrix, b_matrix, c_matrix, d_lower, d_upper)
        plan, record = solver.solve()
        self.assertTrue(matrices_equal(plan, Matrix([[2], [5], [4], [7], [8], [0], [0], [0], [0], [0]])))
        self.assertLess(abs(record - 26), self.eps)

    def test_example8(self):
        A_matrix = Matrix([[1, -5, 3, 1, 0, 0], [4, -1, 1, 0, 1, 0], [2, 4, 2, 0, 0, 1]])
        b_matrix = Matrix([-8, 22, 30])
        c_matrix = Matrix([7, -2, 6, 0, 5, 2])
        d_lower = Matrix([2, 1, 0, 0, 1, 1])
        d_upper = Matrix([6, 6, 5, 2, 4, 6])
        solver = BranchnBound(A_matrix, b_matrix, c_matrix, d_lower, d_upper)
        plan, record = solver.solve()
        self.assertTrue(matrices_equal(plan, Matrix([[6], [3], [0], [1], [1], [6]])))
        self.assertLess(abs(record - 53), self.eps)

    def test_example9(self):
        A_matrix = Matrix([[1, 0, 0, 3, 1, -3, 4, -1], [0, 1, 0, 4, -3, 3, 5, 3], [0, 0, 1, 1, 0, 2, -2, 1]])
        b_matrix = Matrix([30, 78, 5])
        c_matrix = Matrix([2, 1, -2, -1, 4, -5, 5, 5])
        d_lower = Matrix([0, 0, 0, 0, 0, 0, 0, 0])
        d_upper = Matrix([5, 5, 3, 4, 5, 6, 6, 8])
        solver = BranchnBound(A_matrix, b_matrix, c_matrix, d_lower, d_upper)
        plan, record = solver.solve()
        self.assertTrue(matrices_equal(plan, Matrix([[5], [5], [3], [4], [0], [1], [6], [8]])))
        self.assertLess(abs(record - 70), self.eps)

    def test_example10(self):
        A_matrix = Matrix(
            [[1, -3, 2, 0, 1, -1, 4, -1, 0], [1, -1, 6, 1, 0, -2, 2, 2, 0], [2, 2, -1, 1, 0, -3, 2, -1, 1],
             [4, 1, 0, 0, 1, -1, 0, -1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]])
        b_matrix = Matrix([18, 18, 30, 15, 18])
        c_matrix = Matrix([7, 5, -2, 4, 3, 1, 2, 8, 3])
        d_lower = Matrix([0, 0, 0, 0, 0, 0, 0, 0, 0])
        d_upper = Matrix([8, 8, 8, 8, 8, 8, 8, 8, 8])
        solver = BranchnBound(A_matrix, b_matrix, c_matrix, d_lower, d_upper)
        plan, record = solver.solve()
        self.assertTrue(matrices_equal(plan, Matrix([[3], [5], [0], [0], [0], [0], [8], [2], [0]])))
        self.assertLess(abs(record - 78), self.eps)

    def test_example11(self):
        A_matrix = Matrix([[1, 0, 1, 0, 4, 3, 4], [0, 1, 2, 0, 55, 3.5, 5], [0, 0, 3, 1, 6, 2, -2.5]])
        b_matrix = Matrix([26, 185, 32.5])
        c_matrix = Matrix([1, 2, 3, -1, 4, -5, 6])
        d_lower = Matrix([0, 2, 0, 0, 0, 0, 0])
        d_upper = Matrix([1, 2, 5, 7, 8, 4, 2])
        solver = BranchnBound(A_matrix, b_matrix, c_matrix, d_lower, d_upper)
        plan, record = solver.solve()
        self.assertTrue(matrices_equal(plan, Matrix([[1], [2], [3], [4], [3], [2], [1]])))
        self.assertLess(abs(record - 18), self.eps)

    def test_example12(self):
        A_matrix = Matrix(
            [[2, 0, 1, 0, 0, 3, 5], [0, 2, 2.1, 0, 0, 3.5, 5], [0, 0, 3, 2, 0, 2, 1.1], [0, 0, 3, 0, 2, 2, -2.5]])
        b_matrix = Matrix([58, 66.3, 36.7, 13.5])
        c_matrix = Matrix([1, 2, 3, 1, 2, 3, 4])
        d_lower = Matrix([1, 1, 1, 1, 1, 1, 1])
        d_upper = Matrix([2, 3, 4, 5, 8, 7, 7])
        solver = BranchnBound(A_matrix, b_matrix, c_matrix, d_lower, d_upper)
        plan, record = solver.solve()
        self.assertTrue(matrices_equal(plan, Matrix([[1], [2], [3], [4], [5], [6], [7]])))
        self.assertLess(abs(record - 74), self.eps)

    def test_example13(self):
        A_matrix = Matrix(
            [[1, 0, 0, 1, 1, -3, 4, -1, 3, 3], [0, 1, 0, -2, 1, 1, 7, 3, 4, 5], [0, 0, 1, 1, 0, 2, -2, 1, -4, 7]])
        b_matrix = Matrix([27, 6, 18])
        c_matrix = Matrix([-2, 1, -2, -1, 8, -5, 3, 5, 1, 2])
        d_lower = Matrix([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        d_upper = Matrix([8, 7, 6, 7, 8, 5, 6, 7, 8, 5])
        solver = BranchnBound(A_matrix, b_matrix, c_matrix, d_lower, d_upper)
        plan, record = solver.solve()
        self.assertTrue(matrices_equal(plan, Matrix([[5], [0], [6], [7], [8], [0], [1], [0], [0], [1]])))
        self.assertLess(abs(record - 40), self.eps)


if __name__ == "__main__":
    unittest.main()
