# O(nlogn) time complexity


def dfs(start, adajcency_list):
    n = len(adajcency_list)

    visited = [False for _ in range(n)]
    pre_order_time = [None for _ in range(n)]
    parent = [None for _ in range(n)]
    low = [float('inf') for _ in range(n)]
    is_articulation_point = [False for _ in range(n)]
    time = 0

    def dfs_visit(current_vertex):
        nonlocal time
        pre_order_time[current_vertex] = time = time + 1
        low[current_vertex] = pre_order_time[current_vertex]

        children_count = 0

        for v in adajcency_list[current_vertex]:
            if not visited[v]:
                children_count += 1
                parent[v] = current_vertex
                visited[v] = True
                low[current_vertex] = min(dfs_visit(v), low[current_vertex])

                if parent[current_vertex] is not None and low[v] >= pre_order_time[current_vertex]:
                    is_articulation_point[current_vertex] = True

            elif parent[current_vertex] is not v:
                low[current_vertex] = min(pre_order_time[v], low[current_vertex])

        if parent[current_vertex] is None and children_count > 1:
            is_articulation_point[current_vertex] = True

        return low[current_vertex]

    visited[start] = True
    dfs_visit(start)
    return is_articulation_point


def binsearch(array, value):
    left = 0
    right = len(array)

    while left < right:
        mid = left + (right - left) // 2
        if array[mid] == value:
            return None
        if array[mid] < value:
            left = mid + 1
        else:
            right = mid

    return left


def B_to_adjacency_list(B):
    n = -1
    for f, t in B:
        n = max(n, f, t)
    n += 1

    adjacency_list = [[] for _ in range(n)]

    for f, t in B:
        index = binsearch(adjacency_list[f], t)
        if index is not None:
            adjacency_list[f].insert(index, t)
        index = binsearch(adjacency_list[t], f)
        if index is not None:
            adjacency_list[t].insert(index, f)

    return n, adjacency_list


def railways(B):
    n, adjacency_list = B_to_adjacency_list(B)
    if n == 0: return 0

    is_articulation_point = dfs(0, adjacency_list)
    return sum(is_articulation_point)


B = [(3, 1), (0, 1), (4, 2),
     (1, 2), (0, 1), (2, 4),
     (2, 4), (0, 3), (2, 4),
     (1, 0), (2, 1)]
print(railways(B))
