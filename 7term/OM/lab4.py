from transportation_problem.solver import Solver
from  sympy import Matrix


def check(producers, consumers, costs, properResult):
    solver = Solver(producers, consumers, costs)
    plan = solver.solve()
    result = 0
    for i in range(costs.shape[0]):
        for j in range(costs.shape[1]):
            result += plan[i, j] * costs[i, j]
    print(plan)
    print("Cost:", result)
    print("Equal to theoretic: ", result == properResult)


if __name__ == "__main__":
    producers = Matrix([[15], [25], [10]])
    consumers = Matrix([[2], [20], [18]])
    costs = Matrix([[2, 5, 7], [8, 12, 2], [1, 3, 8]])
    properResult = 120
    check(producers, consumers, costs, properResult)

    producers = Matrix([[320], [280], [250]])
    consumers = Matrix([[150], [140], [110], [230], [220]])
    costs = Matrix([[20, 23, 20, 15, 24], [29, 15, 16, 19, 29], [6, 11, 10, 9, 8]])
    properResult = 11770
    check(producers, consumers, costs, properResult)

    producers = Matrix([[500], [300], [100]])
    consumers = Matrix([[150], [350], [200], [100], [100]])
    costs = Matrix([[3, 3, 5, 3, 1], [4, 3, 2, 4, 5], [3, 7, 5, 4, 2]])
    properResult = 2300
    check(producers, consumers, costs, properResult)

    producers = Matrix([[14], [14], [14], [14]])
    consumers = Matrix([[13], [5], [13], [12], [13]])
    costs = Matrix([[16, 26, 12, 24, 3], [5, 2, 19, 27, 2], [29, 23, 25, 16, 8], [2, 25, 14, 15, 21]])
    properResult = 426
    check(producers, consumers, costs, properResult)

    producers = Matrix([[48], [30], [27], [20]])
    consumers = Matrix([[18], [27], [42], [12], [26]])
    costs = Matrix([[10, 8, 5, 6, 9], [6, 7, 8, 6, 5], [8, 7, 10, 8, 7], [7, 5, 4, 6, 8]])
    properResult = 703
    check(producers, consumers, costs, properResult)

    producers = Matrix([[130], [55], [80], [65], [135]])
    consumers = Matrix([[130], [75], [65], [60], [75], [60]])
    costs = Matrix([[6, 6, 8, 5, 4, 3], [2, 4, 3, 9, 8, 5], [3, 5, 7, 9, 6, 11], [3, 5, 4, 4, 2, 1],
                    [2, 5, 6, 3, 2, 8]])
    properResult = 1495
    check(producers, consumers, costs, properResult)

    producers = Matrix([[30], [50], [75], [20]])
    consumers = Matrix([[20], [40], [30], [10], [50], [25]])
    costs = Matrix([[1, 2, 1, 4, 5, 2], [3, 3, 2, 1, 4, 3], [4, 2, 5, 9, 6, 2], [3, 1, 7, 3, 4, 6]])
    properResult = 430
    check(producers, consumers, costs, properResult)

    producers = Matrix([[20], [30], [40]])
    consumers = Matrix([[20], [30], [20], [20]])
    costs = Matrix([[4, 1, 5, 3], [2, 6, 4, 7], [5, 3, 6, 4]])
    properResult = 270
    check(producers, consumers, costs, properResult)

    producers = Matrix([[70], [50], [20], [30]])
    consumers = Matrix([[50], [40], [10], [15], [25], [30]])
    costs = Matrix([[6, 3, 1, 5, 7, 4], [8, 4, 2, 4, 3, 6], [3, 5, 5, 6, 2, 4], [5, 1, 1, 3, 6, 2]])
    properResult = 575
    check(producers, consumers, costs, properResult)

    producers = Matrix([[60], [40], [70], [30]])
    consumers = Matrix([[60], [40], [40], [30], [30]])
    costs = Matrix([[5, 2, 0, 7, 3], [6, 1, 4, 2, 8], [7, 4, 3, 6, 1], [3, 5, 6, 4, 2]])
    properResult = 480
    check(producers, consumers, costs, properResult)

    consumers = Matrix([[10], [30], [40], [50], [70], [30]])
    producers = Matrix([[80], [60], [30], [60]])
    costs = Matrix([[3, 20, 8, 13, 4, 100], [4, 4, 18, 14, 3, 0], [10, 4, 18, 8, 6, 0], [7, 19, 17, 10, 1, 100]])
    solver = Solver(producers, consumers, costs)
    plan = solver.solve()
    result = 0
    for i in range(costs.shape[0]):
        for j in range(costs.shape[1]):
            result += plan[i, j] * costs[i, j]
    print(plan)
    print("Cost:", result)
