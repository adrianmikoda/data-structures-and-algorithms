# O(n) time complexity


def dominance(P):
    n = len(P)
    T = [[0 for _ in range(n+1)] for __ in range(2)]

    for point in P:
        T[0][point[0]] += 1
        T[1][point[1]] += 1

    for i in range(n-1, -1, -1):
        T[0][i] += T[0][i+1]
        T[1][i] += T[1][i+1]

    counter = n
    for point in P:
        counter = min(counter, T[0][point[0]] + T[1][point[1]] - 2)

    return n-counter-1


P = [(1, 3), (3, 4), (4, 2), (2, 2)]
print(dominance(P))
