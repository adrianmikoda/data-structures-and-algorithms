# O(n^2) time complexity
import math
from queue import PriorityQueue


def adjacency_matrix_to_adjacency_list(n, G):
    adjacency_list = [[] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            if G[a][b] != -1:
                adjacency_list[a].append((b, G[a][b]))
    return adjacency_list


def dijkstra(start, adjacency_list, d):
    pq = PriorityQueue()
    d[start][16] = 0
    pq.put((0, 16, start))

    while not pq.empty():
        current_time, remaining_hours, current_node = pq.get()
        if d[current_node][remaining_hours] < current_time:
            continue

        # without rest
        for v, time in adjacency_list[current_node]:
            new_remaining_hours = remaining_hours - time
            if new_remaining_hours >= 0 and d[v][new_remaining_hours] > current_time + time:
                d[v][new_remaining_hours] = current_time + time
                pq.put((current_time + time, new_remaining_hours, v))

        # with rest
        remaining_hours = 16
        current_time += 8
        for v, time in adjacency_list[current_node]:
            new_remaining_hours = remaining_hours - time
            if new_remaining_hours >= 0 and d[v][new_remaining_hours] > current_time + time:
                d[v][new_remaining_hours] = current_time + time
                pq.put((current_time + time, new_remaining_hours, v))


def goodknight(G, s, t):
    n = len(G)
    adjacency_list = adjacency_matrix_to_adjacency_list(n, G)

    d = [[math.inf for _ in range(17)] for __ in range(n)]
    dijkstra(s, adjacency_list, d)

    answer = math.inf
    for time in d[t]:
        answer = time if time < answer else answer

    return answer


G = [[-1, 3, 8,-1,-1,-1],
     [ 3,-1, 3, 6,-1,-1],
     [ 8, 3,-1,-1, 5,-1],
     [-1, 6,-1,-1, 7, 8],
     [-1,-1, 5, 7,-1, 8],
     [-1,-1,-1, 8, 8,-1]]
s = 0
t = 5
print(goodknight(G, s, t))
