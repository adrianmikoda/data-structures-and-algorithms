# leetcode problem no. 200
from collections import deque


class Solution(object):

    def numIslands(self, grid):
        n = len(grid)
        m = len(grid[0])
        answer = 0

        q = deque()

        for line in range(n):
            for column in range(m):
                if grid[line][column] == '1':
                    answer += 1
                    grid[line][column] = 0
                    q.append((line, column))
                    while q:
                        pos = q.popleft()
                        pos_l = pos[0]
                        pos_c = pos[1]
                        if pos_l + 1 < n and grid[pos_l+1][pos_c] == '1':
                            q.append((pos_l+1, pos_c))
                            grid[pos_l+1][pos_c] = '0'
                        if pos_c + 1 < m and grid[pos_l][pos_c+1] == '1':
                            q.append((pos_l, pos_c+1))
                            grid[pos_l][pos_c+1] = '0'
                        if pos_l - 1 >= 0 and grid[pos_l-1][pos_c] == '1':
                            q.append((pos_l-1, pos_c))
                            grid[pos_l-1][pos_c] = '0'
                        if pos_c - 1 >= 0 and grid[pos_l][pos_c-1] == '1':
                            q.append((pos_l, pos_c-1))
                            grid[pos_l][pos_c-1] = '0'

        return answer
