# suboptimal solution
# O(nm) time complexity
# n - number of rows
# m - number of columns
import math


def parquet(B, C, s):
    n = len(B)
    m = len(B[0])
    memory = {}

    def f(row, col):
        if memory.get((row, col), False):
            return memory[(row, col)]

        result = math.inf
        if C[row][col] <= s:
            result = 0
        else:
            if row + 1 < n and C[row][col] - C[row+1][col] <= s:
                result = f(row+1, col) + 1
            if col + 1 < m and C[row][col] - C[row][col+1] <= s:
                result = min(result, f(row, col+1) + 1)

        memory[(row, col)] = result
        return result

    f(0, 0)
    return -1 if memory[(0, 0)] == math.inf else memory[(0, 0)]


B = [[2, 1, 4],
     [1, 3, 1],
     [2, 3, 3]]
C = [[20, 15, 8],
     [13, 10, 4],
     [8,   6, 3]]
s = 5

print(parquet(B, C, s))
