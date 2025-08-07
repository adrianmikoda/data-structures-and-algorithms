# O(n + m) time complexity
from collections import deque


def battle(P, K, R):
    n = len(K)
    m = len(P)
    markers = [None for _ in range(4*n + 4*m)]
    for i in range(m):
        markers[P[i]] = 0
    for i in range(n):
        markers[K[i]] = R[i]

    answer = 0
    stack = deque()

    for i in range(4*n + 4*m):
        if markers[i] and markers[i] > 0:
            stack.append((i, markers[i]))
        elif markers[i] == 0:
            while stack:
                pos, r = stack.pop()
                if r >= i-pos:
                    answer += 1
                    break

    return answer


P = [14, 16, 0, 6, 10, 8]
K = [2, 12, 4]
R = [8, 5, 3]
print(battle(P, K, R))
