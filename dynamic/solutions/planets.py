# O(nE) time complexity
import math


def planets(D, C, T, E):
    n = len(D)
    dp = [[math.inf for _ in range(E+1)] for __ in range(n)]
    dp[0][0] = 0

    for planet in range(0, n):
        for fuel in range(0, E+1):
            distance = D[planet] - D[planet-1]
            if planet > 0 and fuel + distance <= E:
                dp[planet][fuel] = min(dp[planet][fuel], dp[planet-1][fuel+distance])
            if fuel > 0:
                dp[planet][fuel] = min(dp[planet][fuel], dp[planet][fuel-1] + C[planet])
            else:
                destination, cost = T[planet]
                dp[destination][0] = min(dp[destination][0], dp[planet][0] + cost)

    answer = math.inf
    for cost in dp[n-1]:
        answer = cost if cost < answer else answer

    return answer


D = [0, 5, 10, 20]
C = [2, 1, 3, 9]
T = [(2, 3), (3, 7), (2, 10), (3, 10)]
E = 10
print(planets(D, C, T, E))
