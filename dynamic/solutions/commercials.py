# O(nlog) time complexity


def commercials(T, S, o):
    n = len(T)
    array = []
    for i in range(n):
        array.append((T[i][0], T[i][1], S[i]))
    array.sort()

    dp = [[0 for _ in range(3)] for _ in range(n)]
    answer = 0

    for i in range(n):
        start, end, value = array[i]
        for counter in range(2):
            if i > 0:
                dp[i][counter] = max(dp[i-1][counter], dp[i][counter])

            left = 0
            right = n
            while left < right:
                mid = left + (right - left) // 2
                if array[mid][0] <= end:
                    left = mid + 1
                else:
                    right = mid

            if left >= n:
                answer = max(answer, dp[i][counter] + value)
            else:
                dp[left][counter+1] = max(dp[left][counter+1], dp[i][counter] + value)

        answer = max(answer, dp[i][2], dp[i][1], dp[i][0])

    return answer


T = [(0, 3), (4, 5), (1, 4)]
S = [5000, 3000, 15000]
O = 6
print(commercials(T, S, O))
