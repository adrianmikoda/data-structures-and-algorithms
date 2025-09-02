# O(nlogn) time complexity


def wyprawy(WI):
    n = len(WI)
    WI.sort()

    answer = 0
    dp = [0 for _ in range(n)]

    for i in range(n):
        start, end, value = WI[i]
        if i > 0:
            dp[i] = max(dp[i-1], dp[i])

        left = 0
        right = n

        while left < right:
            mid = left + (right - left) // 2
            if WI[mid][0] < end:
                left = mid + 1
            else:
                right = mid

        if left >= n:
            answer = max(answer, dp[i] + value)
        else:
            dp[left] = max(dp[left], dp[i] + value)

    return answer


WI = [(1, 5, 100), (3, 4, 70), (2, 4, 90), (4, 7, 60)]
print(wyprawy(WI))
