# O(nlogn) time complexity


def bridges(T):
    n = len(T)
    T.sort()
    array = []
    array.append(T[0][1])

    for i in range(1, n):
        south = T[i][1]

        if array[-1] < south:
            array.append(south)
        else:
            left = 0
            right = len(array)

            while left < right:
                mid = left + (right - left) // 2
                if array[mid] < south:
                    left = mid + 1
                else:
                    right = mid

            array[left] = south

    return len(array)


T = [(1, 2), (2, 3), (3, 0)]
print(bridges(T))
