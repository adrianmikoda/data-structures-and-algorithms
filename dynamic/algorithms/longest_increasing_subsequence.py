# implementation of the longest increasing subsequence dynamic algorithm
# O(n^2) time complexity
from dynamic_utils import initialize_array


def longest_increasing_subsequence(array):
    maxval_pos = 0
    n = len(array)
    f = [1 for _ in range(n)]
    p = [-1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if array[i] > array[j]:
                if f[i] < f[j]+1:
                    f[i] = f[j]+1 if f[i] < f[j]+1 else f[i]
                    p[i] = j
                maxval_pos = i if f[maxval_pos] < f[i] else maxval_pos
    return maxval_pos, f, p


if __name__ == "__main__":
    array = initialize_array()
    print(f"\n{'array:':<6} {array}")

    pos, f, p = longest_increasing_subsequence(array)
    print(f"{'f:':<6} {f}")
    print(f"{'p:':<6} {p}")
    print(f"sequence length: {f[pos]}")
    sequence = []
    while pos != -1:
        sequence.append(array[pos])
        pos = p[pos]
    print(f"sequence: {sequence[::-1]}")
