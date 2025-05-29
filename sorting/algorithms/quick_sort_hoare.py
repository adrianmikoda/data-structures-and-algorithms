# implementation of the Quick Sort algorithm using Hoare's partition scheme
from sorting_utils import initialize_array
import random


def partition(arr, start, end):
    pivot_pos = random.randint(start,end)
    pivot = arr[pivot_pos]
    a = start-1
    b = end+1

    while True:
        a += 1
        while arr[a] < pivot:
            a += 1
        b -= 1
        while arr[b] > pivot:
            b -= 1

        if a >= b:
            return b
        arr[a], arr[b] = arr[b], arr[a]


def quick_sort(arr, start, end):
    while start < end:
        pivot = partition(arr, start, end)
        if pivot-start+1 < end-pivot:
            quick_sort(arr, start, pivot)
            start = pivot+1
        else:
            quick_sort(arr, pivot+1, end)
            end = pivot


# run test code only when script is executed directly (not imported)
if __name__ == "__main__":
    array = initialize_array()
    print(f"\narray: {array}")
    quick_sort(array, 0, len(array)-1)
    print(f"sorted array: {array}")
