# O(n) time complexity
class Node():
    def __init__(self, value=None):
        self.val = value
        self.next = None


def partition(arr, first, last):
    pivot_pos = (first+last)//2
    arr[last], arr[pivot_pos] = arr[pivot_pos], arr[last]
    i = first-1

    for j in range(first, last):
        if arr[j] <= arr[last]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[last] = arr[last], arr[i+1]

    return i+1


def quickselect(arr, first, last, k):
    pivot = partition(arr, first, last)

    if pivot == k:
        return arr[pivot]
    elif k < pivot:
        return quickselect(arr, first, pivot-1, k)
    return quickselect(arr, pivot+1, last, k)


def insert(q, val):
    p, n, new = q, q.next, Node(val)

    while n is not None and n.val is not None and n.val < new.val:
        p = n
        n = n.next
    new.next = n
    p.next = new
    return q


def bucketsort(T, minimum, maximum):
    n = len(T)
    buckets = [Node() for i in range(n)]
    for i in T:
        pos = int((i-minimum)/(maximum-minimum)*n)
        buckets[pos] = insert(buckets[pos], i)

    res = [0 for i in range(n)]
    index = 0
    for p in buckets:
        p = p.next
        while p is not None:
            res[index] = p.val
            index += 1
            p = p.next
    return res


def answer(arr, D):
    n = len(arr)
    odp = 0
    prev = arr[0]

    for i in range(1, n):
        if arr[i] - prev >= D:
            odp += 1
        prev = arr[i]
    return odp


def fence(M, D, T):
    n = len(T)
    p = quickselect(T, 0, n-1, n//2)
    p1, p2 = 0, 0
    arr1 = [0 for _ in range(n//2)]
    arr2 = [0 for _ in range(n//2)]
    min2 = M
    for i in range(0, len(T)):
        if T[i] < p:
            arr1[p1] = T[i]
            p1 += 1
        else:
            min2 = min2 if min2 < T[i] else T[i]
            arr2[p2] = T[i]
            p2 += 1

    arr1 = bucketsort(arr1, 0, min2)
    arr2 = bucketsort(arr2, min2, M)

    return answer(arr1+arr2, D)
