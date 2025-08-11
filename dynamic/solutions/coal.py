# O(nlogn) time complexity
import math


def insert(current, tree, coal_amount, first_element):
    if current >= first_element:
        tree[current] -= coal_amount
        return current - first_element

    left_child = 2*current + 1
    right_child = 2*current + 2

    i = None
    if tree[left_child] >= coal_amount:
        i = insert(left_child, tree, coal_amount, first_element)
    else:
        i = insert(right_child, tree, coal_amount, first_element)

    tree[current] = max(tree[left_child], tree[right_child])
    return i


def coal(A, T):
    n = len(A)
    p = math.ceil(math.log2(n))
    tree = [T for _ in range(2**(p+1)-1)]
    first_element = 2**p - 1

    answer = None
    for coal_amount in A:
        answer = insert(0, tree, coal_amount, first_element)

    return answer


A = [1, 6, 2, 10, 8, 7, 1]
T = 10
print(coal(A, T))
