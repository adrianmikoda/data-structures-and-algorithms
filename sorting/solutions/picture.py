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
    student_array = [student for student in T]
    n = len(T)

    starting_index = 0
    next_starting_index = k

    row_elements = [deque() for _ in range(m)]

    for row in range(m-1, -1, -1):
        quickselect(starting_index, n-1, student_array, next_starting_index-1)
        for i in range(starting_index, next_starting_index):
            row_elements[row].append(student_array[i])
        k += 1
        starting_index = next_starting_index
        next_starting_index += k

    index = 0
    while index < n:
        for row in range(m):
            if row_elements[row]:
                T[index] = row_elements[row].popleft()
                index += 1

    return None


m = 2
k = 2
T = [(1001, 154), (1002, 176), (1003, 189), (1004, 165), (1005, 162)]
print(picture(T, m, k))
