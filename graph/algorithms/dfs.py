# implementation of the Depth-First Search algorithm using adjacency list graph representation
# O(V+E) time complexity
import graph_utils


def dfs(adjacency_list, start):
    vertices = len(adjacency_list)
    visited = [False for _ in range(vertices)]
    parent = [None for _ in range(vertices)]
    pre_order = [0 for _ in range(vertices)]
    post_order = [0 for _ in range(vertices)]
    pre_order_time = 0
    post_order_time = 0

    def dfs_visit(current_vertex):
        nonlocal pre_order_time
        nonlocal post_order_time
        visited[current_vertex] = True
        pre_order[current_vertex] = pre_order_time = pre_order_time + 1

        for u in adjacency_list[current_vertex]:
            if not visited[u]:
                parent[u] = current_vertex
                dfs_visit(u)

        post_order[current_vertex] = post_order_time = post_order_time + 1

    dfs_visit(start)

    return visited, parent, pre_order, post_order


# run test code only when script is executed directly (not imported)
if __name__ == "__main__":
    G = graph_utils.fill_graph(is_weighted=False)[0]
    graph_utils.print_graph(G)

    s = int(input("Enter the starting vertex: "))
    answer = dfs(G, s)
    print(f"\nvisited: {answer[0]}")
    print(f"parent: {answer[1]}")
    print(f"pre_order: {answer[2]}")
    print(f"post_order: {answer[3]}\n")
