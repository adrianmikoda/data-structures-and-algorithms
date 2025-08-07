# O(VE + V^2) time complexity
from collections import deque


def edges_to_adjacency_list(V, E):
    adjaceny_list = [[] for _ in range(V)]
    for a, b in E:
        adjaceny_list[a].append(b)

    return adjaceny_list


def bfs(start, adjacency_list, visited):
    queue = deque()
    visited[start][start] = True
    queue.append(start)

    while queue:
        u = queue.popleft()
        for v in adjacency_list[u]:
            if not visited[start][v]:
                visited[start][v] = True
                queue.append(v)


def critical(V, E):
    adjacency_list = edges_to_adjacency_list(V, E)
    visited = [[False for _ in range(V)] for __ in range(V)]

    for start in range(V):
        bfs(start, adjacency_list, visited)

    answer = 0

    for a, b in E:
        flag = False
        for v in adjacency_list[a]:
            if v == b:
                continue
            if visited[v][b]:
                flag = True

        if not flag:
            answer += 1

    return answer


V = 4
E = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
print(critical(V, E))
