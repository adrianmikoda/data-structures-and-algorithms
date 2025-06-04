# implmenetation of the dynamic interval sum algorithm using the interval tree data structure
import math


class IntervalTreeSum:
    def __init__(self, n):
        p = math.ceil(math.log2(n))
        self.first_element_index = 2**p - 1
        self.last_element_index = self.first_element_index+n-1
        self.t = [0 for i in range(2**(p+1)-1)]

    def print_elements(self):
        for i in range(self.first_element_index, self.last_element_index+1):
            print(f"{self.t[i]} ", end="")
        print("")

    @staticmethod
    def left(i):
        return i*2 + 1

    @staticmethod
    def right(i):
        return i*2 + 2

    @staticmethod
    def parent(i):
        return (i-1)//2

    def modify(self, i, v):
        k = self.first_element_index + i
        d = v - self.t[k]
        while k >= 0:
            self.t[k] += d
            k = self.parent(k)

    def intsum(self, k, left_boundary, right_boundary, i, j):
        if j < i:
            return 0

        if left_boundary == i and right_boundary == j:
            return self.t[k]

        r = (right_boundary-left_boundary+1)//2
        if j < left_boundary+r:
            return self.intsum(self.left(k), left_boundary, left_boundary+r-1, i, j)
        elif i >= left_boundary+r:
            return self.intsum(self.right(k), left_boundary+r, right_boundary, i, j)
        else:
            sum_left = self.intsum(self.left(k), left_boundary, left_boundary+r-1, i, left_boundary+r-1)
            sum_right = self.intsum(self.right(k), left_boundary+r, right_boundary, left_boundary+r, j)
            return sum_left+sum_right

    def interval_sum(self, i, j):
        return self.intsum(0, self.first_element_index, self.last_element_index,
                           self.first_element_index+i, self.first_element_index+j)


if __name__ == "__main__":
    n = int(input("Enter the element count: "))
    interval_tree = IntervalTreeSum(n)
    task = -1
    interval_tree.print_elements()

    while True:
        task = input('enter task ["m" i v | "s" i j | "0" to end]: ')
        if task == "0":
            break
        task = task.lower().split()
        if task[0] == 'm':
            i, v = int(task[1]), int(task[2])
            interval_tree.modify(i, v)
            interval_tree.print_elements()
        elif task[0] == 's':
            i, j = int(task[1]), int(task[2])
            interval_sum = interval_tree.interval_sum(i, j)
            print(interval_sum)
