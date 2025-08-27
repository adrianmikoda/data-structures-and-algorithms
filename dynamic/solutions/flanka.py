# O(n + k) time complexity


def pijemy(k, PIWO):
    n = len(PIWO)
    counters = [0 for _ in range(k+1)]
    for i in range(n):
        counters[PIWO[i]] += 1

    frequency = [[] for _ in range(n//2 + 2)]
    for piwo in range(1, k+1):
        frequency[counters[piwo]].append(piwo)

    answer = [None for _ in range(n)]
    pointer = 0
    for f in range(n//2 + 1, 0, -1):
        for piwo in frequency[f]:
            while counters[piwo] > 0:
                if pointer >= n:
                    pointer = 1
                answer[pointer] = piwo
                counters[piwo] -= 1
                pointer += 2

    return answer


k = 3
PIWO = [1, 2, 1, 1, 1, 3, 3, 3, 2, 3]
print(pijemy(k, PIWO))
