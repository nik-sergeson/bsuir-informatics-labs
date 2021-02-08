from sympy import Matrix, zeros


class Solver(object):
    """
    :type producers:Matrix
    :type consumers:Matrix
    :type cost_matrix:Matrix
    """

    def __init__(self, producers, consumers, cost_matrix):
        self.producers = producers
        self.consumers = consumers
        self.cost_matrix = cost_matrix
        a = 0
        b = 0
        for i in range(self.producers.shape[0]):
            a += self.producers[i, 0]
        for i in range(self.consumers.shape[0]):
            b += self.consumers[i, 0]
        c = a - b
        if c < 0:
            self.producers = self.producers.row_insert(self.producers.shape[0], Matrix([[-c]]))
            self.cost_matrix = self.cost_matrix.row_insert(self.cost_matrix.shape[0],
                                                           Matrix([[0] * self.consumers.shape[0]]))
        elif c > 0:
            self.consumers = self.consumers.row_insert(self.consumers.shape[0], Matrix([[c]]))
            self.cost_matrix = self.cost_matrix.col_insert(self.cost_matrix.shape[1],
                                                           Matrix([[0]] * self.producers.shape[0]))
        self.m, self.n = self.producers.shape[0], self.consumers.shape[0]

    @staticmethod
    def get_initial_plan(producers, consumers):
        """
        :type producers:Matrix
        :type consumers:Matrix
        """
        m, n = producers.shape[0], consumers.shape[0]
        transportation_matrix = zeros(m, n)
        basis_set = []
        i = 0
        j = 0
        while True:
            if i >= m or j >= n:
                break
            basis_set.append((i, j))
            if producers[i, 0] < consumers[j, 0]:
                transportation_matrix[i, j] = producers[i, 0]
                consumers[j, 0] -= producers[i, 0]
                producers[i, 0] = 0
                for k in range(j + 1, n):
                    transportation_matrix[i, k] = 0
                i += 1
            elif consumers[j, 0] < producers[i, 0]:
                transportation_matrix[i, j] = consumers[j, 0]
                producers[i, 0] -= consumers[j, 0]
                consumers[j, 0] = 0
                for k in range(i + 1, m):
                    transportation_matrix[k, j] = 0
                j += 1
            else:
                transportation_matrix[i, j] = consumers[j, 0]
                producers[i, 0] = 0
                consumers[j, 0] = 0
                for k in range(j + 1, n):
                    transportation_matrix[i, k] = 0
                i += 1
        return transportation_matrix, basis_set

    def solve(self):
        transportation_matrix, basis_set = Solver.get_initial_plan(self.producers, self.consumers)
        while True:
            producer_potentials, consumer_potentials = Solver.get_potentials(self.cost_matrix, basis_set)
            i0_index, j0_index = Solver.get_positive_delta_index(self.cost_matrix, producer_potentials,
                                                                 consumer_potentials, basis_set)
            if i0_index == -1 and j0_index == -1:
                break
            cycle_points = self.get_cycle(basis_set, i0_index, j0_index)
            if not cycle_points:
                raise Exception("No cycle found")
            theta_i_index, theta_j_index = -1, -1
            theta = float('inf')
            for k in range(1, len(cycle_points), 2):
                i, j = cycle_points[k]
                if transportation_matrix[i, j] < theta:
                    theta_i_index, theta_j_index = i, j
                    theta = transportation_matrix[i, j]
            for k, (i, j) in enumerate(cycle_points):
                if k % 2 == 0:
                    transportation_matrix[i, j] += theta
                else:
                    transportation_matrix[i, j] -= theta
            basis_set.remove((theta_i_index, theta_j_index))
            basis_set.append((i0_index, j0_index))
        return transportation_matrix

    @staticmethod
    def get_potentials(cost_matrix, basis_set):
        """
        :type cost_matrix:Matrix
        :type basis_set:list[tuple[int, int]]
        """
        index_set = list(basis_set)
        i, j = index_set.pop(0)
        producers_potentials = {}
        consumer_potentials = {}
        producers_potentials[i] = 0
        consumer_potentials[j] = cost_matrix[i, j]
        while len(index_set) > 0:
            for k, (i, j) in enumerate(index_set):
                if i in producers_potentials:
                    consumer_potentials[j] = cost_matrix[i, j] - producers_potentials[i]
                    index_set.pop(k)
                    break
                elif j in consumer_potentials:
                    producers_potentials[i] = cost_matrix[i, j] - consumer_potentials[j]
                    index_set.pop(k)
                    break
        return producers_potentials, consumer_potentials

    @staticmethod
    def get_positive_delta_index(cost_matrix, producer_potentials, consumer_potentials, basis_set):
        """
        :type cost_matrix:Matrix
        :type producer_potentials:dict[int, int]
        :type consumer_potentials:dict[int, int]
        :type basis_set:list[tuple[int, int]]
        """
        m, n = cost_matrix.shape
        for i in range(m):
            for j in range(n):
                if (i, j) not in basis_set:
                    estimate = producer_potentials[i] + consumer_potentials[j] - cost_matrix[i, j]
                    if estimate > 0:
                        return i, j
        return -1, -1

    def get_cycle(self, basis_set, i0, j0):
        """
        :type basis_set:list[tuple[int, int]]
        :type i0:int
        :type j0:int
        """
        cycle_points = [(i0, j0)]
        if self.move_horizontally(list(basis_set), cycle_points, i0):
            return cycle_points
        else:
            return None

    def move_horizontally(self, basis_set, cycle_points, i_prev):
        """
        :type basis_set:list[tuple[int, int]]
        :type cycle_points:list[tuple[int, int]]
        :type i_prev:int
        """
        for k, i_j_pair in enumerate(basis_set):
            if i_j_pair is not None:
                i, j = i_j_pair
                if i == i_prev:
                    cycle_points.append((i, j))
                    basis_set[k] = None
                    if j == cycle_points[0][1]:
                        return True
                    if self.move_vertically(basis_set, cycle_points, j):
                        return True
                    cycle_points.pop()
                    basis_set[k] = (i, j)
        return False

    def move_vertically(self, basis_set, cycle_points, j_prev):
        """
        :type basis_set:list[tuple[int, int]]
        :type cycle_points:list[tuple[int, int]]
        :type j_prev:int
        """
        for k, i_j_pair in enumerate(basis_set):
            if i_j_pair is not None:
                i, j = i_j_pair
                if j == j_prev:
                    cycle_points.append((i, j))
                    basis_set[k] = None
                    if i == cycle_points[0][0]:
                        return True
                    if self.move_horizontally(basis_set, cycle_points, i):
                        return True
                    cycle_points.pop()
                    basis_set[k] = (i, j)
        return False
