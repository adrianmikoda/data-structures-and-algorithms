# implementation of the Bridge Find Algorithm using the low function
import math
import graph_utils


def dfs(adjacency_list):
    vertices = len(adjacency_list)
    parent = [None for _ in range(vertices)]
    pre_order = [None for _ in range(vertices)]
    low = [math.inf for _ in range(vertices)]
    pre_order_time = 0

    def dfs_visit(current_vertex):
        nonlocal pre_order_time
        pre_order[current_vertex] = pre_order_time = pre_order_time + 1
        low[current_vertex] = pre_order[current_vertex]

        for v in adjacency_list[current_vertex]:
            if pre_order[v] is None:
                parent[v] = current_vertex
                temp = dfs_visit(v)
                low[current_vertex] = temp if temp < low[current_vertex] else low[current_vertex]
            elif v is not parent[current_vertex]:
                low[current_vertex] = pre_order[v] if pre_order[v] < low[current_vertex] else low[current_vertex]

        return low[current_vertex]

    dfs_visit(0)

    return pre_order, parent, low


def find_bridge(adjacency_list):
    vertices = len(adjacency_list)
    pre_order, parent, low = dfs(adjacency_list)
    bridge_list = []

    for vertex in range(vertices):
        if parent[vertex] is not None and pre_order[vertex] == low[vertex]:
            bridge_list.append((parent[vertex], vertex))

    print(parent)
    print(pre_order)
    print(low)
    return bridge_list


G = graph_utils.fill_graph(is_directed=False, is_weighted=False)[0]
graph_utils.print_graph(G)
print(f"\nBridge list: {find_bridge(G)}")
