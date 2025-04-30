# implementation of the Bellman-Ford Algorithm using adjacency list graph representation
# O(VE) time complexity
import graph_utils
import math


def bellman_ford(adjacency_list, start):
    vertices = len(adjacency_list)
    d = [math.inf for i in range(vertices)]
    parent = [None for i in range(vertices)]

    d[start] = 0
    for _ in range(vertices-1):
        for v in range(vertices):
            for u, edge_length in adjacency_list[v]:
                if d[v] + edge_length < d[u]:
                    d[u] = d[v] + edge_length
                    parent[u] = v

    for v in range(vertices):
        for u, edge_length in adjacency_list[v]:
            if d[u] > d[v] + edge_length:
                print("found negative weight cycle")

    return d, parent


# run test code only when script is executed directly (not imported)
if __name__ == "__main__":
    G = graph_utils.fill_graph()[0]
    graph_utils.print_graph(G)

    s = int(input("Enter the starting vertex: "))
    answer = bellman_ford(G, s)
    print(f"\nd: {answer[0]}")
    print(f"parent: {answer[1]}\n")
