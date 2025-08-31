# O(nk) time complexity
import random


def partition(left, right, array):
    pivot_pos = random.randint(left, right)
    array[pivot_pos], array[right] = array[right], array[pivot_pos]
    pivot = array[right]
    i = left-1

    for j in range(left, right):
        if array[j][0] < pivot[0] or (array[j][0] == pivot[0] and array[j][1] <= pivot[1]):
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[right] = array[right], array[i+1]
    return i+1


def quickselect(left, right, array, k):
    while left <= right:
        q = partition(left, right, array)
        if q == k:
            return array[q][2]
        elif q < k:
            left = q + 1
        else:
            right = q - 1


def google(H, s):
    n = len(H)
    array = []
    for i in range(n):
        password = H[i]
        letter_count = 0
        for c in password:
            if c < '0' or c > '9':
                letter_count += 1
        array.append((len(password), letter_count, i))

    return H[quickselect(0, n-1, array, n-s)]


H = ["aba", "abc", "ab1", "abab", "a1a1", "aa12a"]
s = 3
print(google(H, s))
