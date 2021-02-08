import unittest

from MaxFlow import MaxFlow
from sympy import Matrix


class TestExamples(unittest.TestCase):
    def test_example1(self):
        # 7
        paths = Matrix([[0, 4, 0, 9, 0, 0, 0],
                        [0, 0, 0, 2, 4, 0, 0],
                        [0, 0, 0, 0, 1, 10, 0],
                        [0, 0, 1, 0, 0, 6, 0],
                        [0, 0, 0, 0, 0, 1, 2],
                        [0, 0, 0, 0, 0, 0, 9],
                        [0, 0, 0, 0, 0, 0, 0]])
        # 11 edges
        true_result = 10
        result = MaxFlow(paths).solve()
        self.assertEquals(result, true_result)

    def test_example2(self):
        # 7
        paths = Matrix([[0, 12, 0, 0, 0, 6, 0],
                        [0, 0, 2, 0, 0, 0, 0],
                        [0, 0, 0, 0, 5, 0, 1],
                        [0, 2, 6, 0, 0, 0, 0],
                        [0, 0, 0, 2, 0, 0, 15],
                        [0, 10, 0, 8, 5, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0]])
        # 12 edges
        true_result = 8
        result = MaxFlow(paths).solve()
        self.assertEquals(result, true_result)

    def test_task1(self):
        # 8
        paths = Matrix([[0, 3, 2, 1, 0, 6, 0, 0],
                        [0, 0, 0, 1, 2, 0, 0, 0],
                        [0, 0, 0, 1, 2, 4, 0, 0],
                        [0, 0, 0, 0, 7, 5, 4, 1],
                        [0, 0, 0, 0, 0, 0, 3, 2],
                        [0, 0, 0, 0, 0, 0, 0, 4],
                        [0, 0, 0, 0, 0, 3, 0, 5],
                        [0, 0, 0, 0, 0, 0, 0, 0]])
        # 18 edges
        true_result = 10
        result = MaxFlow(paths).solve()
        self.assertEquals(result, true_result)

    def test_task2(self):
        # 9
        paths = Matrix([[0, 4, 1, 0, 1, 5, 2, 0, 0],
                        [0, 0, 0, 1, 0, 6, 0, 0, 0],
                        [0, 0, 0, 0, 2, 0, 0, 0, 0],
                        [0, 0, 6, 0, 0, 0, 3, 0, 0],
                        [0, 0, 0, 0, 0, 4, 0, 3, 0],
                        [0, 0, 0, 0, 0, 0, 1, 3, 6],
                        [0, 0, 0, 0, 0, 0, 0, 4, 5],
                        [0, 0, 0, 0, 0, 0, 0, 0, 4],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0]])
        # 18 edges
        true_result = 13
        result = MaxFlow(paths).solve()
        self.assertEquals(result, true_result)

    def test_task3(self):
        # 10
        paths = Matrix([[0, 2, 1, 0, 2, 0, 0, 0, 0, 0],
                        [0, 0, 0, 2, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 3, 2, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 2, 0, 0],
                        [0, 0, 0, 0, 0, 1, 4, 3, 3, 0],
                        [0, 0, 0, 0, 0, 0, 0, 2, 2, 0],
                        [0, 0, 0, 0, 0, 0, 0, 5, 0, 3],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 4],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
        # 20 edges
        true_result = 5
        result = MaxFlow(paths).solve()
        self.assertEquals(result, true_result)

    def test_task4(self):
        # 8
        paths = Matrix([[0, 3, 6, 3, 2, 0, 0, 0],
                        [0, 0, 4, 1, 4, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 3, 2],
                        [0, 0, 1, 0, 5, 0, 1, 2],
                        [0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 3, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 4],
                        [0, 0, 0, 0, 0, 0, 0, 0]])
        # 17 edges
        true_result = 8
        result = MaxFlow(paths).solve()
        self.assertEquals(result, true_result)

    def test_task5(self):
        # 9
        paths = Matrix([[0, 2, 5, 0, 3, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 4, 0, 0, 1, 0, 0, 3, 1],
                        [0, 0, 2, 0, 2, 4, 5, 0, 0],
                        [0, 4, 0, 0, 0, 4, 0, 0, 5],
                        [0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 4, 0],
                        [0, 0, 0, 0, 3, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 2, 0]])
        # 19 edges
        true_result = 6
        result = MaxFlow(paths).solve()
        self.assertEquals(result, true_result)

    def test_task6(self):
        # 8
        paths = Matrix([[0, 0, 0, 3, 6, 0, 0, 0],
                        [1, 0, 0, 4, 7, 0, 1, 0],
                        [5, 5, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 2, 2, 1, 3],
                        [0, 0, 0, 0, 0, 4, 3, 0],
                        [0, 0, 5, 0, 0, 0, 0, 2],
                        [0, 0, 0, 0, 0, 7, 0, 0],
                        [0, 0, 4, 0, 0, 0, 0, 0]])
        true_result = 5
        result = MaxFlow(paths).solve()
        self.assertEquals(result, true_result)

    def test_task7(self):
        # 9
        paths = Matrix([[0, 0, 0, 0, 4, 6, 2, 0, 0],
                        [3, 0, 2, 0, 7, 0, 4, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 3, 5, 0, 2, 0, 4, 0, 2],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 7],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 3, 6, 0, 0, 4, 0, 1],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0]])
        # 19 edges
        true_result = 7
        result = MaxFlow(paths).solve()
        self.assertEquals(result, true_result)

    def test_task8(self):
        # 10
        paths = Matrix([[0, 3, 3, 0, 0, 2, 1, 0, 0, 0],
                        [0, 0, 6, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 2, 4, 4, 0, 0, 0],
                        [0, 0, 0, 0, 7, 0, 0, 0, 0, 4],
                        [0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
                        [0, 0, 0, 4, 7, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
                        [2, 0, 0, 0, 0, 5, 6, 0, 2, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
        # 22 edges
        true_result = 9
        result = MaxFlow(paths).solve()
        self.assertEquals(result, true_result)


if __name__ == "__main__":
    unittest.main()
