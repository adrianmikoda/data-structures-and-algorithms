class Union:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            x = self.find(self.parent[x])
        return x

    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.rank[x] > self.rank[y]:
            self.parent[x] = y
        elif self.rank[x] < self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[y] = x
            self.rank[x] += 1