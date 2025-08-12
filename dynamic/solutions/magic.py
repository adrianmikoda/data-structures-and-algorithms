# O(n) time complexity


def magic(C):
    n = len(C)
    dp = [-1 for _ in range(n)]
    dp[0] = 0

    for room_number in range(n-1):
        if dp[room_number] != -1:
            current_room = C[room_number]
            current_gold = current_room[0]

            for i in range(1, 4):
                price, room = current_room[i]
                take = current_gold - price
                new_gold_amount = dp[room_number] + take
                if room != -1 and take <= 10 and new_gold_amount >= 0:
                    dp[room] = max(dp[room], new_gold_amount)

    return dp[n-1]


C = [ [8,  [ 6, 3], [ 4, 2], [7, 1]],
      [22, [12, 2], [21, 3], [0,-1]],
      [9,  [11, 3], [ 0,-1], [7,-1]],
      [15, [ 0,-1], [ 1,-1], [0,-1]]]
print(magic(C))
