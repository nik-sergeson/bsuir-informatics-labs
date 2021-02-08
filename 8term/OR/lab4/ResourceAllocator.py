from sympy.matrices.dense import MutableDenseMatrix, zeros


class ResourceAllocator(object):
    """
    :type f_matrix:MutableDenseMatrix
    :type bellman_function:MutableDenseMatrix
    :type used_resources:MutableDenseMatrix
    """

    def __init__(self, f_matrix):
        self.f_matrix = f_matrix
        self.k, self.n = f_matrix.shape
        self._calculate_bellman()

    def _calculate_bellman(self):
        self.bellman_function = zeros(self.k, self.n)
        self.used_resources = zeros(self.k, self.n)
        for y in xrange(self.n):
            self.bellman_function[0, y] = self.f_matrix[0, y]
            self.used_resources[0, y] = y
        for i in xrange(1, self.k):
            for y in xrange(self.n):
                z_max = -1
                B_max = float("-inf")
                for z in xrange(y + 1):
                    curr_value = self.f_matrix[i, z] + self.bellman_function[i - 1, y - z]
                    if curr_value > B_max:
                        z_max = z
                        B_max = curr_value
                self.bellman_function[i, y] = B_max
                self.used_resources[i, y] = z_max

    def find_plan(self, k, n):
        """
        :type used_resources:MutableDenseMatrix
        """
        plan = zeros(k, 1)
        left_resources = n - 1
        for y in reversed(xrange(k)):
            plan[y, 0] = self.used_resources[y, left_resources]
            left_resources -= self.used_resources[y, left_resources]
        return plan

    def solve(self, k=None, n=None):
        if k is None or n is None:
            k, n = self.k, self.n
        return self.bellman_function[k - 1, n - 1], self.find_plan(k, n)
