# O(nlogn) time complexity


def snow(T, I):
    n = len(I)
    array = []
    for first, second in I:
        array.append((first, 0))
        array.append((second, 1))
    array.sort()

    answer = 0
    counter = 0

    n = len(array)
    for i in range(n):
        if array[i][1] == 0:
            counter += 1
        else:
            answer = counter if counter > answer else answer
            counter -= 1

    return answer


T = 100
I = [(3, 10), (0, 5), (20, 30), (25, 35), (26, 26)]
print(snow(T, I))
