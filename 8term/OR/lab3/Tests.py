import unittest
from sympy import Matrix
from CuttingPlaneMethod import CuttingPlaneMethod
from lab1.MatricesHelper import matrices_equal


class TestExamples(unittest.TestCase):
    def setUp(self):
        self.eps = 0.01

    def test_example1(self):
        A = Matrix([[5, -1, 1, 0, 0], [-1, 2, 0, 1, 0], [-7, 2, 0, 0, 1]])
        b = Matrix([[15], [6], [0]])
        c = Matrix([3.5, -1, 0, 0, 0])
        true_result = 0
        solver = CuttingPlaneMethod(A, b, c)
        plan = solver.solve(False)
        exp_plan = Matrix([0, 0, 15, 6, 0])
        result = (c.transpose() * plan)[0, 0]
        self.assertAlmostEquals(result, true_result)
        self.assertTrue(matrices_equal(plan, exp_plan, self.eps))

    def test_example2(self):
        A = Matrix([[5, 3, 1, 0, 0], [-1, 2, 0, 1, 0], [1, -2, 0, 0, 1]])
        b = Matrix([[4], [3], [7]])
        c = Matrix([-1, 1, 0, 0, 0])
        true_result = 0
        solver = CuttingPlaneMethod(A, b, c)
        plan = solver.solve(False)
        exp_plan = Matrix([0, 0, 4, 3, 7])
        result = (c.transpose() * plan)[0, 0]
        self.assertAlmostEquals(result, true_result)
        self.assertTrue(matrices_equal(plan, exp_plan, self.eps))

    def test_example3(self):
        c = Matrix([2, -5, 0, 0, 0])
        A = Matrix([[-2, -1, 1, 0, 0], [3, 1, 0, 1, 0], [-1, 1, 0, 0, 1]])
        b = Matrix([[-1], [10], [3]])
        true_result = 6
        solver = CuttingPlaneMethod(A, b, c)
        plan = solver.solve(True)
        result = (c.transpose() * plan)[0, 0]
        exp_plan = Matrix([3, 0, 5, 1, 6, 0])
        self.assertAlmostEquals(result, true_result)
        self.assertTrue(matrices_equal(plan, exp_plan, self.eps))

    def test_task1(self):
        c = Matrix([7, -2, 6, 0, 5, 2])
        A = Matrix([[1, -5, 3, 1, 0, 0], [4, -1, 1, 0, 1, 0], [2, 4, 2, 0, 0, 1]])
        b = Matrix([[-8], [22], [30]])
        true_result = 160
        solver = CuttingPlaneMethod(A, b, c)
        plan = solver.solve(True)
        result = (c.transpose() * plan)[0, 0]
        exp_plan = Matrix([0, 2, 0, 2, 24, 22])
        self.assertAlmostEquals(result, true_result)
        self.assertTrue(matrices_equal(plan, exp_plan, self.eps))

    @unittest.skip("too many constraint needed")
    def test_task2(self):
        A = Matrix([[1, -3, 2, 0, 1, -1, 4, -1, 0], [1, -1, 6, 1, 0, -2, 2, 2, 0], [2, 2, -1, 1, 0, -3, 8, -1, 1],
                    [4, 1, 0, 0, 1, -1, 0, -1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]])
        b = Matrix([[3], [9], [9], [5], [9]])
        c = Matrix([-1, 5, -2, 4, 3, 1, 2, 8, 3])
        true_result = 23
        solver = CuttingPlaneMethod(A, b, c)
        plan = solver.solve(True)
        result = (c.transpose() * plan)[0, 0]
        exp_plan = Matrix([1, 1, 1, 1, 1, 1, 1, 1, 1])
        self.assertAlmostEquals(result, true_result)
        self.assertTrue(matrices_equal(plan, exp_plan, self.eps))

    def test_task3(self):
        A = Matrix([[1, 0, 0, 12, 1, -3, 4, -1], [0, 1, 0, 11, 12, 3, 5, 3], [0, 0, 1, 1, 0, 22, -2, 1]])
        b = Matrix([[40], [107], [61]])
        c = Matrix([2, 1, -2, -1, 4, -5, 5, 5])
        true_result = 311
        solver = CuttingPlaneMethod(A, b, c)
        plan = solver.solve(True)
        result = (c.transpose() * plan)[0, 0]
        exp_plan = Matrix([77, 2, 5, 0, 0, 1, 0, 34])
        self.assertAlmostEquals(result, true_result)
        self.assertTrue(matrices_equal(plan, exp_plan, self.eps))

    @unittest.skip("too many constraint needed")
    def test_task4(self):
        A = Matrix(
            [[1, 2, 3, 12, 1, - 3, 4, - 1, 2, 3], [0, 2, 0, 11, 12, 3, 5, 3, 4, 5], [0, 0, 2, 1, 0, 22, - 2, 1, 6, 7]])
        b = Matrix([[153], [123], [112]])
        c = Matrix([2, 1, -2, -1, 4, -5, 5, 5, 1, 2])
        true_result = 543
        solver = CuttingPlaneMethod(A, b, c)
        plan = solver.solve(True)
        result = (c.transpose() * plan)[0, 0]
        exp_plan = Matrix([188, 0, 4, 0, 0, 3, 0, 38, 0, 0])
        self.assertAlmostEquals(result, true_result)
        self.assertTrue(matrices_equal(plan, exp_plan, self.eps))

    def test_task5(self):
        A = Matrix([[2, 1, -1, -3, 4, 7], [0, 1, 1, 1, 2, 4], [6, -3, -2, 1, 1, 1]])
        b = Matrix([[7], [16], [6]])
        c = Matrix([1, 2, 1, -1, 2, 3])
        true_result = 21
        solver = CuttingPlaneMethod(A, b, c)
        plan = solver.solve(True)
        result = (c.transpose() * plan)[0, 0]
        exp_plan = Matrix([5, 1, 11, 0, 0, 1])
        self.assertAlmostEquals(result, true_result)
        self.assertTrue(matrices_equal(plan, exp_plan, self.eps))

    def test_task6(self):
        A = Matrix([[0, 7, 1, -1, -4, 2, 4], [5, 1, 4, 3, -5, 2, 1], [2, 0, 3, 1, 0, 1, 5]])
        b = Matrix([[12], [27], [19]])
        c = Matrix([10, 2, 1, 7, 6, 3, 1])
        true_result = 157
        solver = CuttingPlaneMethod(A, b, c)
        plan = solver.solve(True)
        result = (c.transpose() * plan)[0, 0]
        exp_plan = Matrix([5, 6, 0, 8, 6, 1, 0])
        self.assertAlmostEquals(result, true_result)
        self.assertTrue(matrices_equal(plan, exp_plan, self.eps))

    def test_task7(self):
        A = Matrix([[0, 7, -8, -1, 5, 2, 1], [3, 2, 1, -3, -1, 1, 0], [1, 5, 3, -1, -2, 1, 0], [1, 1, 1, 1, 1, 1, 1]])
        b = Matrix([[6], [3], [7], [7]])
        c = Matrix([2, 9, 3, 5, 1, 2, 4])
        true_result = 26
        solver = CuttingPlaneMethod(A, b, c)
        plan = solver.solve(True)
        result = (c.transpose() * plan)[0, 0]
        exp_plan = Matrix([1, 1, 1, 1, 1, 1, 1])
        self.assertAlmostEquals(result, true_result)
        self.assertTrue(matrices_equal(plan, exp_plan, self.eps))

    @unittest.skip("too many constraint needed")
    def test_task8(self):
        A = Matrix([[1, 0, -1, 3, -2, 0, 1], [0, 2, 1, -1, 0, 3, -1], [1, 2, 1, 4, 2, 1, 1]])
        b = Matrix([[4], [8], [24]])
        c = Matrix([-1, -3, -7, 0, -4, 0, -1])
        true_result = -16
        solver = CuttingPlaneMethod(A, b, c)
        plan = solver.solve(True)
        result = (c.transpose() * plan)[0, 0]
        exp_plan = Matrix([1, 1, 0, 3, 3, 3, 0])
        self.assertAlmostEquals(result, true_result)
        self.assertTrue(matrices_equal(plan, exp_plan, self.eps))

    def test_task9(self):
        A = Matrix([[1, -3, 2, 0, 1, -1, 4, -1, 0], [1, -1, 6, 1, 0, -2, 2, 2, 0], [2, 2, -1, 1, 0, -3, 2, -1, 1],
                    [4, 1, 0, 0, 1, -1, 0, -1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]])
        b = Matrix([[3], [9], [9], [5], [9]])
        c = Matrix([-1, 5, -2, 4, 3, 1, 2, 8, 3])
        true_result = 25
        solver = CuttingPlaneMethod(A, b, c)
        plan = solver.solve(True)
        result = (c.transpose() * plan)[0, 0]
        exp_plan = Matrix([0, 1, 1, 2, 0, 0, 1, 0, 4])
        self.assertAlmostEquals(result, true_result)
        self.assertTrue(matrices_equal(plan, exp_plan, self.eps))


if __name__ == "__main__":
    unittest.main()
