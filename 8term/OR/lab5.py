from sympy import Matrix
from lab5.Network import Network
from lab5.MinCostFlow import MinCostFlow, get_flow_cost

paths = Matrix([[0, 1, 0, 0, 0, 0, 0],
                [0, 0, 1, 3, 2, 0, 0],
                [3, 0, 0, 3, 0, 4, 0],
                [4, 0, 0, 0, 0, -1, 6],
                [0, 0, 0, 5, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 2, 0]])
a = Matrix([-2, 3, 1, 8, 4 - 6, -8])
u = {(3, 0): 2, (1, 2): 3, (2, 3): 4, (4, 3): 4, (3, 6): 8, (3, 5): 6}
network = Network(paths, a)
solver = MinCostFlow(network)
U, flow = solver.solve(u)
result = get_flow_cost(U, flow, network)
print(result)

from lab5.MinCostFlowWithContraint import MinCostFlow, get_flow_cost
paths = Matrix([[0, 1, 0, 0, 0, 0, 0],
                [0, 0, 1, 3, 2, 0, 0],
                [3, 0, 0, 3, 0, 4, 0],
                [4, 0, 0, 0, 0, -1, 6],
                [0, 0, 0, 5, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 2, 0]])
constraints = Matrix([[0, 5, 0, 0, 0, 0, 0],
                 [0, 0, 5, 5, 5, 0, 0],
                 [5, 0, 0, 5, 0, 5, 0],
                 [5, 0, 0, 0, 0, 7, 10],
                 [0, 0, 0, 5, 0, 0, 5],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 5, 0]])
a = Matrix([-2, 3, 1, 8, 4 - 6, -8])
u = {(3, 0): 2, (1, 2): 3, (2, 3): 4, (4, 3): 4, (3, 6): 8, (3, 5): 6}
network = Network(paths, a)
solver = MinCostFlow(network)
U, flow = solver.solve(constraints, u)
result = get_flow_cost(U, flow, network)
print(result)


paths = Matrix([[0, 8, 0, 0, 0, 10],
         [0, 0, 10, 0, -10, 5],
         [0, 0, 0, -4, 6, 3],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 5, 0, 0],
         [0, 0, 0, 0, 9, 0]])
constraints = Matrix([[0, 7, 0, 0, 0, 7],
         [0, 0, 7, 0, 7, 7],
         [0, 0, 0, 7, 7, 7],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 7, 0, 0],
         [0, 0, 0, 0, 7, 0]])
a = Matrix([10, 4, 4,-2,-10,-6])
u = {(0,5):3, (1,5):4, (2,5):6,(2,4):5,(4,3):2}
network = Network(paths, a)
solver = MinCostFlow(network)
U, flow = solver.solve(constraints, u)
result = get_flow_cost(U, flow, network)
print(result)