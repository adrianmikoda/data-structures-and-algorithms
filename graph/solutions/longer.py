from collections import deque
def BFS(adjacency_list, s, d, parent, visit_count, t):
    q = deque()
    d[s] = 0
    q.append(s)
    while q:
        u = q.popleft()
        #print(f"u: {u}")
        visit_count[u] += 1
        if u != t:
            
            for v in adjacency_list[u]:
                #print(v)
                if d[v] == -1:
                    d[v] = d[u] + 1
                    parent[v] = u
                    q.append(v)
                elif parent[u] != v:
                    visit_count[v] += 1


def longer(G, s ,t):
    vertices = len(G)
    d = [-1 for i in range(vertices)]
    parent = [-1 for i in range(vertices)]
    visits = [0 for i in range(vertices)]
    BFS(G, s, d, parent, visits, t)

    #print(d[t])
    #print(parent)
    #print(visits)
    if visits[t] == 0:
        return None
    vertex = t
    while vertex != s:
        if visits[vertex] > 1:
            return (parent[vertex], vertex)
        vertex = parent[vertex]
    return None
    


graph = [[1], [0,2,6], [1,3,6], [2,4], [3,5], [4], [1,2]]


print(longer(graph, 0, 5))
            
