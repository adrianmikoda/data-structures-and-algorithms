# optimal solution
# O(V^2logV)time complexity
from queue import PriorityQueue
import math


def dijkstra(start, G, r, flag):
    n = len(G)
    pq = PriorityQueue()
    distance = [math.inf for _ in range(n)]
    distance[start] = 0
    pq.put((0, start))
    while not pq.empty():
        current_cost, current_castle = pq.get()

        if distance[current_castle] < current_cost:
            continue

        if not flag:
            for v, cost in G[current_castle]:
                new_cost = current_cost + cost
                if distance[v] > new_cost:
                    distance[v] = new_cost
                    pq.put((new_cost, v))

        if flag:
            for v, cost in G[current_castle]:
                new_cost = current_cost + 2*cost + r
                if distance[v] > new_cost:
                    distance[v] = new_cost
                    pq.put((new_cost, v))

    return distance


def gold(G, V, s, t, r):
    n = len(V)

    answer = math.inf
    distance_from_s = dijkstra(s, G, r, False)
    distance_to_t = dijkstra(t, G, r, True)

    for robbed_castle in range(n):
        total_cost = distance_from_s[robbed_castle] - V[robbed_castle] + distance_to_t[robbed_castle]

        answer = total_cost if total_cost < answer else answer

    return answer


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
