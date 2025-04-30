# implementation of the Quick Sort algorithm using Lomuto's partition scheme
from array_filler import fill_array
import random


def partition(arr, start, end):
    mid = (start+end) // 2
    pivot_pos = end
    if (arr[start] > arr[mid]) ^ (arr[start] > arr[end]):
        pivot_pos = start
    if (arr[mid] > arr[start]) ^ (arr[mid] > arr[end]):
        pivot_pos = mid

    arr[pivot_pos], arr[end] = arr[end], arr[pivot_pos]

    i = start-1
    for j in range(start, end):
        if arr[j] <= arr[end]:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i+1


def quick_sort(arr, start, end):
    while start < end:
        pivot = partition(arr, start, end)
        if pivot-start < end-pivot:
            quick_sort(arr, start, pivot-1)
            start = pivot + 1
        else:
            quick_sort(arr, pivot+1, end)
            end = pivot - 1


# run test code only when script is executed directly (not imported)
if __name__ == "__main__":
    array = fill_array()
    print(f"\narray: {array}")
    quick_sort(array, 0, len(array)-1)
    print(f"sorted array: {array}")
