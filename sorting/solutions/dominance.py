def dominance(A):
    n = len(A)
    arr_x = [0 for i in range(n+1)]
    arr_y = [0 for i in range(n+1)]

    for i in range(n):
        arr_x[A[i][0]] += 1
        arr_y[A[i][1]] += 1

    for i in range(n-1, -1, -1):
        arr_x[i] += arr_x[i+1]
        arr_y[i] += arr_y[i+1]

    sum = arr_x[A[0][0]] + arr_y[A[0][1]]
    for i in range(1, n):
        curr = arr_x[A[i][0]] + arr_y[A[i][1]]
        sum = sum if sum < curr else curr

    return n-sum+1
