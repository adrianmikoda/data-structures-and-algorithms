# suboptimal solution
# O(n^3) time complexity


def maze(L):
    n = len(L)
    if L[0][0] == '#' or L[n-1][n-1] == '#': return -1

    dpu = [[-1 for _ in range(n)] for __ in range(n)]
    dpd = [[-1 for _ in range(n)] for __ in range(n)]
    dpu[0][0], dpd[0][0] = 0, 0
    for row in range(1, n):
        if L[row][0] == '#': break
        dpd[row][0] = dpd[row-1][0] + 1

    for col in range(1, n):
        for row in range(n):
            if L[row][col] == '#': continue
            if dpu[row][col-1] == -1 and dpd[row][col-1] == -1: continue
            val = max(dpu[row][col-1], dpd[row][col-1]) + 1
            dpd[row][col] = val
            dpu[row][col] = val
        for row in range(n):
            if L[row][col] == '#': continue
            if dpd[row][col-1] == -1 and dpu[row][col-1] == -1: continue
            row1, row2 = row-1, row+1
            while row1 >= 0 and L[row1][col] == '.':
                dpu[row1][col] = max(dpu[row1][col], dpu[row1+1][col] + 1)
                row1 -= 1
            while row2 < n and L[row2][col] == '.':
                dpd[row2][col] = max(dpd[row2][col], dpd[row2-1][col] + 1)
                row2 += 1

    return max(dpu[n-1][n-1], dpd[n-1][n-1])


L = ["....",
     "..#.",
     "..#.",
     "...."]
print(maze(L))
