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


def BFS(adjacency_list, s, color_nr, colors):
    q = deque()
    q.append(s)
    colors[s] = color_nr
    while q:
        u = q.popleft()
        for v in adjacency_list[u]:
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


def visualize_graph(adjacency_list, vertices, is_directed):
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
        graph.add_node(f'{i}', color=color_palette[colors[i]])
    for i in range(0, vertices):
        for j in adjacency_list[i]:
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

visualize_graph(graph[0], len(graph[0]), graph[1])
