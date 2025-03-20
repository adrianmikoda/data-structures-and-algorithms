# implementation of the solution for the strong_string problem
# O(NlogN) time complexity (N is the length of all words in the array combined)

def normalize(arr):
    n = len(arr)
    for i in range(n):
        if arr[i][::-1] < arr[i]:
            arr[i] = arr[i][::-1]

def merge(arr1, arr2):
    p1, p2 = 0, 0
    n1, n2 = len(arr1), len(arr2)
    arr_res = ["0" for _ in range(n1+n2)]
    while p1 < n1 and p2 < n2:
        if arr1[p1] < arr2[p2]:
            arr_res[p1+p2] = arr1[p1]
            p1+=1
        else:
            arr_res[p1+p2] = arr2[p2]
            p2+=1

    # adding leftovers
    while p1 < n1:
        arr_res[p1+p2] = arr1[p1]
        p1+=1
    while p2 < n2:
        arr_res[p1+p2] = arr2[p2]
        p2+=1

    return arr_res

def merge_sort(arr):
    n = len(arr)
    if n <= 1: return arr

    arr1, arr2 = arr[:n//2], arr[n//2:]
    return merge(merge_sort(arr1), merge_sort(arr2))

def strong_string(arr):
    n = len(arr)
    normalize(arr)
    arr_sorted = merge_sort(arr)

    max_strength, curr_strength = 1, 1
    prev = arr_sorted[0]

    for i in range(1,n):
        if prev == arr_sorted[i]:
            curr_strength+=1
        else:
            max_strength = max(max_strength, curr_strength)
            prev = arr_sorted[i]
            curr_strength = 1

    max_strength = max(max_strength, curr_strength)

    return max_strength