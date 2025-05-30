#implementation of the knapsack dynamic algorithm
# O(B * n) time complexity
# B - knapsack size
# n - item count
from dynamic_utils import initialize_array


def knapsack(item_weights, item_values, knapsack_size):
    item_count = len(item_weights)
    f = [[0 for _ in range(knapsack_size+1)] for __ in range(item_count)]

    for b in range(item_weights[0], knapsack_size+1):
        f[0][b] = item_values[0]

    for b in range(knapsack_size+1):
        for item in range(1, item_count):
            f[item][b] = f[item-1][b]
            if b - item_weights[item] >= 0:
                f[item][b] = f[item-1][b - item_weights[item]] + item_values[item] if f[item-1][b - item_weights[item]] + item_values[item] > f[item][b] else f[item][b]

    for a in range(item_count):
        print(f"{f[a]}")
    answer = f[item_count-1][knapsack_size]
    return answer

if __name__ == "__main__":
    item_count = int(input("Item count: "))
    item_weights = initialize_array(array_length=item_count, min_number=1)
    item_values = initialize_array(array_length=item_count, min_number=1)
    knapsack_size = int(input("Knapsack size: "))

    print(f"\n{'item weights:':<13} {item_weights}")
    print(f"{'item values:':<13} {item_values}")
    answer = knapsack(item_weights, item_values, knapsack_size)
    print(f"max sum of values: {answer}")