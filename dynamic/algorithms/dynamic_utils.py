import random


def initialize_array(array_length=None,
               is_randomized=None,
               min_number=None,
               max_number=None):
    if array_length is None:
        array_length = int(input("Length of the array: "))
    else:
        print(f"array_length parameter has already been set to {array_length}")
    if is_randomized is None:
        is_randomized = input("Fill the array with random numbers? (Y/N): ").lower() == 'y'
    else:
        print(f"is_randomized parameter has already been set to {is_randomized}")

    if is_randomized:
        if min_number is None:
            min_number = int(input("Start of the interval for random numbers min_number: "))
        else:
            print(f"min_number parameter has already been set to {min_number}")
        if max_number is None:
            max_number = int(input("End of the interval for random numbers max_number: "))
        else:
            print(f"max_number parameter has already been set to {max_number}")
        if max_number < min_number:
            length = len("ValueError: max_number must be greater than or equal to min_number")
            raise ValueError(f"Invalid max_number={max_number} and min_number={min_number} parameters" +
                             f"\n{'max_number must be greater than or equal to min_number':>{length}}")
        
        array = [random.randint(min_number, max_number) for _ in range(array_length)]
    else:
        print("Enter the values to fill the array")
        array = [0 for i in range(array_length)]
        for i in range(array_length):
            array[i] = int(input())

    return array
