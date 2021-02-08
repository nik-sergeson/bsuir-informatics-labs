from sympy import Matrix, zeros


class ShortestPath(object):
    """
    :type path_matrix:Matrix
    :type vertex_quantity:Matrix
    """

    def __init__(self, path_matrix):
        assert path_matrix.shape[0] == path_matrix.shape[1]
        self.path_matrix = path_matrix
        self.vertex_quantity = path_matrix.shape[0]

    def path_exist(self, i, j):
        if self.path_matrix[i, j] < float("inf"):
            return True
        else:
            return False

    def solve(self):
        self.shortest_path = zeros(*self.path_matrix.shape)
        self.first_node = zeros(*self.path_matrix.shape)
        for i in xrange(self.vertex_quantity):
            for j in xrange(self.vertex_quantity):
                self.first_node[i, j] = j
                if i != j:
                    self.shortest_path[i, j] = self.path_matrix[i, j]
        for j in xrange(self.vertex_quantity):
            for i in xrange(self.vertex_quantity):
                if i == j:
                    continue
                for k in xrange(self.vertex_quantity):
                    if k == j or i == k:
                        continue
                    if self.shortest_path[i, k] > self.shortest_path[i, j] + self.shortest_path[j, k]:
                        self.shortest_path[i, k] = self.shortest_path[i, j] + self.shortest_path[j, k]
                        self.first_node[i, k] = self.first_node[i, j]
        return self.shortest_path, self.first_node
