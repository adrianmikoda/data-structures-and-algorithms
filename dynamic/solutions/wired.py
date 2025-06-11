# O(n^3) time complexity
import math


def wired(T):
    n = len(T)
    mem = {}

    def rec_handler(first, last):
        nonlocal T, mem
        if mem.get((first, last), False):
            return mem[(first, last)]

        if first == last-1:
            mem[(first, last)] = abs(T[first] - T[last]) + 1
            return mem[(first, last)]

        current_minimum = math.inf
        for i in range(first+1, last, 2):
            current_minimum = min(current_minimum, rec_handler(first, i) + rec_handler(i+1, last))

        mem[(first, last)] = min(current_minimum, rec_handler(first+1, last-1) + abs(T[first] - T[last]) + 1)
        return mem[(first, last)]

    rec_handler(0, n-1)

    return mem[(0, n-1)]


print(wired([7, 1, 3, 7, 2, 1]))
