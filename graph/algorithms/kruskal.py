# implementation of the Kruskal's Algorithm
# O(ElogV) time complexity

class Union:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
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

# edge = (weight, vertex, vertex)
edge_list = [(8, 1, 4),
             (1, 1, 3),
             (2, 1, 5),
             (3, 3, 5),
             (12, 3, 2),
             (16, 5, 2),
             (7, 4, 5),
             (12, 3, 2),
             (27, 0, 1),
             (15, 0, 3)]

vertices = 6
union_find_handler = Union(vertices)
edge_list_sorted = sorted(edge_list)
mst = []
for weight,a,b in edge_list_sorted:
    if union_find_handler.find(a) != union_find_handler.find(b):
        union_find_handler.union(a,b)
        mst.append((weight, a, b))
print(edge_list_sorted)
print(mst)
