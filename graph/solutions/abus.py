# O(ElogV) time complexity
import heapq


def kr_to_adjacency_list(kr):
    n = 0
    for u, v, w in kr:
        if u > n: n = u
        if v > n: n = v
    n += 1
    adjacency_list = [[] for _ in range(n)]
    for u, v, w in kr:
        adjacency_list[u].append((v, w))
        adjacency_list[v].append((u, w))

    return n, adjacency_list


def dijkstra(s, t, b, n, adjacency_list, OD):
    if t == s:
        return 0
    if t >= n:
        return -1

    refills = [float('inf') for _ in range(n)]
    refills [s] = 0
    pq = []
    heapq.heappush(pq, (0, 0, 0, s))

    while pq:
        refill_count, current_water_amount, current_time, current_node = heapq.heappop(pq)
        if refill_count > refills[current_node]:
            continue
        if current_node == t:
            continue

        for v, w in adjacency_list[current_node]:
            interval = OD[current_node]
            wait_time = (interval - (current_time % interval)) % interval
            water_amount = current_water_amount - wait_time
            if water_amount < 0:
                water_amount = 0

            time = current_time + wait_time
            water_left = water_amount - w

            if water_left >= 0:
                if refills[v] > refill_count:
                    refills[v] = refill_count
                    heapq.heappush(pq, (refill_count, water_left, time + w, v))
            else:
                if refills[v] > refill_count + 1:
                    refills[v] = refill_count + 1
                    heapq.heappush(pq, (refill_count + 1, max(b-w, 0), time + w, v))

    return refills[t] if refills[t] != float('inf') else -1


def abus(KR, OD, b, s, t):
    n, adjacency_list = kr_to_adjacency_list(KR)
    return dijkstra(s, t, b, n, adjacency_list, OD)


KR = [(0, 4, 4), (0, 1, 7), (1, 3, 6), (4, 3, 2), (1, 2, 1), (3, 2, 3)]
OD = [1, 6, 1, 8, 4]
b = 10
s = 0
t = 2
print(abus(KR, OD, b, s, t))
