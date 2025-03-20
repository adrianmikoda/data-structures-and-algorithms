# implementation of the Radix Sort using counting sort
# decimal numbers >= 0
from array_filler import fill_array

def counting_sort(arr,key):
    n = len(arr)
    counters = [0 for _ in range(10)]

    for number in arr:
        counters[key(number)] += 1
    for i in range(1,10):
        counters[i] += counters[i-1]

    res = [0 for _ in range(n)]
    for i in range(len(arr)-1, -1, -1):
        res[counters[key(arr[i])]-1] = arr[i]
        counters[key(arr[i])] -= 1
    return res

def radix_sort(arr):
    max_num = 0
    for num in arr:
        max_num = max(max_num, num)
    p = 1
    arr_res = arr
    while p < max_num:
        arr_res = counting_sort(arr_res, lambda x: (x//p)%10)
        p*=10
    return arr_res
        
# run test code only when script is executed directly
if(__name__ == "__main__"): 
    array = fill_array() # using the input handling function from array_filler.py
    print(f"\narray: {array}")
    print(f"sorted array: {radix_sort(array)}")
    