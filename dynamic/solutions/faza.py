# O(nlogn) time complexity


def wyprawy(WI):
    n = len(WI)
    WI.sort()

    answer = 0
    dp = [0 for _ in range(n)]

    for index in range(n):
        s, t, k = WI[index]
        if index > 0:
            dp[index] = max(dp[index-1], dp[index])

        left = 0
        right = n

        while left < right:
            mid = left + (right-left)//2
            if WI[mid][0] < t:
                left = mid + 1
            else:
                right = mid

        if left >= n:
            answer = max(answer, dp[index] + k)
        else:
            dp[left] = max(dp[left], dp[index] + k)

    return answer


WI = [(1, 5, 100), (3, 4, 70), (2, 4, 90), (4, 7, 60)]
print(wyprawy(WI))
