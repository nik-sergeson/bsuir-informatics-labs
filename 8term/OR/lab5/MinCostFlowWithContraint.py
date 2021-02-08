from  Network import Network
from sympy import zeros, ImmutableMatrix
from sympy.matrices.dense import MutableDenseMatrix


class MinCostFlow(object):
    """
    :type network:Network
    """

    def __init__(self, network):
        self.network = network

    def find_optimal_flow(self, U_basis, basis_flow, constraints):
        """
        :type U_basis:list[tuple]
        :type basis_flow:MutableDenseMatrix
        :rtype (list[tuple], MutableDenseMatrix)
        """
        while True:
            potentials = self.get_potentials(U_basis, self.network)
            estimates = self.get_not_basis_estimates(U_basis, self.network, potentials)
            for (i, j), estimate in estimates.items():
                if (basis_flow[i, j]==0 and estimate>0) or (basis_flow[i, j]==constraints[i,j] and estimate<0):
                    i0, j0 = i, j
                    break
            else:
                return U_basis, basis_flow
            U_basis.append((i0, j0))
            if basis_flow[i0, j0]==constraints[i0,j0]:
                cycle = Network.find_cycle(U_basis, (j0, i0))
            else:
                cycle = Network.find_cycle(U_basis, (i0, j0))
            cycle.append(cycle[0])
            if cycle is None:
                raise Exception("Bad cycle")
            min_theta, theta_arc = self.get_theta0_arc(basis_flow, U_basis, cycle, constraints)
            for i in xrange(len(cycle) - 1):
                arc = (cycle[i], cycle[i + 1])
                if arc in U_basis:
                    basis_flow[arc[0], arc[1]] += min_theta
                else:
                    basis_flow[arc[1], arc[0]] -= min_theta
            U_basis.remove(theta_arc)

    def solve(self,constraint, basis_flow=None):
        """
        :type basis_flow:dict[tuple, int]
        """
        U_basis = []
        flow = zeros(self.network.node_quantity, self.network.node_quantity)
        for (i, j), quant in basis_flow.items():
            U_basis.append((i, j))
            flow[i, j] = quant
        return self.find_optimal_flow(U_basis, flow, constraint)

    def get_potentials(self, U_basis, network):
        """
        :type U_basis:list
        :type network:Network
        """
        U_set = list(U_basis)
        i0, j0 = U_set.pop(0)
        potentials = {i0: 0, j0: -network.get_cost(i0, j0)}
        arcs_to_proceed = []
        arcs_to_proceed.extend(filter(lambda x: i0 in x or j0 in x, U_set))
        while U_set:
            i, j = arcs_to_proceed.pop(0)
            if i in potentials:
                potentials[j] = potentials[i] - network.get_cost(i, j)
                arcs_to_proceed.extend(filter(lambda x: j in x and i not in x, U_set))
            elif j in potentials:
                potentials[i] = potentials[j] + network.get_cost(i, j)
                arcs_to_proceed.extend(filter(lambda x: i in x and j not in x, U_set))
            U_set.remove((i, j))
        return potentials

    def get_not_basis_estimates(self, U_basis, network, potentials):
        """
        :type U_basis:list[(int,int)]
        :type network:Network
        :type potentials:dict[int, float]
        """
        U_not_basis = list(set(network.get_arcs()) - set(U_basis))
        estimates = {}
        for i, j in U_not_basis:
            estimates[(i, j)] = potentials[i] - potentials[j] - network.get_cost(i, j)
        return estimates

    def get_theta0_arc(self, basis_flow, U_basis, cycle, constraints):
        min_theta = float("inf")
        theta_i, theta_j = -1, -1
        for i in xrange(len(cycle) - 1):
            arc = (cycle[i], cycle[i + 1])
            if arc in U_basis:
                current_theta=constraints[arc[0], arc[1]]-basis_flow[arc[0], arc[1]]
            else:
                arc=arc[1], arc[0]
                current_theta=basis_flow[arc[0], arc[1]]
            if current_theta < min_theta:
                min_theta = current_theta
                theta_i, theta_j = arc
        return min_theta, (theta_i, theta_j)


def get_flow_cost(U_set, flow, network):
    """
    :type U_set:list[tuple[int]]
    :type flow:MutableDenseMatrix
    :type network:Network
    """
    cost = 0
    for i in xrange(flow.shape[0]):
        for j in xrange(flow.shape[1]):
            cost += flow[i, j] * network.get_cost(i, j)
    return cost
