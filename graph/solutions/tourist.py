# O(mlogn) time complexity
from queue import PriorityQueue


def G_to_adjacency_list(G):
    n = 0
    for u, v, p in G:
        n = v if v > n else n
    n += 1

    adjacency_list = [[] for _ in range(n)]
    for u, v, p in G:
        adjacency_list[u].append((v, p))
        adjacency_list[v].append((u, p))

    return n, adjacency_list


def dijkstra(D, L, n, adjacency_list):
    d = [[float('inf') for __ in range(5)] for _ in range(n)]

    d[D][0] = 0
    pq = PriorityQueue()
    pq.put((0, 0, D))

    while not pq.empty():
        current_distance, order, current_node = pq.get()
        if order > 3 or d[current_node][order] < current_distance:
            continue

        for v, p in adjacency_list[current_node]:
            if d[v][order+1] > current_distance + p:
                d[v][order+1] = current_distance + p
                pq.put((current_distance + p, order + 1, v))

    return d[L][4]


def tourist(G, D, L):
    n, adjacency_list = G_to_adjacency_list(G)
    return dijkstra(D, L, n, adjacency_list)


G = [(0, 1, 9), (0, 2, 1),
     (1, 2, 2), (1, 3, 8),
     (1, 4, 3), (2, 4, 7),
     (2, 5, 1), (3, 4, 7),
     (4, 5, 6), (3, 6, 8),
     (4, 6, 1), (5, 6, 1)]
D = 0
L = 6
print(tourist(G, D, L))