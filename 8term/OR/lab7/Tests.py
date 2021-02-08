import unittest

from LongestPathTree import LongestPathTree
from sympy import Matrix


class TestExamples(unittest.TestCase):
    def test_example(self):
        paths = Matrix([[0, 2, 0, 1, 0, 0],
                        [0, 0, 2, 0, 7, 0],
                        [0, 0, 0, 0, 0, 8],
                        [0, 4, 4, 0, 1, 0],
                        [0, 0, 1, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0]])
        true_result = 21
        lpt = LongestPathTree(paths)
        result = lpt.solve()[0][-1, 0]
        self.assertEquals(result, true_result)

    def test_task1(self):
        paths = Matrix([[0, 5, 6, 4, 1, 0, 0, 0],
                        [0, 0, 4, 3, 2, 0, 0, 0],
                        [0, 0, 0, 0, 5, 0, 3, 0],
                        [0, 0, 0, 0, 0, 4, 7, 3],
                        [0, 0, 0, 0, 0, 0, 0, 4],
                        [0, 0, 0, 0, 0, 0, 2, 5],
                        [0, 0, 0, 0, 2, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0]])
        true_result = 21
        lpt = LongestPathTree(paths)
        result = lpt.solve()[0][-1, 0]
        self.assertEquals(result, true_result)

    def test_task2(self):
        paths = Matrix([[0, 3, 4, 5, 3, 0, 0],
                        [0, 0, 0, 2, 0, 0, 0],
                        [0, 0, 0, 6, 0, 3, 0],
                        [0, 0, 0, 0, 4, 1, 4],
                        [0, 0, 0, 0, 0, 2, 5],
                        [0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 0]])
        true_result = 19
        lpt = LongestPathTree(paths)
        result = lpt.solve()[0][-1, 0]
        self.assertEquals(result, true_result)

    def test_task3(self):
        paths = Matrix([[0, 4, 1, 3, 0, 2, 7, 0],
                        [0, 0, 1, 5, 0, 0, 0, 0],
                        [0, 0, 0, 4, 3, 5, 0, 0],
                        [0, 0, 0, 0, 2, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 3, 1],
                        [0, 0, 0, 4, 0, 0, 2, 7],
                        [0, 0, 0, 0, 0, 0, 0, 6],
                        [0, 0, 0, 0, 0, 0, 0, 0]])
        true_result = 25
        lpt = LongestPathTree(paths)
        result = lpt.solve()[0][-1, 0]
        self.assertEquals(result, true_result)

    def test_task4(self):
        paths = Matrix([[0, 3, 4, 6, 2, 0, 0, 0],
                        [0, 0, 0, 5, 1, 0, 0, 0],
                        [0, 3, 0, 2, 0, 6, 0, 0],
                        [0, 0, 0, 0, 4, 2, 7, 0],
                        [0, 0, 0, 0, 0, 3, 7, 1],
                        [0, 0, 0, 0, 0, 0, 1, 4],
                        [0, 0, 0, 0, 0, 0, 0, 6],
                        [0, 0, 0, 0, 0, 0, 0, 0]])
        true_result = 29
        lpt = LongestPathTree(paths)
        result = lpt.solve()[0][-1, 0]
        self.assertEquals(result, true_result)

    def test_task5(self):
        paths = Matrix([[0, 7, 9, 6, 0, 3, 0],
                        [0, 0, 0, 0, 0, 6, 0],
                        [0, 4, 0, 0, 3, 1, 4],
                        [0, 2, 1, 0, 8, 0, 0],
                        [0, 0, 0, 0, 0, 5, 1],
                        [0, 0, 0, 0, 0, 0, 3],
                        [0, 0, 0, 0, 0, 0, 0]])
        true_result = 22
        lpt = LongestPathTree(paths)
        result = lpt.solve()[0][-1, 0]
        self.assertEquals(result, true_result)

    def test_task6(self):
        paths = Matrix([[0, 6, 5, 0, 1, 4, 0, 0, 0],
                        [0, 0, 2, 0, 9, 3, 0, 0, 0],
                        [0, 0, 0, 10, 1, 0, 2, 0, 5],
                        [0, 0, 0, 0, 0, 0, 1, 7, 3],
                        [0, 0, 0, 7, 0, 6, 3, 0, 0],
                        [0, 0, 0, 5, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 8, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 2],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0]])
        true_result = 37
        lpt = LongestPathTree(paths)
        result = lpt.solve()[0][-1, 0]
        self.assertEquals(result, true_result)

    def test_task7(self):
        paths = Matrix([[0, 7, 0, 4, 4, 0, 0, 0, 0],
                        [0, 0, 2, 5, 0, 0, 0, 0, 0],
                        [0, 0, 0, 6, 0, 1, 0, 7, 0],
                        [0, 0, 0, 0, 7, 4, 0, 0, 0],
                        [0, 0, 0, 0, 0, 9, 3, 0, 0],
                        [0, 0, 0, 0, 0, 0, 10, 0, 5],
                        [0, 0, 0, 0, 0, 0, 0, 0, 8],
                        [0, 0, 0, 0, 0, 0, 0, 0, 3],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0]])
        true_result = 49
        lpt = LongestPathTree(paths)
        result = lpt.solve()[0][-1, 0]
        self.assertEquals(result, true_result)

    def test_task8(self):
        paths = Matrix([[0, 7, 2, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 9, 5, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 4, 3, 0, 0],
                        [0, 0, 4, 0, 3, 5, 0, 7, 0],
                        [0, 0, 0, 0, 0, 10, 0, 4, 0],
                        [0, 0, 0, 0, 0, 0, 7, 0, 4],
                        [0, 0, 0, 0, 0, 0, 0, 0, 6],
                        [0, 0, 0, 0, 0, 8, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0]])
        true_result = 44
        lpt = LongestPathTree(paths)
        result = lpt.solve()[0][-1, 0]
        self.assertEquals(result, true_result)


if __name__ == "__main__":
    unittest.main()
