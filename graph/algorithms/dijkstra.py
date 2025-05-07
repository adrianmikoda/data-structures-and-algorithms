# implementation of the Dijkstra's Algorithm using adjacency list graph representation
# O(ElogV) time complexity
import graph_utils
from queue import PriorityQueue
import math


def dijkstra(adjacency_list, start):
    vertices = len(adjacency_list)
    d = [math.inf for i in range(vertices)]
    parent = [None for i in range(vertices)]

    pq = PriorityQueue()
    d[start] = 0

    pq.put((0, start))

    while not pq.empty():
        current_dist, u = pq.get()
        if current_dist > d[u]:
            continue

        d[u] = current_dist
        distance = current_dist+edge_length
        for v, edge_length in adjacency_list[u]:
            if distance < d[v]:
                parent[v] = u
                d[u] = distance
                pq.put((distance, v))

    return d, parent


# run test code only when script is executed directly (not imported)
if __name__ == "__main__":
    G = graph_utils.fill_graph(min_weight=0)[0]
    graph_utils.print_graph(G)

    s = int(input("Enter the starting vertex: "))
    answer = dijkstra(G, s)
    print(f"\nd: {answer[0]}")
    print(f"parent: {answer[1]}\n")
