# filling the adajcency list of a graph with vertices numbered starting from 0
import random


def fill_graph(is_directed=None,
               is_randomized=None,
               is_weighted=None,
               vertex_count=None,
               edge_count=None,
               max_weight=None,
               ):
    if is_directed == None:
        is_directed = input("Is the graph directed? (Y/N): ").lower() == 'y'
    else:
        print(f"is_directed parameter has already been set to {is_directed}")
    if is_weighted == None:
        is_weighted = input("Is the graph weighted? (Y/N): ").lower() == 'y'
    else:
        print(f"is_weighted parameter has already been set to {is_weighted}")
    if is_randomized == None:
        is_randomized = input("Randomize graph? (Y/N): ").lower() == 'y'
    else:
        print(f"is_randomized parameter has already been set to {is_randomized}")
    if vertex_count == None:
        vertex_count = int(input("Enter the number of vertices: "))
    else:
        print(f"vertex_count parameter has already been set to {vertex_count}")
    if edge_count == None:
        edge_count = int(input("Enter the number of edges: "))
    else:
        print(f"edge_count parameter has already been set to {edge_count}")
    adjacency_list = [[] for i in range(0, vertex_count)]

    if not is_randomized:
        for _ in range(edge_count):
            a, b = input("Enter an edge (a b): ").split()
            a, b = int(a), int(b)
            a_input = b
            b_input = a

            if is_weighted:
                weight = int(input("Enter weight for this edge: "))
                if weight < 0:
                    raise ValueError(f"Invalid weight: {weight} " +
                                     f"minimum allowed is 0")
                a_input = [b, weight]
                b_input = [a, weight]

            if b not in adjacency_list[a] and a != b:
                adjacency_list[a].append(a_input)
                if not is_directed:
                    adjacency_list[b].append(b_input)
    else:
        max_edge_count = vertex_count*(vertex_count-1)//2 if not is_directed else \
                    vertex_count*(vertex_count-1)
        if is_randomized and edge_count > max_edge_count:
            raise ValueError(f"Invalid edge count: {edge_count} " +
                             f"maximum allowed for this graph: {max_edge_count}")
        cntr = 0


        if is_weighted:
            if max_weight == None:
                max_weight = int(input("Enter max weight: "))
            else:
                print(f"max_weight parameter has already been set to {max_weight}")

        if max_weight < 0:
            raise ValueError(f"Invalid max weight: {max_weight} " +
                             f"minimum allowed is 0")

        while cntr < edge_count:
            a = random.randint(0, vertex_count-1)
            b = random.randint(0, vertex_count-1)
            a_input = b
            b_input = a
            if is_weighted:
                weight = random.randint(0, max_weight)
                a_input = [b, weight]
                b_input = [a, weight]

            new_edge = True
            for edge in adjacency_list[a]:
                if is_weighted and a_input[0] == edge[0]:
                    new_edge = False
                    break
                if not is_weighted and a_input == edge:
                    new_edge = False
                    break

            if new_edge and a_input not in adjacency_list[a] and a != b:
                cntr += 1
                adjacency_list[a].append(a_input)
                if not is_directed:
                    adjacency_list[b].append(b_input)

    return (adjacency_list, is_directed)


if __name__ == "__main__":
    adjacency_list = fill_graph()[0]
    n = len(adjacency_list)
    for i in range(n):
        print(f"{i}: {adjacency_list[i]}")
