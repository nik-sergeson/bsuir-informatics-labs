import unittest
from ResourceAllocator import ResourceAllocator
from lab1.MatricesHelper import matrices_equal
from sympy import Matrix


class TestExamples(unittest.TestCase):
    def test_example(self):
        profits = Matrix([[0, 3, 4, 5, 8, 9, 10],
                          [0, 2, 3, 7, 9, 12, 13],
                          [0, 1, 2, 6, 11, 11, 13]])
        result = 16
        distr = Matrix([1, 1, 4])
        solver = ResourceAllocator(profits)
        profit, plan = solver.solve()
        self.assertTrue(matrices_equal(plan, distr))
        self.assertEquals(profit, result)

    def test_task1(self):
        profits = Matrix([[0, 1, 2, 2, 4, 5, 6],
                          [0, 2, 3, 5, 7, 7, 8],
                          [0, 2, 4, 5, 6, 7, 7]])
        result = 11
        distr = Matrix([0, 4, 2])
        solver = ResourceAllocator(profits)
        profit, plan = solver.solve()
        self.assertTrue(matrices_equal(plan, distr))
        self.assertEquals(profit, result)

    def test_task2(self):
        profits = Matrix([[0, 1, 1, 3, 6, 10, 11],
                          [0, 2, 3, 5, 6, 7, 13],
                          [0, 1, 4, 4, 7, 8, 9]])
        result = 13
        distr = Matrix([0, 6, 0])
        solver = ResourceAllocator(profits)
        profit, plan = solver.solve()
        self.assertTrue(matrices_equal(plan, distr))
        self.assertEquals(profit, result)

    def test_task3(self):
        profits = Matrix([[0, 1, 2, 4, 8, 9, 9, 23],
                          [0, 2, 4, 6, 6, 8, 10, 11],
                          [0, 3, 4, 7, 7, 8, 8, 24]])
        result = 24
        distr = Matrix([0, 0, 7])
        solver = ResourceAllocator(profits)
        profit, plan = solver.solve()
        self.assertTrue(matrices_equal(plan, distr))
        self.assertEquals(profit, result)

    def test_task4(self):
        profits = Matrix([[0, 3, 3, 6, 7, 8, 9, 14],
                          [0, 2, 4, 4, 5, 6, 8, 13],
                          [0, 1, 1, 2, 3, 3, 10, 11]])
        result = 14
        distr = Matrix([7, 0, 0])
        solver = ResourceAllocator(profits)
        profit, plan = solver.solve()
        self.assertTrue(matrices_equal(plan, distr))
        self.assertEquals(profit, result)

    def test_task5(self):
        profits = Matrix([[0, 2, 2, 3, 5, 8, 8, 10, 17],
                          [0, 1, 2, 5, 8, 10, 11, 13, 15],
                          [0, 4, 4, 5, 6, 7, 13, 14, 14],
                          [0, 1, 3, 6, 9, 10, 11, 14, 16]])
        result = 18
        distr = Matrix([0, 4, 1, 3])
        solver = ResourceAllocator(profits)
        profit, plan = solver.solve()
        self.assertTrue(matrices_equal(plan, distr))
        self.assertEquals(profit, result)

    def test_task6(self):
        profits = Matrix([[0, 1, 3, 4, 5, 8, 9, 9, 11, 12, 12, 14],
                          [0, 1, 2, 3, 3, 3, 7, 12, 13, 14, 17, 19],
                          [0, 4, 4, 7, 7, 8, 12, 14, 14, 16, 18, 22],
                          [0, 5, 5, 5, 7, 9, 13, 13, 15, 15, 19, 24]])
        result = 24
        distr = Matrix([2, 7, 1, 1])
        solver = ResourceAllocator(profits)
        profit, plan = solver.solve()
        self.assertTrue(matrices_equal(plan, distr))
        self.assertEquals(profit, result)

    def test_task7(self):
        profits = Matrix([[0, 4, 4, 6, 9, 12, 12, 15, 16, 19, 19, 19],
                          [0, 1, 1, 1, 4, 7, 8, 8, 13, 13, 19, 20],
                          [0, 2, 5, 6, 7, 8, 9, 11, 11, 13, 13, 18],
                          [0, 1, 2, 4, 5, 7, 8, 8, 9, 9, 15, 19],
                          [0, 2, 5, 7, 8, 9, 10, 10, 11, 14, 17, 21]])
        result = 25
        distr = Matrix([7, 0, 2, 0, 2])
        solver = ResourceAllocator(profits)
        profit, plan = solver.solve()
        self.assertTrue(matrices_equal(plan, distr))
        self.assertEquals(profit, result)

    def test_task8(self):
        profits = Matrix([[0, 1, 2, 2, 2, 3, 5, 8, 9, 13, 14],
                          [0, 1, 3, 4, 5, 5, 7, 7, 10, 12, 12],
                          [0, 2, 2, 3, 4, 6, 6, 8, 9, 11, 17],
                          [0, 1, 1, 1, 2, 3, 9, 9, 11, 12, 15],
                          [0, 2, 7, 7, 7, 9, 9, 10, 11, 12, 13],
                          [0, 2, 5, 5, 5, 6, 6, 7, 12, 18, 22]])
        result = 22
        distr = Matrix([0, 0, 0, 0, 0, 10])
        solver = ResourceAllocator(profits)
        profit, plan = solver.solve()
        self.assertTrue(matrices_equal(plan, distr))
        self.assertEquals(profit, result)


if __name__ == "__main__":
    unittest.main()
