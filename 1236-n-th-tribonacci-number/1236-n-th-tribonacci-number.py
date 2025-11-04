import numpy as np
class Solution:
    def fastPow(self, matrix, pow):  # return matrix ^ pow
        if pow == 1: return matrix
        half = self.fastPow(matrix, pow // 2)
        res = np.dot(half, half)  # res = half * half
        if pow & 1:  # If pow is an odd number
            res = np.dot(res, matrix)  # res *= matrix
        return res

    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        matrix = np.matrix([[0, 1, 0], [0, 0, 1], [1, 1, 1]])
        M0 = np.matrix([[0], [1], [1]])
        Mn = np.dot(self.fastPow(matrix, n), M0)  # Mn = matrix^n * M0
        return Mn.item((0, 0))