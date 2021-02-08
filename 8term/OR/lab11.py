from sympy import Matrix
from lab11.TravellingSalesman import TravellingSalesman
costs = Matrix([[float('inf'), -1, 4, 2, 6, 0],
                [2, float('inf'), 3, 2, 1, 8],
                [-6, 0, float('inf'), 3, 4, 7],
                [1, float('inf'), 1, float('inf'), 9, 2],
                [2, -1, 3, 4, float('inf'), 5],
                [float('inf'), 0, 9, -1, -5, float('inf')]])
result = TravellingSalesman(costs).solve()
print(result)