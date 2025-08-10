# optimal solution
# O(V^2logV)time complexity
from queue import PriorityQueue
import math


def dijkstra(start, adjacency_list, distance):
    pq = PriorityQueue()
    pq.put((0, start))
    while not pq.empty():
        current_cost, current_castle = pq.get()

        if distance[current_castle] < current_cost:
            continue

        for v, cost in adjacency_list[current_castle]:
            new_cost = current_cost + cost
            if distance[v] > new_cost:
                distance[v] = new_cost
                pq.put((new_cost, v))


def gold(G, V, s, t, r):
    n = len(V)
    adjacency_list = [[] for _ in range(n+n)]
    for u in range(n):
        for v, cost in G[u]:
            adjacency_list[u].append((v, cost))
            adjacency_list[u].append((u+n, -V[u]))
            adjacency_list[u+n].append((v+n, 2*cost + r))

    distance = [math.inf for _ in range(n+n)]
    dijkstra(s, adjacency_list, distance)

    return distance[t+n]


G = [[(1, 9), (2, 2)],
     [(0, 9), (3, 2), (4, 6)],
     [(0, 2), (3, 7), (5, 1)],
     [(1, 2), (2, 7), (4, 2), (5, 3)],
     [(1, 6), (3, 2), (6, 1)],
     [(2, 1), (3, 3), (6, 8)],
     [(4, 1), (5, 8)]]
V = [25, 30, 20, 15, 5, 10, 0]
s = 0
t = 6
r = 7
print(gold(G, V, s, t, r))
