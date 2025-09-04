# O(n^2) time complexity
from collections import deque


def kurt(D):
    n = len(D)
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    targets = [[[None for __ in range(n)] for _ in range(n)] for _ in range(4)]

    for row in range(n):
        for col in range(n-1, -1, -1):
            if D[row][col] == '0':
                targets[0][row][col] = (row, col)
                if col+1 < n and D[row][col+1] == '0':
                    targets[0][row][col] = targets[0][row][col+1]

    for col in range(n):
        for row in range(n-1, -1, -1):
            if D[row][col] == '0':
                targets[1][row][col] = (row, col)
                if row+1 < n and D[row+1][col] == '0':
                    targets[1][row][col] = targets[1][row+1][col]

    for row in range(n):
        for col in range(n):
            if D[row][col] == '0':
                targets[2][row][col] = (row, col)
                if col-1 >= 0 and D[row][col-1] == '0':
                    targets[2][row][col] = targets[2][row][col-1]

    for col in range(n):
        for row in range(n):
            if D[row][col] == '0':
                targets[3][row][col] = (row, col)
                if row-1 >= 0 and D[row-1][col] == '0':
                    targets[3][row][col] = targets[3][row-1][col]

    visited = [[[float('inf') for ___ in range(2)] for __ in range(n)] for _ in range(n)]
    visited[0][0][0] = 0
    visited[0][0][1] = 0

    queue = deque()
    queue.append((0, 0, 0))
    answer = float('inf')
    while queue:
        row, col, went_through = queue.popleft()
        current_turn_count = visited[row][col][went_through]
        if row == n-1 and col == n-1:
            continue
        
        if went_through == 0:
            for move_number in range(4):
                move = moves[move_number]
                if (row+2*move[0] >= 0 and row+2*move[0] < n and
                    col+2*move[1] >= 0 and col+2*move[1] < n and
                    D[row+move[0]][col+move[1]] == '#' and
                    D[row+2*move[0]][col+2*move[1]] == '0' and
                    visited[row+2*move[0]][col+2*move[1]][1] > current_turn_count + 1
                ):
                    visited[row+2*move[0]][col+2*move[1]][1] = current_turn_count + 1
                    queue.append((row+2*move[0], col+2*move[1], 1))

        for move_number in range(4):
            move = moves[move_number]
            next_coords = targets[move_number][row][col]

            if (next_coords and (next_coords[0] != row or next_coords[1] != col) and
                visited[next_coords[0]][next_coords[1]][went_through] > current_turn_count + 1
            ):
                visited[next_coords[0]][next_coords[1]][went_through] = current_turn_count + 1
                queue.append((next_coords[0], next_coords[1], went_through))

                if went_through == 0:
                    if (next_coords[0]+2*move[0] >= 0 and next_coords[0]+2*move[0] < n and
                        next_coords[1]+2*move[1] >= 0 and next_coords[1]+2*move[1] < n and
                        D[next_coords[0]+move[0]][next_coords[1]+move[1]] == '#' and
                        D[next_coords[0]+2*move[0]][next_coords[1]+2*move[1]] == '0' and
                        visited[next_coords[0]+2*move[0]][next_coords[1]+2*move[1]][1] > current_turn_count + 1
                    ):
                        visited[next_coords[0]+2*move[0]][next_coords[1]+2*move[1]][1] = current_turn_count + 1
                        queue.append((next_coords[0]+2*move[0], next_coords[1]+2*move[1], 1))

    for went_through in range(2):
        answer = min(answer, visited[n-1][n-1][went_through])

    return answer if answer != float('inf') else -1


D = ["000##",
     "##000",
     "000##",
     "00##0",
     "00000"]
print(kurt(D))
