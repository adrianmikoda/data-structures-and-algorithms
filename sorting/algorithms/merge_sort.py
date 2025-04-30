# implementation of the Merge Sort algorithm
from array_filler import fill_array


def merge(arr1, arr2):
    p1, p2 = 0, 0
    n1, n2 = len(arr1), len(arr2)
    arr_res = [0 for i in range(n1+n2)]

    while p1 < n1 and p2 < n2:
        if arr1[p1] < arr2[p2]:
            arr_res[p1+p2] = arr1[p1]
            p1 += 1
        else:
            arr_res[p1+p2] = arr2[p2]
            p2 += 1

    # adding leftovers
    while p1 < n1:
        arr_res[p1+p2] = arr1[p1]
        p1 += 1
    while p2 < n2:
        arr_res[p1+p2] = arr2[p2]
        p2 += 1

    return arr_res


def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    arr1, arr2 = arr[:n//2], arr[n//2:]
    return merge(merge_sort(arr1), merge_sort(arr2))


# run test code only when script is executed directly (not imported)
if __name__ == "__main__":
    array = fill_array()
    print(f"\narray: {array}")
    print(f"sorted array: {merge_sort(array)}")
