# suboptimal solution
# O(nm) time complexity
# n - number of rows
# m - number of columns
import math


def parquet(B, C, s):
    n, m = len(B), len(B[0])
    dp = [[math.inf for _ in range(m)] for __ in range(n)]
    dp[0][0] = 0

    for row in range(n):
        for col in range(m):
            if n == 0 and m == 0:
                continue
            if col-1 >= 0 and C[row][col-1] - C[row][col] <= s:
                dp[row][col] = min(dp[row][col], dp[row][col-1] + 1)
            if row-1 >= 0 and C[row-1][col] - C[row][col] <= s:
                dp[row][col] = min(dp[row][col], dp[row-1][col] + 1)

    answer = math.inf
    for i in range(n):
        if dp[i][m-1] < answer and C[i][m-1] <= s:
            answer = dp[i][m-1]
    for i in range(m):
        if dp[n-1][i] < answer and C[n-1][i] <= s:
            answer = dp[n-1][i]

    return -1 if answer == math.inf else answer


B = [[2, 1, 4],
     [1, 3, 1],
     [2, 3, 3]]
C = [[20, 15, 8],
     [13, 10, 4],
     [8,   6, 3]]
s = 5

print(parquet(B, C, s))
