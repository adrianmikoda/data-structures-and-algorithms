# implementation of the solution using modified Dijkstra's Algorithm with exhaustion level tracking
# O(ElogV) time complexity

import math
from queue import PriorityQueue
from kol2testy import runtests


def edges_to_adjacency_list(G):
    vertices = 0

    for u, v, weight in G:
        vertices = v if v > vertices else vertices
        vertices = u if u > vertices else vertices

    vertices += 1
    adjacency_list = [[] for i in range(vertices)]

    for u, v, weight in G:
        adjacency_list[u].append((v, weight))
        adjacency_list[v].append((u, weight))

    return adjacency_list, vertices


def warrior(G, s, t):
    adjacency_list, vertices = edges_to_adjacency_list(G)

    # d[vertex][exhaustion (0-16)]
    d = [[math.inf for i in range(17)] for i in range(vertices)]

    pq = PriorityQueue()

    pq.put((0, 0, s))  # cost, exhaustion, vertex
    d[s][0] = 0

    while not pq.empty():
        current_cost, current_exhaustion, current_vertex = pq.get()
        if current_cost > d[current_vertex][current_exhaustion]:
            continue
        if current_vertex == t:
            break

        for v, weight in adjacency_list[current_vertex]:
            exhaustion = current_exhaustion + weight

            # without rest
            if exhaustion <= 16:
                cost = current_cost + weight
                if d[v][exhaustion] > cost:
                    d[v][exhaustion] = cost
                    pq.put((cost, exhaustion, v))

            # with rest
            exhaustion = weight
            weight += 8
            cost = current_cost + weight
            if d[v][exhaustion] > cost:
                d[v][exhaustion] = cost
                pq.put((cost, exhaustion, v))

    minimum = math.inf
    for cost in d[t]:
        minimum = cost if cost < minimum else minimum

    return minimum


runtests(warrior, all_tests=True)
