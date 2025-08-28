# O(nlogm) time complexity


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        if self.rank[y] > self.rank[x]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


def G_to_edge_list(G):
    n = len(G)
    edge_list = []
    for u in range(n):
        for v, w in G[u]:
            if u < v:
                edge_list.append((w, u, v))
    return n, edge_list


def lufthansa(G):
    n, edge_list = G_to_edge_list(G)
    edge_list.sort(reverse=True)

    union_find_handler = UnionFind(n)
    answer = 0
    flag = False
    e = len(edge_list)

    for w, u, v in edge_list:
        if union_find_handler.find(u) == union_find_handler.find(v):
            if flag:
                answer += w
            else:
                flag = True
        union_find_handler.union(u, v)

    return answer


G = [[(1, 15), (2, 5), (3, 10)],
     [(0, 15), (2, 8), (4, 5), (5, 12)],
     [(0, 5), (1, 8), (3, 5), (4, 6)],
     [(0, 10), (2, 5), (4, 2), (5, 11)],
     [(1, 5), (2, 6), (3, 2), (5, 2)],
     [(1, 12), (4, 2), (3, 11)]]
print(lufthansa(G))
