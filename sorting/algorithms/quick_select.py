# implementation of the Quick Select algorithm
from array_filler import fill_array
from quick_sort_lomuto import quick_sort


def partition(arr, start, end):
    x = arr[end]
    i = start-1

    for j in range(start, end):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i+1


def quick_select(arr, start, end, k):
    q = partition(arr, start, end)
    if q == k:
        return arr[q]
    if k < q:
        return quick_select(arr, start, q-1, k)
    else:
        return quick_select(arr, q+1, end, k)


array = fill_array()
arr = array.copy()
print(arr)
print(quick_select(arr, 0, 5, 3))
k = int(input("Index of the searched element k: "))


print(f"\narray: {array}")
print(f"answer using QuickSelect: {quick_select(array, 0, len(array)-1, k)}")  # O(n)

# verifying the result by comparing with the sorted array
quick_sort(array, 0, len(array)-1)
print(f"array sorted: {array}")
print(f"answer using QuickSort: {array[k]}")  # O(nlogn)
