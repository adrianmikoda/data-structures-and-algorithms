# O(mn + qm) time complexity
import math


def insert(tree, word):
    length = len(word)
    index = 0

    for pointer in range(length-1, -1, 0):
        tree[index] += 1
        if word[pointer] == '0':
            index = 2*index + 1
        else:
            index = 2*index + 2
    tree[index] += 1


def retrieve(tree, word):
    length = len(word)
    index = 0

    for pointer in range(length-1, -1, 0):
        if word[pointer] == '0':
            index = 2*index + 1
        else:
            index = 2*index + 2

    return tree[index]


def cryptographer(D, Q):
    m = 0
    for word in D:
        length = len(word)
        if length > m:
            m = length

    tree = [0 for _ in range(2**(m+1))]

    for word in D:
        insert(tree, word)

    answer = 0
    for word in Q:
        answer += math.log10(retrieve(tree, word))

    return answer


D = ['0', '100', '1100', '1101', '1111']
Q = ['', '1', '11', '0', '1101']
print(cryptographer(D, Q))
