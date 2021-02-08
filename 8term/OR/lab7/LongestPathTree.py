from sympy import zeros, Matrix


class LongestPathTree(object):
    """
    :type path_matrix:Matrix
    :type vertex_quantity:Matrix
    """

    def __init__(self, path_matrix):
        assert path_matrix.shape[0] == path_matrix.shape[1]
        for i in xrange(path_matrix.shape[0]):
            for j in xrange(path_matrix.shape[1]):
                assert path_matrix[i, j] >= 0
        self.path_matrix = path_matrix
        self.vertex_quantity = path_matrix.shape[0]

    def get_mutable_ajacency_list(self):
        """
        :rtype list[list]
        """
        adjacency_list = []
        for i in xrange(self.vertex_quantity):
            vertex_adjacency = []
            for j in xrange(self.vertex_quantity):
                if self.path_matrix[i, j] != 0:
                    vertex_adjacency.append(j)
            adjacency_list.append(vertex_adjacency)
        return adjacency_list

    def get_vertex_sources_list(self):
        """
        :rtype list[list]
        """
        source_list = []
        for i in xrange(self.vertex_quantity):
            source_list.append([])
        for i in xrange(self.vertex_quantity):
            for j in xrange(self.vertex_quantity):
                if self.path_matrix[i, j] != 0:
                    source_list[j].append(i)
        return source_list

    def solve(self):
        """
        :rtype tuple[Matrix]
        """
        self.longest_path = zeros(self.vertex_quantity, 1)
        for i in xrange(1, self.vertex_quantity):
            self.longest_path[i, 0] = float("-inf")
        self.parents = zeros(self.vertex_quantity, 1)
        adjacency_list = self.get_mutable_ajacency_list()
        known_bellman = {0}
        network_cut = set(adjacency_list[0])
        vertex_sources = self.get_vertex_sources_list()
        while self.vertex_quantity - 1 not in known_bellman:
            for ver in network_cut:
                if set(vertex_sources[ver]).issubset(known_bellman):
                    for source_ver in vertex_sources[ver]:
                        if self.longest_path[source_ver, 0] + self.path_matrix[source_ver, ver] > self.longest_path[
                            ver, 0]:
                            self.longest_path[ver, 0] = self.longest_path[source_ver, 0] + self.path_matrix[
                                source_ver, ver]
                            self.parents[ver, 0] = source_ver
                    known_bellman.add(ver)
                    network_cut.remove(ver)
                    network_cut.update(adjacency_list[ver])
                    break
            else:
                break
        return self.longest_path, self.parents
