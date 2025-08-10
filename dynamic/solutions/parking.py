# O(nm) time complexity
# n - number of skyscrapers
# m - number of parking lots
import math

def parking(X, Y):
    n = len(X)
    m = len(Y)
    f = [[math.inf for __ in range(m)] for _ in range(n)]

    f[0][0] = abs(X[0] - Y[0])
    for p in range(1, m):
        f[0][p] = abs(X[0] - Y[p])
        f[0][p] = f[0][p-1] if f[0][p-1] < f[0][p] else f[0][p]

    for s in range(1, n):
        for p in range(s, m):
            f[s][p] = min(f[s-1][p-1] + abs(X[s] - Y[p]), f[s][p-1])
            
    return f[n-1][m-1]


X = [3,6,10,14]
Y = [1,4,5,10,11,13,17]
print(parking(X, Y))