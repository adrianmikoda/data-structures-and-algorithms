# implementation of the Breadth-First Search algorithm using adjacency list graph representation
# O(V+E) time complexity
import graph_utils
from collections import deque


def BFS(adjacency_list, start):
    vertices = len(adjacency_list)
    visited = [False for i in range(vertices)]
    d = [0 for i in range(vertices)]
    parent = [None for i in range(vertices)]

    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        u = q.popleft()
        for v in adjacency_list[u]:
            if visited[v] is not True:
                visited[v] = True
                parent[v] = u
                d[v] = d[u]+1
                q.append(v)

    return visited, d, parent


if __name__ == "__main__":
    G = graph_utils.fill_graph(is_weighted=False)[0]
    graph_utils.print_graph(G)

    s = int(input("Enter the starting vertex: "))
    answer = BFS(G, s)
    print(f"\nvisited: {answer[0]}")
    print(f"d: {answer[1]}")
    print(f"parent: {answer[2]}\n")
