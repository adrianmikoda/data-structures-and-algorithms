# implementation of the Quick Sort algorithm using Lomuto's partition scheme
from array_filler import fill_array
import random

def median_of_three(arr, start, end):
    mid = (start+end)//2
    a, b, c = arr[start], arr[mid], arr[end]
    if a > b != a > c: 
        return start
    if b > c != b > a: 
        return mid
    return end

def partition(arr, start, end):
    # x_pos = random.randint(start, end) make random choice of the pivot point
    x_pos = median_of_three(arr, start, end)
    arr[x_pos], arr[end] = arr[end], arr[x_pos]

    i = start-1
    for j in range(start, end):
        if(arr[j] <= arr[end]):
            i+=1
            arr[j], arr[i] = arr[i], arr[j]

    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i+1

def quick_sort(arr, start, end):
    while start < end:
        pivot = partition(arr, start, end)
        if pivot-start < end-pivot:
            quick_sort(arr, start, pivot-1)
            start = pivot + 1
        else:
            quick_sort(arr, pivot+1, end)
            end = pivot - 1 
    
# run test code only when script is executed directly
if(__name__ == "__main__"): 
    array = fill_array() # using the input handling function from array_filler.py
    print(f"\narray: {array}")
    quick_sort(array, 0, len(array)-1)
    print(f"sorted array: {array}")