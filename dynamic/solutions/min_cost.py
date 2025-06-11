# O(n^2) time complexity
import math


def min_cost(O, C, T, L):
    n = len(O)
    parkings = [(O[i], C[i]) for i in range(n)]
    parkings.append((0, 0))
    parkings.append((L, 0))
    parkings = sorted(parkings)
    n += 2

    dp = [[math.inf for _ in range(n)] for __ in range(2)]
    dp[0][0] = 0
    dp[1][0] = 0

    for parking_num in range(1, n):
        for rest_point_num in range(parking_num):
            if parkings[parking_num][0] - parkings[rest_point_num][0] <= T:
                dp[0][parking_num] = min(dp[0][parking_num], dp[0][rest_point_num] + parkings[parking_num][1])
                dp[1][parking_num] = min(dp[1][parking_num], dp[1][rest_point_num] + parkings[parking_num][1])
            elif parkings[parking_num][0] - parkings[rest_point_num][0] <= 2*T:
                dp[1][parking_num] = min(dp[1][parking_num], dp[0][rest_point_num] + parkings[parking_num][1])

    return min(dp[0][n-1], dp[1][n-1])


print(min_cost([17, 20, 11, 5, 12], [9, 7, 7, 7, 3], 7, 25))
