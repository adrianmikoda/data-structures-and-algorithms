# O(V+E) time complexity
from collections import deque
import math


def bfs(adjacency_list, fungus_markers, B):
    n = len(adjacency_list)
    fungus_count = len(B)
    time = [math.inf for _ in range(n)]
    q = deque()

    for i in range(fungus_count):
        fungus_markers[B[i]] = i
        time[B[i]] = 0
        q.append(B[i])

    while q:
        u = q.popleft()

        for v in adjacency_list[u]:
            if time[v] > time[u] + 1:
                time[v] = time[u] + 1
                fungus_markers[v] = fungus_markers[u]
                q.append(v)
            elif time[v] == time[u] + 1 and fungus_markers[u] < fungus_markers[v]:
                fungus_markers[v] = fungus_markers


def mykoryza(G, T, d):
    n = len(G)
    markers = [math.inf for _ in range(n)]
    bfs(G, markers, T)
    answer = 0
    for i in markers:
        if i == d:
            answer += 1

    return answer


G = [[1, 3], [0, 2, 4], [1, 5],
     [0, 4, 6], [1, 3, 5, 7], [2, 4, 8],
     [3, 7], [4, 6, 8], [7, 5]]
T = [8, 2, 6]
d = 1
print(mykoryza(G, T, d))
