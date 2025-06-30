# O(ElogV) time complexity
from queue import PriorityQueue
import math


def edges_to_adjacency_list(G):
    n = 0
    for u, v, weigth in G:
        n = max(n, u, v)
    n += 1
    adjacency_list = [[] for _ in range(n)]
    for u, v, weight in G:
        adjacency_list[u].append((v, weight))
        adjacency_list[v].append((u, weight))
    return adjacency_list


def dijkstra(adjacency_list, d, start):
    n = len(adjacency_list)
    parent = [None for _ in range(n)]
    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        current_weight, u = pq.get()
        if current_weight > d[u]:
            continue
        d[u] = current_weight

        for v, weight in adjacency_list[u]:
            if current_weight+weight < d[v]:
                pq.put((current_weight+weight, v))


def armstrong(B, G, s, t):
    adjacency_list = edges_to_adjacency_list(G)
    n = len(adjacency_list)

    d_from_start = [math.inf for _ in range(n)]
    d_from_end = [math.inf for _ in range(n)]
    dijkstra(adjacency_list, d_from_start, s)
    dijkstra(adjacency_list, d_from_end, t)

    answer = d_from_start[t]
    for i, p, q in B:
        answer = min(answer, d_from_start[i] + d_from_end[i] * (p/q))
    return int(answer)

B = [ (1, 1, 2), (2, 2, 3) ]
G = [ (0,1,6), (1,4,7), (4,3,4),
 (3,2,4), (2,0,3), (0,3,6) ]
s = 0
t = 4
print(armstrong(B, G, s, t))