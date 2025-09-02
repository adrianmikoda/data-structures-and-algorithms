# O(n^3) time complexity
import math

def G_to_adjacency_matrix(G):
    n = len(G)
    adjacency_matrix = [[math.inf for __ in range(n)] for _ in range(n)]

    for u in range(n):
        for v, d in G[u]:
            adjacency_matrix[u][v] = d

    return n, adjacency_matrix


def robot(G, P):
    n, adjacency_matrix = G_to_adjacency_matrix(G)
    distance_matrix = [row[:] for row in adjacency_matrix]

    for k in range(n):
        for u in range(n):
            for v in range(n):
                s = distance_matrix[u][k] + distance_matrix[k][v]
                if s < distance_matrix[u][v]:
                    distance_matrix[u][v] = s

    previous = P[0]
    P_length = len(P)
    answer = 0
    for i in range(1, P_length):
        current = P[i]
        answer += distance_matrix[previous][current]
        previous = current

    return answer


G = [[(1, 3), (2, 3)],
     [(0, 3), (4, 4)],
     [(0, 3), (3, 1), (4, 4)],
     [(2, 1), (4, 2)],
     [(1, 4), (2, 4), (3, 2)]]
P = [0, 3, 4]
print(robot(G, P))
