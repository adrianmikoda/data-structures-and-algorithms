# O(nk) time complexity


def kstrong(T, k):
    n = len(T)
    dp = [[0 for __ in range(k+1)] for _ in range(n)]
    answer = T[0]
    dp[0][0] = T[0]
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0]+T[i], T[i])
        answer = max(answer, dp[i][0])

    for kj in range(1, k+1):
        for i in range(1, n):
            dp[i][kj] = max(dp[i-1][kj-1], dp[i-1][kj] + T[i])
            answer = max(answer, dp[i][kj])

    return answer


T = [-20, 5, -1, 10, 2, -8, 10]
k = 1
print(kstrong(T, k))
