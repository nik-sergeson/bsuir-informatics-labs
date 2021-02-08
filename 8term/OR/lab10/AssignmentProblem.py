from sympy import Matrix, zeros
from lab8.MaxFlow import MaxFlow


class AssignmentProblem(object):
    """
    :type cost_matrix:MutableDenseMatrix
    """

    def __init__(self, cost_matrix):
        assert cost_matrix.shape[0] == cost_matrix.shape[1]
        self.cost_matrix = cost_matrix
        self.size = cost_matrix.shape[0]

    def get_left_partite_vertexes(self):
        return set(range(self.size))

    def get_right_partite_vertexes(self):
        return set(range(self.size, 2 * self.size))

    def solve(self):
        self.modified_cost_matrix = Matrix(self.cost_matrix)
        for i in xrange(self.modified_cost_matrix.shape[0]):
            min_cost = min(self.modified_cost_matrix[i, :])
            for j in xrange(self.modified_cost_matrix.shape[1]):
                self.modified_cost_matrix[i, j] = self.modified_cost_matrix[i, j] - min_cost
        for j in xrange(self.modified_cost_matrix.shape[1]):
            min_cost = min(self.modified_cost_matrix[:, j])
            for i in xrange(self.modified_cost_matrix.shape[0]):
                self.modified_cost_matrix[i, j] = self.modified_cost_matrix[i, j] - min_cost
        while True:
            network = self.build_network(self.modified_cost_matrix)
            max_flow = MaxFlow(network)
            if max_flow.solve() == self.size:
                assignments = zeros(self.size, 1)
                for i in self.get_left_partite_vertexes():
                    for j in self.get_right_partite_vertexes():
                        if max_flow.flow[i + 1, j + 1] != 0:
                            assignments[i, 0] = j - self.size
                return assignments
            else:
                X_cover, Y_cover = self.get_minimal_vertex_cover(max_flow)
                self.transform_cost_matrix(self.modified_cost_matrix, X_cover, Y_cover)

    def build_network(self, modified_cost_matrix):
        """
        :type modified_cost_matrix:Matrix
        """
        network = zeros(2 * self.size + 2)
        for i in xrange(1, self.size + 1):
            network[0, i] = 1
        for i in xrange(self.size + 1, 2 * self.size + 1):
            network[i, 2 * self.size + 1] = 1
        for i in xrange(self.size):
            for j in xrange(self.size):
                if modified_cost_matrix[i, j] == 0:
                    network[i + 1, j + self.size + 1] = 1
        return network

    def get_minimal_vertex_cover(self, max_flow):
        """
        :type max_flow:MaxFlow
        :rtype tuple[set[int]]
        """
        flow = max_flow.flow
        adjacency_list = []
        for _ in xrange(2 * self.size):
            adjacency_list.append([])
        left_visited = set()
        right_visited = set()
        saturated_vertex = set()
        for i in xrange(1, self.size + 1):
            for j in xrange(self.size + 1, 2 * self.size + 1):
                if max_flow.throughputs[i, j] != 0:
                    if flow[i, j] != 0:
                        adjacency_list[j - 1].append(i - 1)
                        saturated_vertex.add(i - 1)
                    else:
                        adjacency_list[i - 1].append(j - 1)
        for i in xrange(2 * self.size):
            adjacency_list[i] = tuple(adjacency_list[i])
        adjacency_list = tuple(adjacency_list)
        for ver in self.get_left_partite_vertexes() - saturated_vertex:
            self._minimal_vertex_cover_dfs(ver, left_visited, right_visited, adjacency_list)
        return self.get_left_partite_vertexes() - left_visited, right_visited

    def _minimal_vertex_cover_dfs(self, vertex, left_visited, right_visited, adjacecency_list):
        """
        :type vertex:int
        :type left_visited:set
        :type right_visited: set
        :type adjacecency_list:tuple[tuple[int]]
        """
        if vertex < self.size:
            left_visited.add(vertex)
        else:
            right_visited.add(vertex)
        for ver in adjacecency_list[vertex]:
            if ver not in left_visited and ver not in right_visited:
                self._minimal_vertex_cover_dfs(ver, left_visited, right_visited, adjacecency_list)

    def transform_cost_matrix(self, modified_cost_matrix, X_cover, Y_cover):
        min_d = float('inf')
        for i in self.get_left_partite_vertexes() - X_cover:
            for j in self.get_right_partite_vertexes() - Y_cover:
                if modified_cost_matrix[i, j - self.size] < min_d:
                    min_d = modified_cost_matrix[i, j - self.size]
        for i in X_cover:
            for j in self.get_right_partite_vertexes():
                modified_cost_matrix[i, j - self.size] += min_d
        for i in self.get_left_partite_vertexes():
            for j in self.get_right_partite_vertexes() - Y_cover:
                modified_cost_matrix[i, j - self.size] -= min_d

    @staticmethod
    def get_cost(cost_matrix, assignments):
        result = 0
        for i in xrange(assignments.shape[0]):
            result += cost_matrix[i, assignments[i, 0]]
        return result
