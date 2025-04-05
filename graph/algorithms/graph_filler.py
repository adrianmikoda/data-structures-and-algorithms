# filling the adajcency list of a graph with vertices numbered starting from 0
import random


def fill_graph():
    is_directed = input("Is the graph directed? (Y/N): ").lower() == 'y'
    is_randomized = input("Randomize graph? (Y/N) ").lower() == 'y'

    vertices = int(input("Enter the number of vertices: "))
    edges = int(input("Enter the number of edges: "))
    adjacency_list = [[] for i in range(0, vertices)]

    if not is_randomized:
        for _ in range(edges):
            a, b = input("Enter an edge (a b): ").split()
            a, b = int(a), int(b)
            if b not in adjacency_list[a] and a != b:
                adjacency_list[a].append(b)
                if not is_directed:
                    adjacency_list[b].append(a)
    else:
        max_edges = vertices*(vertices-1)//2 if not is_directed else \
                    vertices*(vertices-1)
        if is_randomized and edges > max_edges:
            raise ValueError(f"Invalid edge count: {edges}",
                             f"Maximum allowed for this graph: {max_edges}")
        cntr = 0
        while cntr < edges:
            a = random.randint(0, vertices-1)
            b = random.randint(0, vertices-1)
            if b not in adjacency_list[a] and a != b:
                cntr += 1
                adjacency_list[a].append(b)
                if not is_directed:
                    adjacency_list[b].append(a)

    return (adjacency_list, is_directed)


if __name__ == "__main__":
    adjacency_list = fill_graph()
    n = len(adjacency_list)
    for i in range(n):
        print(f"{i}: {adjacency_list[i]}")
    print(f"\n{adjacency_list}")
