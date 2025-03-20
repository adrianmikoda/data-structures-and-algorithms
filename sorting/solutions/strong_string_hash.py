# implementation of the solution for the strong_string problem
# O(N + nlogn) time complexity (N is the length of all words in the array combined)
# using double hashing to lower the chances of hash collision

p1, m1 = 31, 1000000009 
p2, m2 = 37, 1000000007

def normalize(arr):
    n = len(arr)
    for i in range(n):
        if arr[i][::-1] < arr[i]:
            arr[i] = arr[i][::-1]
            
def hash_string(s, p, m):
    hash_val = 0
    p_power = 1
    for c in s:
        hash_val = (hash_val + p_power * ord(c))%m
        p_power = (p_power*p)%m
    return hash_val
    
def hash(arr, p, m): # using hashing to speed up string comparisons
    n = len(arr)
    arr_hash_res = [0 for i in range(n)]
    for i in range(0,n):
        arr_hash_res[i] = hash_string(arr[i], p, m)
        
    return arr_hash_res
    
def merge(arr1, arr2):
    p1, p2 = 0, 0
    n1, n2 = len(arr1), len(arr2)
    arr_res = ["0" for _ in range(n1+n2)]
    while p1 < n1 and p2 < n2:
        if arr1[p1] < arr2[p2]:
            arr_res[p1+p2] = arr1[p1]
            p1+=1
        else:
            arr_res[p1+p2] = arr2[p2]
            p2+=1

    # adding leftovers
    while p1 < n1:
        arr_res[p1+p2] = arr1[p1]
        p1+=1
    while p2 < n2:
        arr_res[p1+p2] = arr2[p2]
        p2+=1

    return arr_res

def merge_sort(arr):
    n = len(arr)
    if n <= 1: return arr

    arr1, arr2 = arr[:n//2], arr[n//2:]
    return merge(merge_sort(arr1), merge_sort(arr2))

def answer(arr):
    n = len(arr)
    max_strength, curr_strength = 1, 1
    prev = arr[0]

    for i in range(1,n):
        if prev == arr[i]:
            curr_strength+=1
        else:
            max_strength = max(max_strength, curr_strength)
            prev = arr[i]
            curr_strength = 1

    return max(max_strength, curr_strength)

def strong_string(arr):
    n = len(arr)
    normalize(arr)
    arr_hash1 = hash(arr, p1, m1)
    arr_hash2 = hash(arr, p2, m2)
    
    arr_hash_sorted1 = merge_sort(arr_hash1)
    arr_hash_sorted2 = merge_sort(arr_hash2)
    
    return min(answer(arr_hash_sorted1), answer(arr_hash_sorted2))