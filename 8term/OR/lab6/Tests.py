import unittest
from lab6.ShortestPathTree import ShortestPathTree
from lab1.MatricesHelper import matrices_equal
from sympy import Matrix


class TestExamples(unittest.TestCase):
    def test_example(self):
        paths = Matrix([[0, 12, 0, 0, 0, 1, 0],
                        [0, 0, 2, 0, 0, 0, 0],
                        [0, 0, 0, 1, 5, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 15, 0, 0, 2],
                        [0, 10, 0, 0, 5, 0, 8],
                        [0, 2, 6, 0, 0, 0, 0]])
        # 12 edges
        expected = Matrix([0, 10, 12, 13, 6, 1, 8])
        result, parents = ShortestPathTree(paths).solve()
        self.assertTrue(matrices_equal(result, expected))

    def test_task1(self):
        # 10
        paths = Matrix([[0, 5, 0, 0, 0, 0, 0, 3, 0, 0],
                        [0, 0, 2, 0, 0, 0, 3, 0, 0, 0],
                        [0, 0, 0, 0, 5, 0, 0, 0, 0, 0],
                        [0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 2],
                        [0, 0, 4, 0, 1, 0, 0, 6, 2, 0],
                        [2, 0, 2, 0, 0, 5, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 4, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
                        [0, 0, 0, 6, 0, 3, 0, 0, 0, 0]])
        # 21 edges
        expected = Matrix([0, 4, 6, 12, 11, 12, 7, 3, 4, 9])
        result, parents = ShortestPathTree(paths).solve()
        self.assertTrue(matrices_equal(result, expected))

    def test_task2(self):
        # 9
        paths = Matrix([[0, 6, 2, 0, 0, 0, 2, 0, 0],
                        [0, 0, 5, 0, 0, 6, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 2, 0, 3, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 4, 0],
                        [4, 0, 0, 0, 6, 0, 3, 7, 0],
                        [0, 0, 0, 0, 0, 0, 0, 4, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 1, 5, 2, 0, 0, 0]])
        # 19 edges
        expected = Matrix([0, 6, 2, 8, 9, 3, 2, 6, 7])
        result, parents = ShortestPathTree(paths).solve()
        self.assertTrue(matrices_equal(result, expected))

    def test_task3(self):
        # 8
        paths = Matrix([[0, 3, 0, 0, 0, 0, 4, 0],
                        [0, 0, 4, 0, 0, 8, 0, 6],
                        [0, 0, 0, 0, 6, 0, 0, 0],
                        [0, 0, 2, 0, 0, 0, 0, 0],
                        [0, 2, 0, 0, 0, 0, 2, 0],
                        [2, 0, 5, 1, 4, 0, 0, 2],
                        [0, 0, 0, 1, 0, 6, 0, 0],
                        [1, 0, 0, 0, 0, 0, 5, 0]])
        # 18 edges
        expected = Matrix([0, 3, 7, 5, 13, 10, 4, 9])
        result, parents = ShortestPathTree(paths).solve()
        self.assertTrue(matrices_equal(result, expected))

    def test_task4(self):
        # 8
        paths = Matrix([[0, 4, 3, 0, 0, 7, 2, 1],
                        [0, 0, 5, 0, 0, 0, 0, 1],
                        [0, 0, 0, 2, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 3, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 6, 0, 0, 0],
                        [0, 0, 4, 0, 7, 2, 0, 0],
                        [0, 0, 4, 3, 0, 0, 5, 0]])
        # 17 edges
        expected = Matrix([0, 4, 3, 4, 5, 4, 2, 1])
        result, parents = ShortestPathTree(paths).solve()
        self.assertTrue(matrices_equal(result, expected))

    def test_task5(self):
        # 7
        paths = Matrix([[0, 4, 0, 0, 0, 6, 0],
                        [0, 0, 7, 1, 0, 3, 0],
                        [0, 0, 0, 2, 5, 0, 0],
                        [2, 0, 0, 0, 6, 4, 0],
                        [0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 2, 0, 3],
                        [0, 7, 1, 3, 0, 0, 0]])
        # 16 edges
        expected = Matrix([0, 4, 10, 5, 8, 6, 9])
        result, parents = ShortestPathTree(paths).solve()
        self.assertTrue(matrices_equal(result, expected))

    def test_task6(self):
        # 8
        paths = Matrix([[0, 0, 4, 0, 0, 1, 5, 4],
                        [9, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 4, 2, 5, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 3, 0, 0, 0, 8],
                        [0, 2, 0, 0, 7, 0, 0, 3],
                        [0, 10, 0, 0, 0, 0, 0, 3],
                        [0, 0, 0, 6, 0, 0, 0, 0]])
        # 18 edges
        expected = Matrix([0, 3, 4, 8, 6, 1, 5, 4])
        result, parents = ShortestPathTree(paths).solve()
        self.assertTrue(matrices_equal(result, expected))

    def test_task7(self):
        # 9
        paths = Matrix([[0, 5, 0, 0, 0, 0, 4, 3, 0],
                        [0, 0, 6, 0, 0, 0, 11, 0, 0],
                        [0, 0, 0, 3, 1, 8, 0, 0, 6],
                        [0, 0, 0, 0, 0, 0, 0, 7, 0],
                        [0, 0, 0, 5, 0, 0, 0, 0, 0],
                        [6, 2, 0, 0, 5, 0, 0, 0, 0],
                        [0, 0, 2, 0, 0, 0, 0, 7, 0],
                        [0, 0, 0, 0, 3, 4, 0, 0, 4],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0]])
        # 20 edges
        expected = Matrix([0, 5, 6, 8, 6, 7, 4, 3, 7])
        result, parents = ShortestPathTree(paths).solve()
        self.assertTrue(matrices_equal(result, expected))

    def test_task8(self):
        # 8
        paths = Matrix([[0, 1, 0, 0, 0, 5, 6, 5],
                        [0, 0, 4, 4, 6, 0, 0, 0],
                        [0, 0, 0, 5, 7, 12, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 8],
                        [0, 0, 0, 3, 0, 0, 9, 1],
                        [0, 0, 0, 0, 4, 0, 3, 0],
                        [0, 2, 0, 0, 0, 0, 0, 0],
                        [0, 0, 2, 0, 0, 0, 2, 0]])
        # 19 edges
        expected = Matrix([0, 1, 5, 5, 7, 5, 6, 5])
        result, parents = ShortestPathTree(paths).solve()
        self.assertTrue(matrices_equal(result, expected))


if __name__ == "__main__":
    unittest.main()
