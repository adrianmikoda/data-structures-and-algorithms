# implementation of the Topological Sort algorithm for a directed and acyclic graph
from graph_filler import fill_graph
from collections import deque


def dfs(adjacency_list, current, visited, order):
    for v in adjacency_list[current]:
        if not visited[v]:
            visited[v] = True
            dfs(adjacency_list, v, visited, order)

    order.appendleft(current)


def topological_sort(adjacency_list):
    vertices = len(adjacency_list)
    visited = [False for i in range(vertices)]
    topological_order = deque()

    for vertex in range(0, vertices):
        if not visited[vertex]:
            visited[vertex] = True
            dfs(adjacency_list, vertex, visited, topological_order)
    return topological_order


print(topological_sort([[1, 2], [], [6], [], [], [7], [], []]))
