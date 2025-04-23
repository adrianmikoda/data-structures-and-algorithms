# implementation of the Dijkstra's Algorithm

from queue import PriorityQueue
import math

pq = PriorityQueue()


def num_gen(value=0):
    while True:
        yield value
        value += 1


order = num_gen()
# edge (target, cost)
G = [[(1, 6), (5, 10)], [], [(3, 20)], [], [], [(2, 10), (4, 8)]]


def dijkstra(adjacency_list, start):
    vertices = len(adjacency_list)
    d = [math.inf for i in range(vertices)]
    parent = [-1 for i in range(vertices)]
    d[start] = 0

    pq = PriorityQueue()
    pq.put((0, next(order), start))

    while not pq.empty():
        current = pq.get()
        u = current[2]
        for v, cost in adjacency_list[u]:
            if d[u] + cost < d[v]:
                d[v] = d[u] + cost
                parent[v] = u
                pq.put((cost, next(order), v))

    print(f"d: {d}")
    print(f"parent: {parent}")


dijkstra(G, 0)
