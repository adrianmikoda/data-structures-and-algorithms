# O(nlogn) time complexiy


def G_R_to_adjaceny_list(G, R):
    n = len(G)
    adjacency_list = [[] for _ in range(n)]
    for u in range(n):
        G[u].sort()
        R[u].sort()
        for i in range(len(G[u])-1, -1, -1):
            v = G[u][i]
            if len(R[u]) > 0 and R[u][-1] == v:
                R[u].pop()
            else:
                adjacency_list[u].append(v)
    return n, adjacency_list


def dyrektor(G, R):
    n, adjacency_list = G_R_to_adjaceny_list(G, R)
    if n == 0:
        return []

    stack = [0]
    order = []
    while len(stack) > 0:
        u = stack[-1]
        if len(adjacency_list[u]) > 0:
            v = adjacency_list[u].pop()
            stack.append(v)
        else:
            order.append(stack.pop())

    return order[::-1]


G = [[1, 0, 2], [2, 0], [1, 0]]
R = [[0], [], []]
print(dyrektor(G, R))
