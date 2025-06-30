# O(m) time complexity
from collections import deque
import math


def edges_to_adjacency_list(E):
    n = 0
    for u, v, length, r_type in E:
        n = max(n, u, v)
    n += 1
    adjacency_list = [[] for i in range(n)]
    for u, v, length, r_type in E:
        if r_type == 'P':
            adjacency_list[u].append((v, length, 1))
            adjacency_list[v].append((u, length, 1))
        else:
            adjacency_list[u].append((v, length, 0))
            adjacency_list[v].append((u, length, 0))
    return adjacency_list


def bfs(adjacency_list, d, start):
    q = deque()
    d[start][1] = 0
    d[start][0] = 0
    for v, cost, is_P in adjacency_list[start]:
        q.append((cost-1, cost, v, is_P))

    while q:
        counter, current_cost, u, u_is_P = q.popleft()
        if current_cost > d[u][u_is_P]:
            continue
        if counter > 0:
            q.append((counter-1, current_cost, u, u_is_P))
            continue

        for v, cost, is_P in adjacency_list[u]:
            addition = 0
            if u_is_P != is_P:
                addition = 20
            else:
                if u_is_P == 1:
                    addition = 10
                else:
                    addition = 5
            if d[v][is_P] > current_cost+cost+addition:
                q.append((cost+addition-1, current_cost+cost+addition, v, is_P))
                d[v][is_P] = current_cost+cost+addition


def tory_amos(E, A, B):
    adjacency_list = edges_to_adjacency_list(E)
    n = len(adjacency_list)
    d = [[math.inf, math.inf] for _ in range(n)]
    bfs(adjacency_list, d, A)
    return min(d[B][0], d[B][1])


E = [(0, 1, 5, 'P'), (1, 3, 1, 'I'), (3, 4, 1, 'I'),
 (2, 4, 1, 'P'), (2, 5, 1, 'I'), (0, 5, 5, 'P')]
A = 5
B = 3
print(tory_amos(E, A, B))