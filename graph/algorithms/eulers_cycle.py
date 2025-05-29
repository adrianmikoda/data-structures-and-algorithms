# implementation of finding the Eulers Cycle using dfs on a connected and undirected graph
from collections import deque


def dfs(adjacency_list, current, deleted_edges, order):
    for v in adjacency_list[current]:
        edge  = (current, v) if current < v else (v,current)

        if edge not in deleted_edges:
            deleted_edges.append(edge)
            dfs(adjacency_list, v, deleted_edges, order)
    order.appendleft(current)


def find_eulers_cycle(adjacency_list):
    for adjacent_vertices in adjacency_list:
        if len(adjacent_vertices) % 2 != 0:
            return False
        
    vertices = len(adjacency_list)
    adjacency_matrix = [[0 for _ in range(vertices)] for __ in range(vertices)]
    order = deque()
    for adjacent_vertices in adjacency_list:
        if len(adjacent_vertices) % 2 != 0:
            return False
        
    dfs(adjacency_list, 0, [], order)
    return order


print(find_eulers_cycle([[5,3], [4,5,3,2], [1,5], [1,5,0,4], [1,3], [0,3,1,2]]))





