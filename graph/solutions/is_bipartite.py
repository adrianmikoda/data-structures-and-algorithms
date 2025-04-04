# leetcode problem no. 785

from collections import deque
moves = [[1, 0], [0, 1], [-1, 0] ,[0, -1]]

class Solution(object):
                
    def numIslands(self, grid):
        n = len(grid)
        m = len(grid[0])
        answer = 0

        q = deque()
        def BFS(s_pos):
            
            grid[s_pos[0]][s_pos[1]] = "X"
            q.append(s_pos)

            while q:
                curr_pos = q.popleft()
                for move in moves:
                    target_pos = (curr_pos[0]+move[0], curr_pos[1]+move[1])
                    if (target_pos[0] >= 0 and target_pos[0] < n and
                        target_pos[1] >= 0 and target_pos[1] < m and
                        grid[target_pos[0]][target_pos[1]] == "1"):

                        q.append(target_pos)
                        grid[target_pos[0]][target_pos[1]] = "X"


        for line in range(n):
            for column in range(m):
                if grid[line][column] == "1":
                    answer += 1
                    BFS((line, column))
        return answer