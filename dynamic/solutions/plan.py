# O(nm + mlogm) time complexity
from queue import PriorityQueue


def linearise(T, n, m):

    def dfs(current_row, current_col):
        nonlocal T, n, m
        total, T[current_row][current_col] = T[current_row][current_col], 0
        moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        for drow, dcol in moves:
            if (
                current_row+drow >= 0 and
                current_row+drow < n and
                current_col+dcol >= 0 and
                current_col+dcol < m and
                T[current_row+drow][current_col+dcol] != 0
            ):
                total += dfs(current_row+drow, current_col+dcol)

        return total

    for col in range(0, m):
        if T[0][col] != 0:
            T[0][col] = dfs(0, col)


def plan(T):
    n, m = len(T), len(T[0])
    linearise(T, n, m)
    pq = PriorityQueue()
    stop_count = 1
    fuel = T[0][0]-1
    i = 1

    while i < m - 1:
        if T[0][i] != 0:
            pq.put(T[0][i]*-1)
        if fuel == 0:
            fuel += pq.get()*-1
            stop_count += 1
        i += 1
        fuel -= 1

    return stop_count


T = [[3, 0, 0, 1, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [4, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(plan(T))
