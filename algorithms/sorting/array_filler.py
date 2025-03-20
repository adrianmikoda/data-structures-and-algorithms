import random

def fill_array(): # filling the array with test values
    n = int(input("Length of the array: "))
    random_array = input("Fill the array with random numbers? (Y/N): ")
    a,b = 0,0
    if random_array.lower() == "y":
        a = int(input("Start of the interval for random numbers a: "))
        b = int(input("End of the interval for random numbers b: "))
        if b < a:
            print("Error: b must be grater than or equal to a")
            quit()
        array = [random.randint(a, b) for i in range(n)]
    else:
        print("Enter the values to fill the array")
        array = [0 for i in range(n)]
        for i in range(n):
            array[i] = int(input())
    return array