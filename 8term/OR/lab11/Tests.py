import unittest
from sympy import Matrix
from TravellingSalesman import TravellingSalesman


class TestExamples(unittest.TestCase):
    def test_example1(self):
        costs = Matrix([[inf(), 2, 1, 10, 6],
                        [4, inf(), 3, 1, 3],
                        [2, 5, inf(), 8, 4],
                        [6, 7, 13, inf(), 3],
                        [10, 2, 4, 6, inf()]])
        true_result = 12
        result = TravellingSalesman(costs).solve()
        self.assertEquals(result, true_result)

    def test_example2(self):
        costs = Matrix([[inf(), 27, 43, 16, 30, 26],
                        [7, inf(), 16, 1, 30, 30],
                        [20, 13, inf(), 35, 5, 0],
                        [21, 16, 25, inf(), 18, 18],
                        [12, 46, 27, 48, inf(), 5],
                        [23, 5, 5, 9, 5, inf()]])
        true_result = 63
        result = TravellingSalesman(costs).solve()
        self.assertEquals(result, true_result)

    def test_task1(self):
        costs = Matrix([[inf(), 10, 25, 25, 10],
                        [1, inf(), 10, 15, 2],
                        [8, 9, inf(), 20, 10],
                        [14, 10, 24, inf(), 15],
                        [10, 8, 25, 27, inf()]])
        true_result = 62
        result = TravellingSalesman(costs).solve()
        self.assertEquals(result, true_result)

    def test_task2(self):
        costs = Matrix([[inf(), 10, 10, 8, 13, 1],
                        [3, inf(), 1, 17, 17, 7],
                        [1, 10, inf(), 6, 1, 17],
                        [6, 3, 2, inf(), 5, 12],
                        [8, 17, 8, 13, inf(), 11],
                        [11, 14, 12, 6, 11, inf()]])
        true_result = 20
        result = TravellingSalesman(costs).solve()
        self.assertEquals(result, true_result)

    def test_task3(self):
        costs = Matrix([[inf(), 8, 0, 1, 18, 16, 5],
                        [19, inf(), 12, 5, 11, 8, 17],
                        [10, 19, inf(), 17, 11, 15, 5],
                        [1, 8, 9, inf(), 11, 2, 2],
                        [11, 12, 14, 8, inf(), 4, 1],
                        [9, 3, 5, 17, 15, inf(), 19],
                        [13, 6, 15, 13, 18, 10, inf()]])
        true_result = 31
        result = TravellingSalesman(costs).solve()
        self.assertEquals(result, true_result)

    def test_task4(self):
        costs = Matrix([[inf(), 18, 13, 18, 8, 16, 11, 0],
                        [0, inf(), 1, 8, 2, 15, 19, 11],
                        [1, 10, inf(), 18, 5, 15, 12, 12],
                        [15, 16, 10, inf(), 16, 10, 6, 9],
                        [2, 18, 14, 16, inf(), 18, 13, 1],
                        [5, 19, 1, 19, 1, inf(), 7, 4],
                        [5, 7, 16, 0, 0, 8, inf(), 6],
                        [10, 8, 13, 10, 12, 3, 13, inf()]])
        true_result = 30
        result = TravellingSalesman(costs).solve()
        self.assertEquals(result, true_result)

    def test_task5(self):
        costs = Matrix([[inf(), 13, 2, 17, 14],
                        [11, inf(), 11, 8, 2],
                        [4, 10, inf(), 3, 6],
                        [9, 4, 6, inf(), 19],
                        [3, 7, 12, 18, inf()]])
        true_result = 14
        result = TravellingSalesman(costs).solve()
        self.assertEquals(result, true_result)

    def test_task6(self):
        costs = Matrix([[inf(), 6, 16, 16, 4, 12, 11, 1, 4, 10],
                        [1, inf(), 16, 9, 17, 5, 3, 2, 6, 19],
                        [19, 4, inf(), 11, 17, 8, 10, 4, 15, 11],
                        [7, 1, 17, inf(), 17, 2, 5, 6, 10, 17],
                        [8, 18, 18, 13, inf(), 0, 19, 6, 12, 14],
                        [3, 5, 13, 19, 16, inf(), 12, 17, 2, 19],
                        [1, 4, 1, 18, 2, 17, inf(), 8, 12, 10],
                        [6, 14, 19, 7, 19, 19, 10, inf(), 2, 9],
                        [2, 14, 18, 0, 16, 17, 13, 15, inf(), 1],
                        [1, 12, 2, 6, 19, 4, 13, 7, 0, inf()]])
        true_result = 25
        result = TravellingSalesman(costs).solve()
        self.assertEquals(result, true_result)

    def test_task7(self):
        costs = Matrix([[inf(), 12, 11, 1, 18, 4, 14, 3, 18],
                        [9, inf(), 14, 12, 7, 10, 4, 18, 9],
                        [7, 8, inf(), 18, 1, 6, 1, 9, 19],
                        [10, 18, 0, inf(), 3, 14, 3, 11, 4],
                        [7, 3, 17, 10, inf(), 14, 14, 9, 8],
                        [17, 16, 17, 16, 8, inf(), 9, 3, 19],
                        [13, 19, 8, 19, 12, 0, inf(), 13, 4],
                        [3, 3, 7, 6, 9, 15, 16, inf(), 15],
                        [5, 13, 15, 19, 6, 5, 5, 2, inf()]])
        true_result = 24
        result = TravellingSalesman(costs).solve()
        self.assertEquals(result, true_result)

    def test_task8(self):
        costs = Matrix([[inf(), 1, 14, 18, 11, 5, 13, 18, 17, 5, 11, ],
                        [4, inf(), 19, 14, 5, 3, 6, 15, 14, 15, 14, ],
                        [12, 6, inf(), 16, 19, 15, 6, 2, 12, 15, 8, ],
                        [14, 4, 18, inf(), 15, 0, 18, 13, 6, 2, 8, ],
                        [19, 15, 19, 14, inf(), 12, 9, 15, 3, 11, 16, ],
                        [10, 6, 11, 4, 15, inf(), 10, 9, 0, 9, 6, ],
                        [16, 0, 10, 17, 18, 6, inf(), 4, 4, 1, 0],
                        [7, 17, 17, 6, 7, 12, 10, inf(), 14, 9, 17],
                        [19, 5, 7, 6, 16, 4, 6, 17, inf(), 13, 14],
                        [2, 11, 11, 16, 12, 7, 14, 12, 15, inf(), 0],
                        [1, 14, 10, 0, 10, 3, 1, 0, 5, 6, inf()]])
        true_result = 32
        result = TravellingSalesman(costs).solve()
        self.assertEquals(result, true_result)

    def test_task9(self):
        costs = Matrix([[inf(), 8, 12, 7, 5, 0, 11, 5, 13, 9, 18, 1, ],
                        [10, inf(), 14, 4, 7, 4, 10, 10, 6, 6, 4, 3, ],
                        [4, 16, inf(), 13, 3, 2, 5, 5, 15, 7, 11, 19, ],
                        [3, 7, 11, inf(), 7, 6, 14, 3, 3, 8, 8, 18, ],
                        [11, 15, 18, 12, inf(), 19, 12, 13, 11, 16, 1, 12, ],
                        [8, 7, 16, 19, 1, inf(), 3, 16, 12, 11, 0, 5, ],
                        [5, 10, 8, 0, 17, 10, inf(), 6, 13, 1, 0, 6],
                        [6, 6, 6, 5, 1, 5, 17, inf(), 7, 14, 11, 5],
                        [19, 8, 4, 19, 13, 2, 5, 14, inf(), 12, 15, 16],
                        [11, 8, 8, 3, 4, 3, 4, 11, 2, inf(), 4, 15],
                        [9, 6, 12, 0, 18, 13, 14, 3, 12, 16, inf(), 4],
                        [18, 10, 8, 3, 18, 17, 16, 19, 7, 0, 12, inf()]])
        true_result = 27
        result = TravellingSalesman(costs).solve()
        self.assertEquals(result, true_result)

    def test_task10(self):
        costs = Matrix([[inf(), 10, 17, 15, 0, 15, 2, 16, 10, 2, 6, 19, 10],
                        [1, inf(), 9, 5, 13, 4, 13, 9, 18, 10, 14, 2, 9],
                        [7, 9, inf(), 12, 13, 12, 7, 7, 9, 15, 0, 3, 12],
                        [6, 1, 19, inf(), 9, 17, 4, 1, 0, 10, 10, 15, 18],
                        [13, 9, 9, 8, inf(), 2, 6, 4, 14, 2, 0, 17, 9],
                        [17, 10, 10, 13, 1, inf(), 14, 8, 14, 17, 14, 14, 2],
                        [17, 18, 3, 2, 6, 0, inf(), 19, 14, 3, 13, 3, 13],
                        [0, 4, 1, 9, 6, 6, 16, inf(), 3, 19, 8, 15, 4],
                        [15, 7, 5, 14, 6, 10, 1, 4, inf(), 4, 16, 17, 19],
                        [1, 9, 18, 7, 16, 16, 1, 19, 16, inf(), 1, 6, 12],
                        [7, 6, 7, 13, 8, 18, 10, 5, 19, 9, inf(), 5, 10],
                        [10, 16, 10, 5, 2, 5, 9, 13, 6, 7, 9, inf(), 7],
                        [18, 19, 4, 14, 13, 12, 7, 11, 8, 11, 12, 13, inf()]])
        true_result = 26
        result = TravellingSalesman(costs).solve()
        self.assertEquals(result, true_result)


def inf():
    return float('inf')


if __name__ == "__main__":
    unittest.main()
