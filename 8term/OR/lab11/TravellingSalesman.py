from sympy import Matrix
from lab10.AssignmentProblem import AssignmentProblem


class TravellingSalesman(object):
    """
    :type cost_matrix:MutableDenseMatrix
    :type task_list:list[AssignmentProblem]
    """

    def __init__(self, cost_matrix):
        assert cost_matrix.shape[0] == cost_matrix.shape[1]
        self.size = cost_matrix.shape[0]
        self.cost_matrix = cost_matrix
        self.path = range(self.size) + [0]
        self.min_cost = TravellingSalesman.get_path_cost(cost_matrix, self.path)
        self.task_list = []
        self.task_list.append(AssignmentProblem(self.cost_matrix))

    def solve(self):
        while self.task_list:
            cur_task = self.task_list.pop(0)
            path = cur_task.solve()
            path_length = AssignmentProblem.get_cost(self.cost_matrix, path)
            if path_length < self.min_cost:
                subcycles = self.build_cycle(path)
                if len(subcycles) == 1:
                    self.path = path
                    self.min_cost = path_length
                else:
                    shortest_cycle = subcycles[0]
                    for cycle in subcycles[1::]:
                        if len(cycle) < len(shortest_cycle):
                            shortest_cycle = cycle
                    for i, j in zip(shortest_cycle[::], shortest_cycle[1::]):
                        cost_matrix = Matrix(cur_task.modified_cost_matrix)
                        cost_matrix[i, j] = float('inf')
                        self.task_list.append(AssignmentProblem(cost_matrix))
        return self.min_cost

    def build_cycle(self, path):
        """
        :type path:MutableDenseMatrix
        :rtype list[list[int]]
        """
        cycle = []
        vertex_to_process = range(path.shape[0])
        while vertex_to_process:
            next_vert = vertex_to_process.pop(0)
            subcycle = [next_vert]
            next_vert = path[next_vert, 0]
            while next_vert != subcycle[0]:
                vertex_to_process.remove(next_vert)
                subcycle.append(next_vert)
                next_vert = path[next_vert, 0]
            subcycle.append(next_vert)
            cycle.append(subcycle)
        return cycle

    @staticmethod
    def get_path_cost(cost_matrix, path):
        """
        :type cost_matrix:MutableDenseMatrix
        :type path:MutableDenseMatrix
        """
        cost = 0
        for i, j in zip(path[::], path[1::]):
            cost += cost_matrix[i, j]
        return cost
