from sympy.matrices import MutableDenseMatrix
from sympy.core.numbers import Integer
from math import floor
from lab1.DualSimplexMethod import DualSimplexMethod


class BranchnBound(object):
    """
    :rtype A_matrix:MutbaleDenseMatrix
    :rtype b_matrix:MutableDenseMatrix
    :rtype c_matrix:MutableDenseMatrix
    :rtype d_lower:MutableDenseMatrix
    :rtype d_upper:MutableDenseMatrix
    """

    def __init__(self, A_matrix, b_matrix, c_matrix, d_lower, d_upper):
        self.record = float("-inf")
        self.task_list = []
        self.plan = None
        self.task_list.append(DualSimplexMethod(A_matrix, b_matrix, c_matrix, d_lower, d_upper))
        self.eps = 0.0001

    def solve(self):
        while self.task_list:
            task = self.task_list.pop()
            try:
                plan, J_basis = task.solve()
            except Exception:
                continue
            c_x = (task.c_matrix.transpose() * plan)[0, 0]
            if c_x > self.record:
                j = -1
                for i in xrange(plan.shape[0]):
                    if abs(plan[i, 0] - round(plan[i, 0])) > self.eps:
                        j = i
                        break
                if j == -1:
                    self.plan = plan
                    self.record = c_x
                else:
                    self.split(task, plan, j)
        if self.plan is None:
            raise Exception("Task has no plans")
        else:
            return self.plan, self.record

    def split(self, task, plan, j):
        x_aster = plan[j, 0]
        l_j = floor(x_aster)
        d_upper_task_1 = MutableDenseMatrix(task.d_upper)
        d_upper_task_1[j, 0] = l_j
        d_lower_task2 = MutableDenseMatrix(task.d_lower)
        d_lower_task2[j, 0] = l_j + 1
        self.task_list.append(
            DualSimplexMethod(task.A_matrix, task.b_matrix, task.c_matrix, task.d_lower, d_upper_task_1))
        self.task_list.append(
            DualSimplexMethod(task.A_matrix, task.b_matrix, task.c_matrix, d_lower_task2, task.d_upper))
