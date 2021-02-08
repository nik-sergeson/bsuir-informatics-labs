__author__ = 'nik'
import unittest
from sympy import Matrix
from Network import Network
from MinCostFlow import MinCostFlow, get_flow_cost


class TestExamples(unittest.TestCase):
    def test_example(self):
        paths = Matrix([[0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 3],
                        [0, 3, 0, 5, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 4, 1, 0, 0],
                        [-2, 0, 3, 0, 4, 0]])
        a = Matrix([1, -4, -5, -6, 5, 9])
        u = {(0, 1): 1, (2, 1): 3, (5, 2): 9, (2, 3): 1, (4, 3): 5}
        true_result = 23
        network = Network(paths, a)
        solver = MinCostFlow(network)
        U, flow = solver.solve(u)
        result = get_flow_cost(U, flow, network)
        self.assertEquals(result, true_result)

    def test_task1(self):
        paths = Matrix([[0, 9, 0, 0, 0, 0, 0, 5, 0],
                        [0, 0, 1, 0, 0, 3, 5, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, -2],
                        [0, 0, -3, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 6, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 8, 0, 0, 0, 0],
                        [0, 0, -1, 4, 7, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 2, 0, 2],
                        [0, 0, 0, 0, 0, 6, 0, 0, 0]])
        a = Matrix([9, 5, -4, -3, -6, 2, 2, -7, 2])
        u = {(0, 1): 2, (0, 7): 7, (1, 6): 3, (1, 2): 4, (4, 3): 3, (5, 4): 4, (6, 4): 5, (8, 5): 2}
        true_result = 127
        network = Network(paths, a)
        solver = MinCostFlow(network)
        U, flow = solver.solve(u)
        result = get_flow_cost(U, flow, network)
        self.assertEquals(result, true_result)

    def test_task2(self):
        paths = Matrix([[0, 8, 0, 0, 0, 0, 0, 3],
                        [0, 0, 2, 0, 0, 0, 9, 0],
                        [0, 0, 0, 0, 0, 4, 0, 0],
                        [0, 0, -2, 0, 0, 1, 0, 0],
                        [0, 0, 0, 8, 0, 0, 0, 0],
                        [0, 0, 0, 0, 4, 0, 0, 0],
                        [0, 0, 11, 0, 6, 2, 0, 0],
                        [0, 0, 0, 0, 0, 5, 5, 0]])
        a = Matrix([5, -5, -1, -6, -1, -6, 3, 11])
        u = {(0, 1): 5, (0, 7): 0, (4, 3): 6, (6, 2): 1, (6, 4): 7, (7, 5): 6, (7, 6): 5}
        true_result = 186
        network = Network(paths, a)
        solver = MinCostFlow(network)
        U, flow = solver.solve(u)
        result = get_flow_cost(U, flow, network)
        self.assertEquals(result, true_result)

    def test_task3(self):
        paths = Matrix([[0, 8, 0, 0, 0, 0, 0, 3],
                        [0, 0, 2, 0, 0, 0, 9, 0],
                        [0, 0, 0, 0, 0, 4, 0, 0],
                        [0, 0, -2, 0, 0, 0, 0, 0],
                        [0, 0, 0, -3, 0, 0, 0, 0],
                        [0, 0, 0, 0, 8, 0, 0, 0],
                        [0, 0, 13, 1, 1, 7, 0, 0],
                        [0, 0, 0, 0, 0, -1, 1, 0]])
        a = Matrix([9, -2, -4, -6, -1, 4, 4, -4])
        u = {(0, 1): 5, (0, 7): 4, (1, 6): 3, (4, 3): 6, (5, 4): 7, (6, 2): 4, (6, 5): 3}
        true_result = 41
        network = Network(paths, a)
        solver = MinCostFlow(network)
        U, flow = solver.solve(u)
        result = get_flow_cost(U, flow, network)
        self.assertEquals(result, true_result)

    def test_task4(self):
        paths = Matrix([[0, 1, 0, 0, 0, 0, 4],
                        [0, 0, 5, 0, 3, 0, 0],
                        [0, 0, 0, 3, 0, 2, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 10, 5, 0, 2, 0],
                        [0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 8, 6, 0]])
        a = Matrix([3, 2, -6, -7, 9, -5, 4])
        u = {(0, 6): 3, (1, 2): 2, (4, 2): 4, (4, 3): 7, (6, 4): 2, (6, 5): 5}
        true_result = 85
        network = Network(paths, a)
        solver = MinCostFlow(network)
        U, flow = solver.solve(u)
        result = get_flow_cost(U, flow, network)
        self.assertEquals(result, true_result)

    def test_task5(self):
        paths = Matrix([[0, 3, 0, 0, 5, 4, 2],
                        [0, 0, 5, 0, -1, 0, 7],
                        [0, 0, 0, 6, 0, 0, 1],
                        [0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 2, -2, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 7],
                        [0, 0, 0, 0, 0, 0, 0]])
        a = Matrix([6, 4, -1, -2, -2, 1, -6])
        u = {(0, 4): 2, (0, 5): 4, (1, 2): 3, (1, 6): 1, (2, 3): 2, (5, 6): 5}
        true_result = 13
        network = Network(paths, a)
        solver = MinCostFlow(network)
        U, flow = solver.solve(u)
        result = get_flow_cost(U, flow, network)
        self.assertEquals(result, true_result)

    def test_task6(self):
        paths = Matrix([[0, 6, 0, 0, 0, 2, -2, 0],
                        [0, 0, 3, 6, 0, 1, 0, 0],
                        [0, 0, 0, 0, 3, 4, 0, 0],
                        [0, 0, -1, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 0, 7],
                        [0, 0, 0, 0, 5, 0, 5, 3],
                        [0, 4, 0, 0, 2, 0, 0, 2],
                        [0, 0, 0, 0, 0, 0, 0, 0]])
        a = Matrix([2, -4, 6, -2, 2, 0, 1, -5])
        u = {(0, 1): 2, (1, 3): 2, (2, 5): 6, (4, 7): 5, (5, 4): 3, (5, 6): 3, (6, 1): 4}
        true_result = 94
        network = Network(paths, a)
        solver = MinCostFlow(network)
        U, flow = solver.solve(u)
        result = get_flow_cost(U, flow, network)
        self.assertEquals(result, true_result)

    def test_task7(self):
        paths = Matrix([[0, 7, 6, 0, 3, 0, 0],
                        [0, 0, 4, 0, 0, 3, 0],
                        [0, 0, 0, 6, 5, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 4, 0, -1, 0],
                        [0, 0, 0, 0, 0, 0, 4],
                        [2, 0, 0, 0, 7, 0, 0]])
        a = Matrix([5, -2, 5, -4, -9, 2, 3])
        u = {(0, 1): 2, (0, 2): 3, (2, 3): 4, (2, 4): 4, (5, 6): 2, (6, 4): 5}
        true_result = 85
        network = Network(paths, a)
        solver = MinCostFlow(network)
        U, flow = solver.solve(u)
        result = get_flow_cost(U, flow, network)
        self.assertEquals(result, true_result)

    def test_task8(self):
        paths = Matrix([[0, 5, 0, 0, 1, 5],
                        [0, 0, 0, 10, 0, 3],
                        [1, 3, 0, 6, 2, 0],
                        [0, 0, 0, 0, 3, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 2, 4, 0]])
        a = Matrix([6, 1, 1, -6, -3, 1])
        u = {(0, 1): 4, (0, 5): 2, (1, 3): 5, (2, 3): 1, (5, 4): 3}
        true_result = 37
        network = Network(paths, a)
        solver = MinCostFlow(network)
        U, flow = solver.solve(u)
        result = get_flow_cost(U, flow, network)
        self.assertEquals(result, true_result)


if __name__ == "__main__":
    unittest.main()
