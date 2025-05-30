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

    for w in range(1, n):
        for p in range(w, m):
            f[w][p] = min(f[w-1][p-1] + abs(X[w] - Y[p]), f[w][p-1])
    for row in f:
        print(row)
    return f[n-1][m-1]

print(parking([3,6,10,14], [1,4,5,10,11,13,17]))