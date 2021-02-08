from sympy import Matrix, zeros


class MaxFlow(object):
    """
    :type throughputs:MutableDenseMatrix
    :type flows:MutableDenseMatrix
    """

    def __init__(self, throughputs):
        assert throughputs.shape[0] == throughputs.shape[1]
        self.throughputs = throughputs
        self.flow = zeros(*throughputs.shape)
        self.vertex_quantity = self.throughputs.shape[0]
        self.adjacency_list = self.get_adjacency_list()

    def get_adjacency_list(self):
        adjacency_list = []
        for i in xrange(self.vertex_quantity):
            ver_adjacency = []
            for j in xrange(self.vertex_quantity):
                if self.throughputs[i, j] != 0 or self.throughputs[j, i] != 0:
                    ver_adjacency.append(j)
            adjacency_list.append(tuple(ver_adjacency))
        return tuple(adjacency_list)

    def is_straight_arc(self, i, j):
        if self.throughputs[i, j] != 0:
            return True
        elif self.throughputs[j, i] != 0:
            return False
        else:
            raise Exception("Arc doesn't exist")

    def find_augmenting_path(self):
        path = []
        if self._augmenting_path_dfs(0, self.adjacency_list, path, set()):
            return path
        else:
            return None

    def can_increase_flow(self, vertex1, vertex2):
        if self.is_straight_arc(vertex1, vertex2):
            return self.flow[vertex1, vertex2] < self.throughputs[vertex1, vertex2]
        else:
            return self.flow[vertex2, vertex1] > 0

    def _augmenting_path_dfs(self, vertex, adjacency_list, path, visited):
        """
        :type vertex:int
        :type visited:set[int]
        :type path:list[int]
        :type adjacency_list:tuple[tuple[int]]
        :rtype int
        """
        path.append(vertex)
        visited.add(vertex)
        if vertex == self.vertex_quantity - 1:
            return True
        for ver in adjacency_list[vertex]:
            if ver not in visited and self.can_increase_flow(vertex, ver):
                if self._augmenting_path_dfs(ver, adjacency_list, path, visited):
                    return True
        path.pop()
        return False

    def recalculate_flow(self, path):
        min_flow = float("inf")
        for i in xrange(len(path) - 1):
            arc = (path[i], path[i + 1])
            if self.is_straight_arc(*arc):
                min_flow = min(min_flow, self.throughputs[arc[0], arc[1]] - self.flow[arc[0], arc[1]])
            else:
                min_flow = min(min_flow, self.flow[arc[1], arc[0]])
        for i in xrange(len(path) - 1):
            arc = (path[i], path[i + 1])
            if self.is_straight_arc(*arc):
                self.flow[arc[0], arc[1]] += min_flow
            else:
                self.flow[arc[1], arc[0]] -= min_flow
        return min_flow

    def solve(self):
        max_flow = 0
        while True:
            augmenting_path = self.find_augmenting_path()
            if augmenting_path is None:
                return max_flow
            else:
                max_flow += self.recalculate_flow(augmenting_path)
