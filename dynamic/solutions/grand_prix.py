# O(nk) time complexity
import math


def grand_prix(D, C, k, s):
    D.append(s)
    n = len(D)
    dp = [[math.inf for __ in range(k+1)] for _ in range(n)]
    
    if k-D[0] >= 0:
        dp[0][k-D[0]] = 0
    for jump in range(0, 3):
        if jump < n:
            dp[jump][0] = 0

    for station in range(n-1):
        for fuel in range(k+1):

            if fuel >= 0:
                dp[station][fuel] = min(dp[station][fuel], dp[station][fuel-1] + C[station])

            if dp[station][fuel] == math.inf:
                continue

            fuel_need = D[station+1] - D[station]
            resulting_fuel = fuel - fuel_need
            if resulting_fuel >= 0:
                dp[station+1][resulting_fuel] = min(dp[station+1][resulting_fuel], dp[station][fuel])

            if fuel == k:
                for jump in range(1, 4):
                    if station + jump < n:
                        dp[station+jump][0] = min(dp[station+jump][0], dp[station][fuel])
                    else:
                        break

    return min(dp[n-1])


D = [2, 6, 8, 9, 11, 12]
C = [5, 3, 1, 4, 2, 9]
k = 5
s = 15
print(grand_prix(D, C, k, s))
