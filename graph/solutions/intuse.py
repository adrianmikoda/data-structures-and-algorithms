# O(n) time complexity
from collections import defaultdict
from collections import deque


def I_to_adjaceny_list(I, length):
    adjacency_list_x_to_y = defaultdict(list)
    adjacency_list_y_to_x = defaultdict(list)

    for i in range(length):
        a, b = I[i]
        adjacency_list_x_to_y[a].append(b)
        adjacency_list_y_to_x[b].append(a)

    return adjacency_list_x_to_y, adjacency_list_y_to_x


def bfs(start, adjacency_list, can_reach):
    visited = set()
    queue = deque()
    queue.append(start)
    visited.add(start)

    while queue:
        u = queue.popleft()
        can_reach[u] = True
        for v in adjacency_list[u]:
            if v not in visited:
                visited.add(v)
                queue.append(v)


def intuse(I, x, y):
    length = len(I)
    adjacency_list_x_to_y, adjacency_list_y_to_x = I_to_adjaceny_list(I, length)

    can_x_reach = defaultdict(bool)
    can_y_reach = defaultdict(bool)

    bfs(x, adjacency_list_x_to_y, can_x_reach)
    bfs(y, adjacency_list_y_to_x, can_y_reach)

    answer = []
    for i in range(length):
        if can_x_reach[I[i][0]] and can_y_reach[I[i][1]]:
            answer.append(i)

    return answer


I = [(3, 4), (2, 5), (1, 3), (4, 6), (1, 4)]
x = 1
y = 6
print(intuse(I, x, y))
