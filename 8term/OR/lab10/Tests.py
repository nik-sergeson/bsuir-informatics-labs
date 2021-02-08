import unittest
from sympy import Matrix

from AssignmentProblem import AssignmentProblem


class TestExamples(unittest.TestCase):
    def test_example1(self):
        costs = Matrix([[2, -1, 9, 4],
                        [3, 2, 5, 1],
                        [13, 0, -3, 4],
                        [5, 6, 1, 2]])
        true_assignment = Matrix([1, 0, 2, 3])
        true_result = 1
        assignments = AssignmentProblem(costs).solve()
        result = AssignmentProblem.get_cost(costs, assignments)
        self.assertEquals(result, true_result)
        self.assertEquals(assignments, true_assignment)

    def test_task1(self):
        costs = Matrix([[6, 4, 13, 4, 19, 15, 11, 8],
                        [17, 15, 18, 14, 0, 7, 18, 7],
                        [3, 5, 11, 9, 7, 7, 18, 16],
                        [17, 10, 16, 19, 9, 6, 1, 5],
                        [14, 2, 10, 14, 11, 6, 4, 10],
                        [17, 11, 17, 12, 1, 10, 6, 19],
                        [13, 1, 4, 2, 2, 7, 2, 14],
                        [12, 15, 19, 11, 13, 1, 7, 8]])
        true_assignment = Matrix([3, 7, 0, 6, 1, 4, 2, 5])
        true_result = 23
        assignment = AssignmentProblem(costs).solve()
        result = AssignmentProblem.get_cost(costs, assignment)
        self.assertEquals(result, true_result)
        self.assertEquals(assignment, true_assignment)

    def test_task2(self):
        costs = Matrix([[9, 6, 4, 9, 3, 8, 0],
                        [5, 8, 6, 8, 8, 3, 5],
                        [5, 2, 1, 1, 8, 6, 8],
                        [1, 0, 9, 2, 5, 9, 2],
                        [9, 2, 3, 3, 0, 3, 0],
                        [7, 3, 0, 9, 4, 5, 6],
                        [0, 9, 6, 0, 8, 8, 9]])
        true_assignment = Matrix([6, 5, 3, 1, 4, 2, 0])
        true_result = 4
        assignment = AssignmentProblem(costs).solve()
        result = AssignmentProblem.get_cost(costs, assignment)
        self.assertEquals(result, true_result)
        self.assertEquals(assignment, true_assignment)

    def test_task3(self):
        costs = Matrix([[6, 6, 2, 4, 7, 1, 9, 4, 6],
                        [5, 0, 2, 4, 9, 2, 9, 2, 0],
                        [7, 6, 0, 5, 2, 3, 0, 5, 5],
                        [9, 5, 8, 9, 2, 3, 1, 5, 7],
                        [3, 1, 7, 3, 0, 2, 2, 8, 1],
                        [3, 0, 0, 6, 1, 7, 2, 4, 7],
                        [5, 6, 1, 9, 9, 8, 4, 1, 8],
                        [5, 4, 5, 2, 2, 6, 6, 5, 6],
                        [3, 6, 1, 6, 3, 0, 5, 2, 2]])
        true_assignment = Matrix([5, 8, 2, 6, 4, 1, 7, 3, 0])
        true_result = 8
        assignment = AssignmentProblem(costs).solve()
        result = AssignmentProblem.get_cost(costs, assignment)
        self.assertEquals(result, true_result)
        self.assertEquals(assignment, true_assignment)

    def test_task4(self):
        costs = Matrix([[6, 5, 6, 8, 4, 0, 4, 6],
                        [5, 7, 8, 7, 4, 4, 0, 9],
                        [0, 7, 9, 2, 8, 7, 0, 3],
                        [6, 6, 6, 3, 0, 3, 0, 8],
                        [7, 4, 7, 1, 1, 1, 8, 9],
                        [8, 0, 7, 5, 0, 9, 1, 3],
                        [3, 2, 4, 7, 1, 7, 3, 4],
                        [9, 2, 4, 3, 2, 4, 3, 9]])
        true_assignment = Matrix([5, 6, 0, 4, 3, 1, 7, 2])
        true_result = 9
        assignment = AssignmentProblem(costs).solve()
        result = AssignmentProblem.get_cost(costs, assignment)
        self.assertEquals(result, true_result)
        self.assertEquals(assignment, true_assignment)

    def test_task5(self):
        costs = Matrix([[7, 4, 5, 3, 8, 9, 6, 5, 5, 3, 2],
                        [5, 6, 9, 4, 9, 0, 0, 4, 4, 7, 2],
                        [8, 8, 3, 2, 7, 3, 7, 6, 7, 4, 6],
                        [7, 4, 9, 9, 3, 7, 3, 8, 1, 5, 8],
                        [5, 2, 4, 3, 3, 9, 6, 2, 5, 1, 3],
                        [9, 4, 5, 8, 6, 3, 3, 1, 7, 6, 5],
                        [9, 1, 0, 3, 1, 2, 7, 6, 9, 4, 6],
                        [5, 6, 8, 0, 9, 9, 1, 9, 3, 0, 8],
                        [4, 6, 5, 6, 4, 7, 5, 3, 8, 0, 1],
                        [2, 3, 7, 8, 4, 9, 5, 0, 2, 8, 0],
                        [7, 6, 7, 1, 9, 5, 7, 4, 2, 3, 0]])
        true_assignment = Matrix([[10], [5], [2], [8], [1], [7], [4], [6], [9], [0], [3]])
        true_result = 14
        assignment = AssignmentProblem(costs).solve()
        result = AssignmentProblem.get_cost(costs, assignment)
        self.assertEquals(result, true_result)
        self.assertEquals(assignment, true_assignment)

    def test_task6(self):
        costs = Matrix([[7, -4, 5, 3, 8, 9, 6, 5],
                        [5, 6, 9, 4, 9, 0, 0, 4],
                        [8, 8, 3, -2, 7, -3, 7, 6],
                        [7, 4, 9, 9, 3, 7, 3, 8],
                        [5, 2, 4, 3, 3, 9, 6, 2],
                        [9, 4, 5, 8, 6, 3, 3, 1],
                        [9, 1, 0, -3, 1, 2, 7, 6],
                        [5, 6, 8, 0, 9, 9, 1, 9]])
        true_assignment = Matrix([1, 6, 5, 4, 0, 7, 2, 3])
        true_result = 2
        assignment = AssignmentProblem(costs).solve()
        result = AssignmentProblem.get_cost(costs, assignment)
        self.assertEquals(result, true_result)
        self.assertEquals(assignment, true_assignment)

    def test_task7(self):
        costs = Matrix([[2, 6, 5, -1, 6, 1, 8, 4, 6],
                        [2, 1, 2, 7, 9, -2, 8, 2, 0],
                        [0, 6, 0, 5, 1, 3, 4, 3, 5],
                        [7, 0, 8, 9, 2, 4, 1, 6, 7],
                        [-1, 1, 0, -3, 0, 2, 2, 2, 1],
                        [3, 0, 6, 6, 1, -2, 2, 4, 0],
                        [1, 7, 1, 9, 4, 8, 2, 6, 8],
                        [5, 1, 5, 2, 2, 6, -1, 5, 4],
                        [3, 6, 0, 6, 3, 0, 9, 1, 2]])
        true_assignment = Matrix([[3], [8], [2], [1], [4], [5], [0], [6], [7]])
        true_result = -2
        assignment = AssignmentProblem(costs).solve()
        result = AssignmentProblem.get_cost(costs, assignment)
        self.assertEquals(result, true_result)
        self.assertEquals(assignment, true_assignment)

    def test_task8(self):
        costs = Matrix([[2, 4, 0, 3, 8, -1, 6, 5],
                        [8, 6, 3, 4, 2, 0, 0, 4],
                        [8, -4, 3, 2, 7, 3, 1, 0],
                        [2, 4, 9, 5, 3, 0, 3, 8],
                        [5, 2, 7, 3, -1, 0, 3, 2],
                        [3, 2, 5, 1, 5, 3, 0, 1],
                        [2, 1, 0, -3, 1, 2, 7, 0],
                        [1, 6, 4, 0, 0, 9, 1, 7]])
        true_assignment = Matrix([2, 6, 1, 5, 4, 7, 3, 0])
        true_result = -6
        assignment = AssignmentProblem(costs).solve()
        result = AssignmentProblem.get_cost(costs, assignment)
        self.assertEquals(result, true_result)
        self.assertEquals(assignment, true_assignment)


if __name__ == "__main__":
    unittest.main()
