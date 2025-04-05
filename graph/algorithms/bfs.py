# implementation of the Breadth-First Search algorithm
from collections import deque
from graph_filler import fill_graph


def BFS(adjacency_list, s):
    n = len(adjacency_list)
    visited = [False for i in range(n)]
    distance = [0 for i in range(n)]
    parent = [0 for i in range(n)]

    q = deque()
    q.append(s)
    visited[s] = True

    while q:
        u = q.popleft()
        for v in adjacency_list[u]:
            if visited[v] is not True:
                visited[v] = True
                parent[v] = u
                distance[v] = distance[u]+1
                q.append(v)

    return (visited, distance, parent)


graph = fill_graph()
print(graph[0])
print(BFS(graph[0], 0))
