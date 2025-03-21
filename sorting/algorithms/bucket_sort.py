# implementation of the Bucket Sort algorithm
# sorting real numbers from the [0,1) range
from array_filler import fill_array


class Node:
    def __init__(self, value=None):
        self.val = value
        self.next = None


# inserting new nodes into a sorted linked list
def insert(q, val):
    p, n, new = q, q.next, Node(val)

    while n is not None and n.val is not None and n.val < new.val:
        p = n
        n = n.next
    new.next = n
    p.next = new

    return q


def print_list(p):
    p = p.next
    while p is not None:
        print(p.val)
        p = p.next


def bucket_sort(arr):
    n = len(arr)
    buckets = [Node() for _ in range(n)]

    # scatter
    for val in arr:
        bucket_nr = int(val*n)
        p = buckets[bucket_nr]
        p = insert(p, val)
    res = [0 for _ in range(n)]
    i = 0

    # gather values from sorted buckets (linked lists)
    for bucket in buckets:
        p = bucket.next
        while p is not None:
            res[i] = p.val
            i += 1
            p = p.next

    return res


# run test code only when script is executed directly
if __name__ == "__main__":
    array = fill_array(0, 1000000-1)
    for i in range(0, len(array)):
        array[i] /= 1000000
    print(f"\narray: {array}")
    print(f"sorted array: {bucket_sort(array)}")
