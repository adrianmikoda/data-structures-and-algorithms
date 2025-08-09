# suboptimal solution
# O(n^2) time complexity


def uncool(P):
    n = len(P)
    for i in range(n):
        for j in range(i+1, n):
            a = P[i]
            b = P[j]

            if a[1] < b[0] or b[1] < a[0]:
                continue
            if (b[0] <= a[0] and a[1] <= b[1]) or (a[0] <= b[0] and b[1] <= a[1]):
                continue
            else:
                return (i, j)


P = [[1, 3], [6, 7], [2, 6], [4, 6], [1, 8], [5, 10]]
print(uncool(P))
