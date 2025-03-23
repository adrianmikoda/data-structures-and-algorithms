def merge(arr_left, arr_right, counter):
    nl, nr = len(arr_left), len(arr_right)
    pl, pr = 0, 0
    res = [0 for i in range(nl + nr)]
    while pl < nl and pr < nr:
        if arr_right[pr] < arr_left[pl]:
            counter += nl - pl
        if arr_left[pl] <= arr_right[pr]:
            res[pl+pr] = arr_left[pl]
            pl += 1
        else:
            res[pl+pr] = arr_right[pr]
            pr += 1

    while pl < nl:
        res[pl+pr] = arr_left[pl]
        pl += 1
    while pr < nr:
        res[pl+pr] = arr_right[pr]
        pr += 1
    return (res, counter)


def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return (arr, 0)
    arr_left, arr_right = arr[:n//2], arr[n//2:]
    merge_left = merge_sort(arr_left)
    merge_right = merge_sort(arr_right)

    return merge(merge_left[0], merge_right[0], merge_left[1] + merge_right[1])


def count_inversions(A):
    merge_result = merge_sort(A)
    return merge_result[1]
