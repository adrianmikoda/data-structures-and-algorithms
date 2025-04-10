# leetcode problem no. 785
from collections import deque


class Solution(object):
    def BFS(self, graph, s, color):
        q = deque()
        q.append(s)
        color[s] = 0

        while q:
            u = q.popleft()
            print(u)
            for v in graph[u]:
                if color[v] == -1:
                    color[v] = (color[u]+1) % 2
                    q.append(v)
                elif color[v] == color[u]:
                    return False
        return True

    def isBipartite(self, graph):
        n = len(graph)
        color = [-1 for i in range(n)]
        for node in range(n):
            if color[node] == -1 and not self.BFS(graph, node, color):
                return False
        return True
