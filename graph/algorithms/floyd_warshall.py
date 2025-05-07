# Implementation of the Floyd Warshall Algorithm using matrix graph representation
# O(V^3) time complexity
import math


def reconstruct_path(i, j, parent):
    if parent[i][j] is None:
        return []
    path = [j]
    while j != i:
        j = parent[i][j]
        path.append(j)
    path.reverse()
    return path


def floyd_warshall(adjacency_matrix):
    vertices = len(adjacency_matrix)
    distance_matrix = [row[:] for row in adjacency_matrix]
    parent_matrix = [[j if adjacency_matrix[i][j] != math.inf else None for j in range(vertices)] for i in range(vertices)]

    for k in range(vertices):
        for u in range(vertices):
            for v in range(vertices):
                s = distance_matrix[u][k] + distance_matrix[k][v]
                if s < distance_matrix[u][v]:
                    distance_matrix[u][v] = s
                    parent_matrix[u][v] = parent_matrix[k][v]

    for row in distance_matrix:
        print(row)

    print('/n')
    for row in parent_matrix:
        print(row)

i = math.inf
G = [# 0, 1, 2, 3, 4
      [0, -4,i, i, i], #0
      [i, 0, 4, 5, i], #1
      [i, i, 0, 2, i], #2
      [i, i, i, 0, 3], #3
      [i, i, i, i, 0], #4
]

floyd_warshall(G)
