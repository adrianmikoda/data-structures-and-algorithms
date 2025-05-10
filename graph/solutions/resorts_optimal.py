# optimal solution
# O(ElogV) time complexity
from queue import PriorityQueue
import math


def flights_to_adjacency_list(flights):  # O(E)
    max_n = 0
    for u, v, c in flights:
        max_n = u if u > max_n else max_n
        max_n = v if v > max_n else max_n
    vertices = max_n+1
    adjacency_list = [[] for _ in range(vertices)]
    for u, v, c in flights:
        adjacency_list[u].append((v, c))
        adjacency_list[v].append((u, c))

    return adjacency_list


def dijkstra(adjacency_list, start, resorts_marker, resorts_d):   # O(ElogV)
    vertices = len(adjacency_list)
    d = [math.inf for _ in range(vertices)]
    parent = [None for _ in range(vertices)]
    pq = PriorityQueue()
    d[start] = 0
    pq.put((0, start))

    while not pq.empty():
        current_cost, current_vertex = pq.get()
        for v, cost in adjacency_list[current_vertex]:
            if current_cost + cost < d[v]:
                if resorts_marker[v] is not False:
                    resort_num = resorts_marker[v]
                    resorts_d[resort_num] = current_cost + cost
                else:
                    pq.put((current_cost+cost, v))
                d[v] = current_cost + cost
                parent[v] = current_vertex


def lets_roll(start_city, flights, resorts):
    adjacency_list = flights_to_adjacency_list(flights)
    resorts_count = len(resorts)
    vertices = len(adjacency_list)
    resorts_marker = [False for _ in range(vertices)]
    for resort in range(resorts_count):
        resorts_marker[resorts[resort]] = resort
    resorts_d = [math.inf for i in range(resorts_count)]

    sum = 0
    dijkstra(adjacency_list, start_city, resorts_marker, resorts_d)
    for i in resorts_d:
        if i != math.inf:
            sum += (i*2)
    return sum
