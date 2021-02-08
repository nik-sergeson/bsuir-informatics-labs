import unittest

from ShortestPath import ShortestPath
from sympy import Matrix, ones
from lab1.MatricesHelper import matrices_equal


class TestExamples(unittest.TestCase):
    def test_task1(self):
        paths = Matrix([[0, 9, inf(), 3, inf(), inf(), inf(), inf()],
                        [9, 0, 2, inf(), 7, inf(), inf(), inf()],
                        [inf(), 2, 0, 2, 4, 8, 6, inf()],
                        [3, inf(), 2, 0, inf(), inf(), 5, inf()],
                        [inf(), 7, 4, inf(), 0, 10, inf(), inf()],
                        [inf(), inf(), 8, inf(), 10, 0, 7, inf()],
                        [inf(), inf(), 6, 5, inf(), 7, 0, inf()],
                        [inf(), inf(), inf(), inf(), 9, 12, 10, 0]])
        true_result = Matrix([[0, 7, 5, 3, 9, 13, 8, inf()],
                              [7, 0, 2, 4, 6, 10, 8, inf()],
                              [5, 2, 0, 2, 4, 8, 6, inf()],
                              [3, 4, 2, 0, 6, 10, 5, inf()],
                              [9, 6, 4, 6, 0, 10, 10, inf()],
                              [13, 10, 8, 10, 10, 0, 7, inf()],
                              [8, 8, 6, 5, 10, 7, 0, inf()],
                              [18, 15, 13, 15, 9, 12, 10, 0]])
        true_next = Matrix([[1, 4, 4, 4, 4, 4, 4, 8],
                            [3, 2, 3, 3, 3, 3, 3, 8],
                            [4, 2, 3, 4, 5, 6, 7, 8],
                            [1, 3, 3, 4, 3, 3, 7, 8],
                            [3, 3, 3, 3, 5, 6, 3, 8],
                            [3, 3, 3, 3, 5, 6, 7, 8],
                            [4, 3, 3, 4, 3, 6, 7, 8],
                            [5, 5, 5, 5, 5, 6, 7, 8]])
        result, next = ShortestPath(paths).solve()
        self.assertTrue(matrices_equal(result, true_result))
        self.assertTrue(matrices_equal(next, true_next - ones(*true_next.shape)))

    def test_task2(self):
        paths = Matrix([[0, 3, 2, 6, inf(), inf(), inf(), inf(), inf()],
                        [inf(), 0, inf(), 2, inf(), inf(), inf(), inf(), inf()],
                        [inf(), inf(), 0, inf(), inf(), 4, inf(), inf(), inf()],
                        [inf(), inf(), 3, 0, 1, inf(), 6, inf(), inf()],
                        [inf(), inf(), inf(), inf(), 0, inf(), 7, 5, inf()],
                        [inf(), inf(), inf(), inf(), 5, 0, inf(), 4, inf()],
                        [inf(), inf(), inf(), inf(), inf(), inf(), 0, 2, 4],
                        [inf(), inf(), inf(), inf(), inf(), inf(), inf(), 0, 4],
                        [inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), 0]])
        true_result = Matrix([[0, 3, 2, 5, 6, 6, 11, 10, 14],
                              [inf(), 0, 5, 2, 3, 9, 8, 8, 12],
                              [inf(), inf(), 0, inf(), 9, 4, 16, 8, 12],
                              [inf(), inf(), 3, 0, 1, 7, 6, 6, 10],
                              [inf(), inf(), inf(), inf(), 0, inf(), 7, 5, 9],
                              [inf(), inf(), inf(), inf(), 5, 0, 12, 4, 8],
                              [inf(), inf(), inf(), inf(), inf(), inf(), 0, 2, 4],
                              [inf(), inf(), inf(), inf(), inf(), inf(), inf(), 0, 4],
                              [inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), 0]])
        true_next = Matrix([[1, 2, 3, 2, 2, 3, 2, 3, 3],
                            [1, 2, 4, 4, 4, 4, 4, 4, 4],
                            [1, 2, 3, 4, 6, 6, 6, 6, 6],
                            [1, 2, 3, 4, 5, 3, 7, 5, 7],
                            [1, 2, 3, 4, 5, 6, 7, 8, 8],
                            [1, 2, 3, 4, 5, 6, 5, 8, 8],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9]])
        result, next = ShortestPath(paths).solve()
        self.assertTrue(matrices_equal(result, true_result))
        self.assertTrue(matrices_equal(next, true_next - ones(*true_next.shape)))

    def test_task3(self):
        paths = Matrix([[0, 3, 2, 6, inf(), inf(), inf(), inf(), inf()],
                        [inf(), 0, inf(), 2, inf(), inf(), inf(), inf(), inf()],
                        [inf(), inf(), 0, inf(), inf(), 4, inf(), inf(), inf()],
                        [inf(), inf(), 3, 0, 1, inf(), 6, inf(), inf()],
                        [inf(), inf(), inf(), inf(), 0, inf(), 7, 5, inf()],
                        [inf(), inf(), inf(), inf(), 5, 0, inf(), 4, inf()],
                        [inf(), inf(), inf(), inf(), inf(), inf(), 0, 2, 4],
                        [inf(), inf(), inf(), inf(), inf(), inf(), inf(), 0, 15],
                        [inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), 0]])
        true_result = Matrix([[0, 3, 2, 5, 6, 6, 11, 10, 15],
                              [inf(), 0, 5, 2, 3, 9, 8, 8, 12],
                              [inf(), inf(), 0, inf(), 9, 4, 16, 8, 20],
                              [inf(), inf(), 3, 0, 1, 7, 6, 6, 10],
                              [inf(), inf(), inf(), inf(), 0, inf(), 7, 5, 11],
                              [inf(), inf(), inf(), inf(), 5, 0, 12, 4, 16],
                              [inf(), inf(), inf(), inf(), inf(), inf(), 0, 2, 4],
                              [inf(), inf(), inf(), inf(), inf(), inf(), inf(), 0, 15],
                              [inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), 0]])
        true_next = Matrix([[1, 2, 3, 2, 2, 3, 2, 3, 2],
                            [1, 2, 4, 4, 4, 4, 4, 4, 4],
                            [1, 2, 3, 4, 6, 6, 6, 6, 6],
                            [1, 2, 3, 4, 5, 3, 7, 5, 7],
                            [1, 2, 3, 4, 5, 6, 7, 8, 7],
                            [1, 2, 3, 4, 5, 6, 5, 8, 5],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9]])
        result, next = ShortestPath(paths).solve()
        self.assertTrue(matrices_equal(result, true_result))
        self.assertTrue(matrices_equal(next, true_next - ones(*true_next.shape)))

    def test_task4(self):
        paths = Matrix([[0, 3, 4, inf(), 5, inf(), inf(), inf()],
                        [inf(), 0, 2, 1, inf(), inf(), 4, inf()],
                        [inf(), inf(), 0, 3, 2, inf(), inf(), inf()],
                        [inf(), inf(), inf(), 0, inf(), inf(), 3, inf()],
                        [inf(), inf(), inf(), 4, 0, 8, inf(), 3],
                        [inf(), inf(), inf(), 5, inf(), 0, inf(), 2],
                        [inf(), inf(), inf(), inf(), inf(), 2, 0, 1],
                        [inf(), inf(), inf(), inf(), inf(), inf(), inf(), 0]])
        true_result = Matrix([[0, 3, 4, 4, 5, 9, 7, 8],
                              [inf(), 0, 2, 1, 4, 6, 4, 5],
                              [inf(), inf(), 0, 3, 2, 8, 6, 5],
                              [inf(), inf(), inf(), 0, inf(), 5, 3, 4],
                              [inf(), inf(), inf(), 4, 0, 8, 7, 3],
                              [inf(), inf(), inf(), 5, inf(), 0, 8, 2],
                              [inf(), inf(), inf(), 7, inf(), 2, 0, 1],
                              [inf(), inf(), inf(), inf(), inf(), inf(), inf(), 0]])
        true_next = Matrix([[1, 2, 3, 2, 5, 2, 2, 5],
                            [1, 2, 3, 4, 3, 7, 7, 7],
                            [1, 2, 3, 4, 5, 4, 4, 5],
                            [1, 2, 3, 4, 5, 7, 7, 7],
                            [1, 2, 3, 4, 5, 6, 4, 8],
                            [1, 2, 3, 4, 5, 6, 4, 8],
                            [1, 2, 3, 6, 5, 6, 7, 8],
                            [1, 2, 3, 4, 5, 6, 7, 8]])
        result, next = ShortestPath(paths).solve()
        self.assertTrue(matrices_equal(result, true_result))
        self.assertTrue(matrices_equal(next, true_next - ones(*true_next.shape)))

    def test_task5(self):
        paths = Matrix([[0, 3, 4, inf(), 5, inf(), inf(), inf()],
                        [inf(), 0, inf(), 1, inf(), inf(), 4, inf()],
                        [inf(), inf(), 0, 3, 2, inf(), inf(), inf()],
                        [inf(), inf(), inf(), 0, inf(), inf(), 1, inf()],
                        [inf(), inf(), inf(), 4, 0, 8, inf(), 3],
                        [inf(), inf(), inf(), 5, inf(), 0, inf(), 2],
                        [inf(), inf(), inf(), inf(), inf(), 2, 0, 1],
                        [inf(), inf(), inf(), inf(), inf(), inf(), inf(), 0]])
        true_result = Matrix([[0, 3, 4, 4, 5, 7, 5, 6],
                              [inf(), 0, inf(), 1, inf(), 4, 2, 3],
                              [inf(), inf(), 0, 3, 2, 6, 4, 5],
                              [inf(), inf(), inf(), 0, inf(), 3, 1, 2],
                              [inf(), inf(), inf(), 4, 0, 7, 5, 3],
                              [inf(), inf(), inf(), 5, inf(), 0, 6, 2],
                              [inf(), inf(), inf(), 7, inf(), 2, 0, 1],
                              [inf(), inf(), inf(), inf(), inf(), inf(), inf(), 0]])
        true_next = Matrix([[1, 2, 3, 2, 5, 2, 2, 2],
                            [1, 2, 3, 4, 5, 4, 4, 4],
                            [1, 2, 3, 4, 5, 4, 4, 5],
                            [1, 2, 3, 4, 5, 7, 7, 7],
                            [1, 2, 3, 4, 5, 4, 4, 8],
                            [1, 2, 3, 4, 5, 6, 4, 8],
                            [1, 2, 3, 6, 5, 6, 7, 8],
                            [1, 2, 3, 4, 5, 6, 7, 8]])
        result, next = ShortestPath(paths).solve()
        self.assertTrue(matrices_equal(result, true_result))
        self.assertTrue(matrices_equal(next, true_next - ones(*true_next.shape)))

    def test_task6(self):
        paths = Matrix([[0, 6, 1, 5, inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf()],
                        [inf(), 0, 4, inf(), 2, 3, inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf()],
                        [inf(), inf(), 0, 2, inf(), inf(), 5, inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf()],
                        [inf(), inf(), inf(), 0, inf(), inf(), 6, 6, inf(), inf(), inf(), inf(), inf(), inf(), inf()],
                        [inf(), inf(), inf(), inf(), 0, inf(), inf(), inf(), 10, inf(), inf(), inf(), inf(), inf(),
                         inf()],
                        [inf(), inf(), inf(), inf(), 4, 0, inf(), inf(), inf(), 7, inf(), inf(), inf(), inf(), inf()],
                        [inf(), inf(), inf(), inf(), inf(), 20, 0, inf(), inf(), 10, 5, inf(), inf(), inf(), inf()],
                        [inf(), inf(), inf(), inf(), inf(), inf(), 2, 0, inf(), inf(), 3, 4, inf(), inf(), inf()],
                        [inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), 0, 1, inf(), inf(), 3, inf(), inf()],
                        [inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), 0, inf(), inf(), 2, inf(),
                         inf()],
                        [inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), 8, 0, inf(), inf(), 2, inf()],
                        [inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), 0, inf(), 1,
                         inf()],
                        [inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), 0, 3, 4],
                        [inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), 0,
                         5],
                        [inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(),
                         inf(), 0]])
        true_result = Matrix([[0, 6, 1, 3, 8, 9, 6, 9, 18, 16, 11, 13, 18, 13, 18],
                              [inf(), 0, 4, 6, 2, 3, 9, 12, 12, 10, 14, 16, 12, 15, 16],
                              [inf(), inf(), 0, 2, 29, 25, 5, 8, 39, 15, 10, 12, 17, 12, 17],
                              [inf(), inf(), inf(), 0, 30, 26, 6, 6, 40, 16, 9, 10, 18, 11, 16],
                              [inf(), inf(), inf(), inf(), 0, inf(), inf(), inf(), 10, 11, inf(), inf(), 13, 16, 17],
                              [inf(), inf(), inf(), inf(), 4, 0, inf(), inf(), 14, 7, inf(), inf(), 9, 12, 13],
                              [inf(), inf(), inf(), inf(), 24, 20, 0, inf(), 34, 10, 5, inf(), 12, 7, 12],
                              [inf(), inf(), inf(), inf(), 26, 22, 2, 0, 36, 11, 3, 4, 13, 5, 10],
                              [inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), 0, 1, inf(), inf(), 3, 6, 7],
                              [inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), 0, inf(), inf(), 2, 5, 6],
                              [inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), 8, 0, inf(), 10, 2, 7],
                              [inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), 0, inf(), 1,
                               6],
                              [inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), 0, 3,
                               4],
                              [inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(),
                               inf(), 0,
                               5],
                              [inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(),
                               inf(),
                               inf(), 0]])
        true_next = Matrix([[1, 2, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2, 3, 3],
                            [1, 2, 3, 3, 5, 6, 3, 3, 5, 6, 3, 3, 6, 6, 6],
                            [1, 2, 3, 4, 7, 7, 7, 4, 7, 7, 7, 4, 7, 7, 7],
                            [1, 2, 3, 4, 7, 7, 7, 8, 7, 7, 8, 8, 7, 8, 8],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 11, 12, 9, 9, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 5, 10, 11, 12, 10, 10, 10],
                            [1, 2, 3, 4, 6, 6, 7, 8, 6, 10, 11, 12, 10, 11, 11],
                            [1, 2, 3, 4, 7, 7, 7, 8, 7, 11, 11, 12, 11, 11, 11],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 13, 13],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 13, 13],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 10, 14, 14],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 14],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]])
        result, next = ShortestPath(paths).solve()
        self.assertTrue(matrices_equal(result, true_result))
        self.assertTrue(matrices_equal(next, true_next - ones(*true_next.shape)))

    def test_task7(self):
        paths = Matrix([[0, 2, inf(), inf(), 5, inf(), inf(), 7, inf(), inf(), 3, inf(), inf(), inf()],
                        [inf(), 0, 3, inf(), 4, inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf()],
                        [inf(), inf(), 0, 7, inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf()],
                        [inf(), inf(), inf(), 0, inf(), inf(), 9, inf(), inf(), inf(), inf(), inf(), inf(), 3],
                        [inf(), inf(), 1, inf(), 0, 2, inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf()],
                        [inf(), inf(), 5, 8, inf(), 0, inf(), inf(), 2, 3, inf(), inf(), inf(), inf()],
                        [inf(), inf(), inf(), inf(), inf(), inf(), 0, inf(), inf(), inf(), inf(), inf(), inf(), 5],
                        [inf(), inf(), inf(), inf(), inf(), 1, inf(), 0, inf(), inf(), 4, 2, inf(), inf()],
                        [inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), 0, inf(), inf(), 7, 1, inf()],
                        [inf(), inf(), inf(), inf(), inf(), inf(), 4, inf(), inf(), 0, inf(), inf(), inf(), 2],
                        [inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), 0, 6, inf(), inf()],
                        [inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), 0, 4, inf()],
                        [inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), 3, inf(), inf(), 0, 4],
                        [inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), 0]])
        true_result = Matrix([[0, 2, 5, 12, 5, 7, 14, 7, 9, 10, 3, 9, 10, 12],
                              [inf(), 0, 3, 10, 4, 6, 13, inf(), 8, 9, inf(), 15, 9, 11],
                              [inf(), inf(), 0, 7, inf(), inf(), 16, inf(), inf(), inf(), inf(), inf(), inf(), 10],
                              [inf(), inf(), inf(), 0, inf(), inf(), 9, inf(), inf(), inf(), inf(), inf(), inf(), 3],
                              [inf(), inf(), 1, 8, 0, 2, 9, inf(), 4, 5, inf(), 11, 5, 7],
                              [inf(), inf(), 5, 8, inf(), 0, 7, inf(), 2, 3, inf(), 9, 3, 5],
                              [inf(), inf(), inf(), inf(), inf(), inf(), 0, inf(), inf(), inf(), inf(), inf(), inf(),
                               5],
                              [inf(), inf(), 6, 9, inf(), 1, 8, 0, 3, 4, 4, 2, 4, 6],
                              [inf(), inf(), inf(), inf(), inf(), inf(), 8, inf(), 0, 4, inf(), 7, 1, 5],
                              [inf(), inf(), inf(), inf(), inf(), inf(), 4, inf(), inf(), 0, inf(), inf(), inf(), 2],
                              [inf(), inf(), inf(), inf(), inf(), inf(), 17, inf(), inf(), 13, 0, 6, 10, 14],
                              [inf(), inf(), inf(), inf(), inf(), inf(), 11, inf(), inf(), 7, inf(), 0, 4, 8],
                              [inf(), inf(), inf(), inf(), inf(), inf(), 7, inf(), inf(), 3, inf(), inf(), 0, 4],
                              [inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(), inf(),
                               inf(), 0]])
        true_next = Matrix([[1, 2, 2, 2, 5, 5, 5, 8, 5, 5, 11, 8, 5, 5],
                            [1, 2, 3, 3, 5, 5, 5, 8, 5, 5, 11, 5, 5, 5],
                            [1, 2, 3, 4, 5, 6, 4, 8, 9, 10, 11, 12, 13, 4],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
                            [1, 2, 3, 3, 5, 6, 6, 8, 6, 6, 11, 6, 6, 6],
                            [1, 2, 3, 4, 5, 6, 10, 8, 9, 10, 11, 9, 9, 10],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
                            [1, 2, 6, 6, 5, 6, 6, 8, 6, 6, 11, 12, 6, 6],
                            [1, 2, 3, 4, 5, 6, 13, 8, 9, 13, 11, 12, 13, 13],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
                            [1, 2, 3, 4, 5, 6, 12, 8, 9, 12, 11, 12, 12, 12],
                            [1, 2, 3, 4, 5, 6, 13, 8, 9, 13, 11, 12, 13, 13],
                            [1, 2, 3, 4, 5, 6, 10, 8, 9, 10, 11, 12, 13, 14],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]])
        result, next = ShortestPath(paths).solve()
        self.assertTrue(matrices_equal(result, true_result))
        self.assertTrue(matrices_equal(next, true_next - ones(*true_next.shape)))


def inf():
    return float('inf')


if __name__ == "__main__":
    unittest.main()
