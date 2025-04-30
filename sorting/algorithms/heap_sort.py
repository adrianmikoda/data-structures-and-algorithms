# implementation of the Heap Sort algorithm
from array_filler import fill_array

def parent(x):
    return (x-1)//2
def left_child(x):
    return 2*x+1
def right_child(x):
    return 2*x+2


def heapify(arr, n, i):
    max_index = i
    l = left_child(i)
    r = right_child(i)

    if l < n and arr[l] > arr[max_index]:
        max_index = l
    if r < n and arr[r] > arr[max_index]:
        max_index = r
    if max_index != i:
        arr[i], arr[max_index] = arr[max_index], arr[i]
        heapify(arr, n, max_index)


def build_heap(arr):
    n = len(arr)
    for i in range(parent(n-1), -1, -1):
        heapify(arr, n, i)


def heap_sort(arr):
    n = len(arr)
    build_heap(arr)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


# run test code only when script is executed directly (not imported)
if __name__ == "__main__":
    array = fill_array()
    print(f"array {array}")
    heap_sort(array)
    print(f"sorted array {array}")
