from sympy import zeros
from sympy.matrices.dense import MutableDenseMatrix


class Network(object):
    """
    :type intensities:MutableDenseMatrix
    :type adjacency_matrix:MutableDenseMatrix
    """

    def __init__(self, adjacency_matrix, intensities):
        intens_sum = 0
        for i in xrange(intensities.shape[0]):
            intens_sum += intensities[i, 0]
        assert intens_sum == 0
        assert adjacency_matrix.shape[0] == adjacency_matrix.shape[1]
        self.node_quantity = adjacency_matrix.shape[0]
        self.adjacency_matrix = adjacency_matrix
        self.intensities = intensities

    def add_synthetic_node(self):
        added_arcs = []
        intensities = zeros(self.node_quantity + 1, 1)
        intensities[:-1, 0] = self.intensities[:, 0]
        self.intensities = intensities
        adjacency_matrx = zeros(self.node_quantity + 1, self.node_quantity + 1)
        adjacency_matrx[:-1, :-1] = self.adjacency_matrix[:, :]
        for i in xrange(self.node_quantity):
            if self.intensities[i, 0] >= 0:
                self.adjacency_matrix[i, self.node_quantity] = 1
                added_arcs.append((i, self.node_quantity))
            else:
                self.adjacency_matrix[self.node_quantity, i] = 1
                added_arcs.append((self.node_quantity, i))
        self.node_quantity += 1
        return added_arcs

    def get_cost(self, i, j):
        return self.adjacency_matrix[i, j]

    def get_intensity(self, i):
        return self.intensities[i, 0]

    def get_arcs(self):
        arcs = []
        for i in xrange(self.node_quantity):
            for j in xrange(self.node_quantity):
                if self.adjacency_matrix[i, j] != 0:
                    arcs.append((i, j))
        return arcs

    def get_adjacency_list(self):
        adjacency_list = []
        for i in xrange(self.node_quantity):
            ver_adjacency = []
            for j in xrange(self.node_quantity):
                if self.adjacency_matrix[i, j] != 0 or self.adjacency_matrix[j, i] != 0:
                    ver_adjacency.append(j)
            adjacency_list.append(tuple(ver_adjacency))
        return tuple(adjacency_list)

    @staticmethod
    def get_vertexes_neighbors(arc_set):
        adjacency_dict = {}
        for i, j in arc_set:
            if i in adjacency_dict:
                adjacency_dict[i].append(j)
            else:
                adjacency_dict[i] = [j]
            if j in adjacency_dict:
                adjacency_dict[j].append(i)
            else:
                adjacency_dict[j] = [i]
        adjacency_list = [()] * (max(adjacency_dict.keys()) + 1)
        for i, neighb in adjacency_dict.items():
            adjacency_list[i] = tuple(neighb)
        return tuple(adjacency_list)

    @staticmethod
    def find_cycle(arc_set, start_edge):
        adjacency_list = Network.get_vertexes_neighbors(arc_set)
        vertex_list = list(start_edge)
        for ver in adjacency_list[start_edge[1]]:
            if Network._cycle_dfs(ver, set(start_edge), vertex_list, adjacency_list):
                return vertex_list
        else:
            return None

    @staticmethod
    def _cycle_dfs(vertex, visited, vertex_list, adjacency_list):
        """
        :type vertex:int
        :type visited set[int]
        :type vertex_list:list[int]
        :type adjacency_list:tuple[tuple[int]]
        :rtype bool
        """
        vertex_list.append(vertex)
        visited.add(vertex)
        for ver in adjacency_list[vertex]:
            if ver == vertex_list[0]:
                return True
            elif ver not in visited:
                if Network._cycle_dfs(ver, visited, vertex_list, adjacency_list):
                    return True
        vertex_list.pop()
        return False
