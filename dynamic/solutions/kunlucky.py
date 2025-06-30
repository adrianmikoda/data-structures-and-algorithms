# O(n) time complexity


def calculate_kunlucky(is_kunlucky, k, n):
    x = k
    i = 1
    while x <= n:
        is_kunlucky[x] = True
        x_new = x + x % i + 7
        i += 1
        x = x_new


def kunlucky(T, k):
    n = len(T)
    is_kunlucky = [False for i in range(n+1)]
    calculate_kunlucky(is_kunlucky, k, n)
    answer, counter, a = 0, 0, 0
    for b in range(0, n):
        if is_kunlucky[T[b]]:
                counter += 1
        while a <= b and counter > 2:
            if is_kunlucky[T[a]]:
                counter -= 1
            a += 1
        answer = max(answer, b-a+1)

    return answer


T = [11, 10, 19, 19, 17, 16, 3, 9, 6, 14, 13, 8, 2, 13, 11, 12, 5, 5, 5]
k = 3
print(kunlucky(T, k))
