# O(n^2) time complexity
import math


def orchard(T, m):
    n = len(T)
    dp = [[math.inf for _ in range(m)] for __ in range(n+1)]
    sum = 0

    for value in T:
        sum += value
    dp[0][sum % m] = 0

    for tree_count in range(1, n+1):
        for modulo in range(0, m):
            dp[tree_count][modulo] = min(dp[tree_count][modulo], dp[tree_count-1][modulo])
            target_modulo = (modulo-T[tree_count-1]) % m
            dp[tree_count][target_modulo] = min(dp[tree_count][target_modulo], dp[tree_count-1][modulo]+1)

    return dp[n][0]

T = [2, 2, 7, 5, 1, 14, 7]
m = 7
print(orchard(T, m))
