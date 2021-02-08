from sympy import Matrix, zeros


class ShortestPathTree(object):
    def __init__(self, length_matrix):
        assert length_matrix.shape[0] == length_matrix.shape[1]
        for i in xrange(length_matrix.shape[0]):
            for j in xrange(length_matrix.shape[1]):
                assert length_matrix[i, j] >= 0
        self.length_matrix = length_matrix
        self.vertex_quantity = length_matrix.shape[0]

    def solve(self):
        self.shortest_length = zeros(self.vertex_quantity, 1)
        for i in xrange(1, self.vertex_quantity):
            self.shortest_length[i, 0] = float("inf")
        self.parents = zeros(self.vertex_quantity, 1)
        not_visited = set(range(self.vertex_quantity))
        for i in xrange(self.vertex_quantity):
            min_length = float("inf")
            min_length_ver = -1
            for ver in not_visited:
                if self.shortest_length[ver] < min_length:
                    min_length_ver = ver
                    min_length = self.shortest_length[ver]
            if min_length_ver == -1:
                break
            not_visited.remove(min_length_ver)
            for j in xrange(self.vertex_quantity):
                if self.length_matrix[min_length_ver, j] != 0:
                    if self.shortest_length[min_length_ver, 0] + self.length_matrix[min_length_ver, j] < \
                            self.shortest_length[j, 0]:
                        self.shortest_length[j, 0] = self.shortest_length[min_length_ver, 0] + self.length_matrix[
                            min_length_ver, j]
                        self.parents[j, 0] = min_length_ver
        return self.shortest_length, self.parents
