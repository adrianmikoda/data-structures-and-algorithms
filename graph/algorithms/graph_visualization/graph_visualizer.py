# visualisation of a graph given in the adjacency_list form using pyvis library
from collections import deque
import colorsys
import random
import webbrowser

try:
    import pyvis
    from pyvis.network import Network
except ModuleNotFoundError:
    print("Error: pyvis is NOT installed.")
    print("Please run 'python -m pip install pyvis'")
    quit()


def fill_graph(is_directed=None,
               is_randomized=None,
               is_weighted=None,
               vertex_count=None,
               edge_count=None,
               min_weight=None,
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
            if min_weight == None:
                min_weight = int(input("Enter min weight: "))
            else:
                print(f"min_weight parameter has already been set to {min_weight}")
            if max_weight == None:
                max_weight = int(input("Enter max weight: "))
            else:
                print(f"max_weight parameter has already been set to {max_weight}")
            
            if max_weight < min_weight:
                raise ValueError(f"Invalid max weight: {max_weight} " +
                                 f"max_weight parameter cannot be less than min_weight")

        while cntr < edge_count:
            a = random.randint(0, vertex_count-1)
            b = random.randint(0, vertex_count-1)
            a_input = b
            b_input = a
            if is_weighted:
                weight = random.randint(min_weight, max_weight)
                a_input = (b, weight)
                b_input = (a, weight)

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


def BFS(adjacency_list, s, color_nr, colors):
    q = deque()
    q.append(s)
    colors[s] = color_nr
    while q:
        u = q.popleft()
        for v, weight in adjacency_list[u]:
            if colors[v] != color_nr:
                colors[v] = color_nr
                q.append(v)
    return colors


def generate_colors(n):
    golden_ratio_conjugate = 0.61803398875
    color_palette = []
    hue = random.random()
    for _ in range(n):
        hue += golden_ratio_conjugate
        hue %= 1
        rgb = colorsys.hsv_to_rgb(hue, 0.7, 1)
        hex_color = "#{:02x}{:02x}{:02x}".format(
            int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255)
        )
        color_palette.append(hex_color)
    return color_palette


def visualize_graph(G, vertices, is_directed):
    adjacency_list = G[0]
    is_directed = G[1]
    colors = [-1 for i in range(len(adjacency_list))]
    n = len(adjacency_list)

    color_nr = -1
    for i in range(0, vertices):
        if colors[i] == -1:
            color_nr += 1
            BFS(adjacency_list, i, color_nr, colors)
    color_palette = generate_colors(color_nr+1)

    graph = Network(notebook=True,
                    directed=is_directed,
                    cdn_resources='remote')

    for i in range(0, vertices):
        graph.add_node(f'{i}', color=color_palette[colors[i]], color_background="white")
    for i in range(0, vertices):
        for j in adjacency_list[i]:
            if is_directed:
                if(type(j) == tuple):
                    graph.add_edge(f'{i}', f'{j[0]}', color='black', label=f"{j[1]}", arrows="to") 
                else:
                    graph.add_edge(f'{i}', f'{j[0]}', color='black', arrows="to")
            else:
                if(type(j) == tuple):
                    graph.add_edge(f'{i}', f'{j[0]}', color='black', label=f"{j[1]}") 
                else:
                    graph.add_edge(f'{i}', f'{j}', color='black')
            

    graph.repulsion(node_distance=100,
                    central_gravity=0.7,
                    spring_length=200,
                    spring_strength=0.05,
                    damping=0.09)
    graph.show_buttons(filter_='physics')

    open_file = input(("Open the graph visualization file? (Y/N): ")).lower() == 'y'
    if open_file:
        path = __file__.rsplit('\\', 1)[0]
        graph.show(path+'\\graph.html')
        webbrowser.open(path+'\\graph.html')

graph = fill_graph()
n = len(graph[0])
for i in range(n):
    print(f"{i}: {graph[0][i]}")

visualize_graph(graph, len(graph[0]), graph[1])
