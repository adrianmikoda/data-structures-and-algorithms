# implementation of the Dijkstra's Algorithm
# edge - (target, cost)
from graph_filler import fill_graph
from queue import PriorityQueue
import math

pq = PriorityQueue()

def dijkstra(adjacency_list, start):
    vertices = len(adjacency_list)
    cost = [math.inf for i in range(vertices)]
    parent = [-1 for i in range(vertices)]
    # cost[start] = 0

    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        current_cost, u = pq.get()
        cost[u] = current_cost
        for v, edge_cost in adjacency_list[u]:
            if cost[v] == math.inf:
                parent[v] = u
                pq.put((current_cost+edge_cost, v))

    print(f"d: {cost}")
    print(f"parent: {parent}")


if __name__ == "__main__":
    G = fill_graph()[0]
    print("")
    print(f"Adjacency list representation: {G}")
    s = int(input("Enter the starting vertex: "))
    dijkstra(G, s)
