# O(nm) time complexity
from collections import deque
import random


def partition(left, right, array):
    x_pos = random.randint(left, right)
    array[x_pos], array[right] = array[right], array[x_pos]
    x = array[right]
    i = left-1

    for j in range(left, right):
        if array[j][1] <= x[1]:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[right] = array[right], array[i+1]
    return i+1


def quickselect(left, right, array, k):
    pivot = partition(left, right, array)
    while pivot != k:
        pivot = partition(left, right, array)
        if pivot < k:
            left = pivot + 1
        else:
            right = pivot - 1

    return array[pivot]


def picture(T, m, k):
    n = len(T)
    array = T[:]
    row_elements = [deque() for _ in range(m)]

    starting_index = 0
    next_starting_index = k
    for row in range(m-1, -1, -1):
        quickselect(starting_index, n-1, array, next_starting_index-1)
        for i in range(starting_index, next_starting_index):
            row_elements[row].append(array[i])
        k += 1
        starting_index = next_starting_index
        next_starting_index += k

    i = 0
    while i < n:
        for row in range(m):
            if row_elements[row]:
                T[i] = row_elements[row].popleft()
                i += 1

    return None


m = 2
k = 2
T = [(1001, 154), (1002, 176), (1003, 189), (1004, 165), (1005, 162)]
print(picture(T, m, k))
