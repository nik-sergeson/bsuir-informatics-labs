from  Network import Network
from sympy import zeros, ImmutableMatrix
from sympy.matrices.dense import MutableDenseMatrix


class MinCostFlow(object):
    """
    :type network:Network
    """

    def __init__(self, network):
        self.network = network

    def find_initial_flow(self):
        U_arcs = self.network.get_arcs()
        U_synt = self.network.add_synthetic_node()
        basis_flow = zeros(self.network.node_quantity, self.network.node_quantity)
        for i, j in U_synt:
            if i == self.network.node_quantity - 1:
                basis_flow[i, j] = abs(self.network.get_intensity(j))
            else:
                basis_flow[i, j] = abs(self.network.get_intensity(i))
        U_basis = U_synt
        while True:
            U_basis, basis_flow = self.find_optimal_flow(list(U_basis), MutableDenseMatrix(basis_flow))
            for i, j in U_synt:
                if basis_flow[i, j] != 0:
                    raise Exception("No flow can be found")
            synt_intersection = list(set(U_basis).intersection(set(U_synt)))
            if len(synt_intersection) == 1:
                U_basis.remove(synt_intersection[0])
                return U_basis, basis_flow
            else:
                U_not_basis = list(set(U_arcs) - set(U_basis))
                for arc in U_not_basis:
                    arc_to_remove = self.syntetic_arc_to_remove(arc, list(U_basis), U_synt)
                    if arc_to_remove:
                        U_basis.remove(arc_to_remove)
                        U_basis.append(arc)
                        break

    def syntetic_arc_to_remove(self, new_arc, U_basis, U_synt):
        U_basis.append(new_arc)
        synthetic_arcs = []
        cycle = Network.find_cycle(U_basis, new_arc[0])
        for i in xrange(len(cycle) - 1):
            arc = (cycle[i], cycle[i + 1])
            if arc in U_synt:
                synthetic_arcs.append(arc)
            elif tuple(reversed(arc)) in U_synt:
                synthetic_arcs.append(tuple(reversed(arc)))
        if len(synthetic_arcs) == 2:
            return synthetic_arcs[0]
        else:
            return None

    def find_optimal_flow(self, U_basis, basis_flow):
        """
        :type U_basis:list[tuple]
        :type basis_flow:MutableDenseMatrix
        :rtype (list[tuple], MutableDenseMatrix)
        """
        while True:
            potentials = self.get_potentials(U_basis, self.network)
            estimates = self.get_not_basis_estimates(U_basis, self.network, potentials)
            for (i, j), estimate in estimates.items():
                if estimate > 0:
                    i0, j0 = i, j
                    break
            else:
                return U_basis, basis_flow
            U_basis.append((i0, j0))
            cycle = Network.find_cycle(U_basis, (i0, j0))
            cycle.append(cycle[0])
            if cycle is None:
                raise Exception("Bad cycle")
            min_theta, theta_arc = self.get_theta0_arc(basis_flow, U_basis, cycle)
            for i in xrange(len(cycle) - 1):
                arc = (cycle[i], cycle[i + 1])
                if arc in U_basis:
                    basis_flow[cycle[i], cycle[i + 1]] += min_theta
                else:
                    basis_flow[cycle[i + 1], cycle[i]] -= min_theta
            U_basis.remove(theta_arc)
            basis_flow[theta_arc[0], theta_arc[1]] = 0

    def solve(self, basis_flow=None):
        """
        :type basis_flow:dict[tuple, int]
        """
        if basis_flow is None:
            U_basis, flow = self.find_initial_flow()
        else:
            U_basis = []
            flow = zeros(self.network.node_quantity, self.network.node_quantity)
            for (i, j), quant in basis_flow.items():
                U_basis.append((i, j))
                flow[i, j] = quant
        return self.find_optimal_flow(U_basis, flow)

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

    def get_theta0_arc(self, basis_flow, U_basis, cycle):
        min_theta = float("inf")
        theta_i, theta_j = -1, -1
        for i in xrange(len(cycle) - 1):
            arc = (cycle[i], cycle[i + 1])
            if arc not in U_basis:
                if basis_flow[cycle[i + 1], cycle[i]] < min_theta:
                    min_theta = basis_flow[cycle[i + 1], cycle[i]]
                    theta_i, theta_j = cycle[i + 1], cycle[i]
        return min_theta, (theta_i, theta_j)


def get_flow_cost(U_set, flow, network):
    """
    :type U_set:list[tuple[int]]
    :type flow:MutableDenseMatrix
    :type network:Network
    """
    cost = 0
    for i, j in U_set:
        cost += flow[i, j] * network.get_cost(i, j)
    return cost
