# implementation of the Counting Sort algorithm
# numbers in the [0, max_range] range
from array_filler import fill_array

max_range = 9

def counting_sort(arr):
    n = len(arr)
    counters = [0 for _ in range(max_range+1)] #

    for number in arr:
        counters[number] += 1
    for i in range(1, max_range+1):
        counters[i] += counters[i-1]
    
    res = [0 for _ in range(n)]
    for i in range(len(arr)-1, -1, -1):
        res[counters[arr[i]]-1] = arr[i]
        counters[arr[i]] -= 1

    return res

# run test code only when script is executed directly
if(__name__ == "__main__"): 
    array = fill_array(0, max_range) # using the input handling function from array_filler.py
    print(f"\narray: {array}")
    print(f"sorted array: {counting_sort(array)}")