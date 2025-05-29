# suboptimal solution
# O(RElogV) time complexity
from queue import PriorityQueue
import math


def flights_to_adjacency_list(flights):
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


def dijkstra(adjacency_list, start, blocked_vertices, resorts_marker, resorts_d):
    vertices = len(adjacency_list)
    d = [math.inf for _ in range(vertices)]
    parent = [None for _ in range(vertices)]
    pq = PriorityQueue()
    d[start] = 0
    pq.put((0, start))

    while not pq.empty():
        current_cost, current_vertex = pq.get()

        if current_cost > d[current_vertex]:
            continue

        for v, cost in adjacency_list[current_vertex]:
            if current_cost + cost < d[v] and blocked_vertices[v] is False:
                if resorts_marker[v] is not False:
                    resort_num = resorts_marker[v]
                    resorts_d[resort_num] = current_cost + cost
                d[v] = current_cost + cost
                parent[v] = current_vertex
                pq.put((current_cost+cost, v))


def choose_smallest_resort(resorts, resorts_marker, resorts_d):
    smallest_resort_num = 0
    smallest_resort_cost = math.inf
    for resort in resorts:
        if resorts_d[resorts_marker[resort]] < smallest_resort_cost:
            smallest_resort_num = resort
            smallest_resort_cost = resorts_d[resorts_marker[resort]]

    if smallest_resort_cost == math.inf:
        return -1
    return smallest_resort_num


def lets_roll(start_city, flights, resorts):
    adjacency_list = flights_to_adjacency_list(flights)
    resorts_count = len(resorts)
    vertices = len(adjacency_list)
    blocked_vertices = [False for _ in range(vertices)]
    resorts_marker = [False for _ in range(vertices)]
    for resort in range(resorts_count):
        resorts_marker[resorts[resort]] = resort

    sum = 0
    i = 0
    smallest_resort = -2
    while i < resorts_count and smallest_resort != -1:
        resorts_d = [math.inf for i in range(resorts_count)]
        dijkstra(adjacency_list, start_city, blocked_vertices, resorts_marker, resorts_d)
        smallest_resort = choose_smallest_resort(resorts, resorts_marker, resorts_d)
        if smallest_resort != -1:
            sum += ((resorts_d[resorts_marker[smallest_resort]])*2)
            blocked_vertices[smallest_resort] = True
        i += 1

    return sum
