# O(n) time complexity


def jump (M):
    moves = {'UL': (-2, -1),
             'LU': (-1, -2),
             'LD': (1, -2),
             'DL': (2, -1),
             'DR': (2, 1),
             'RD': (1, 2),
             'RU': (-1, 2),
             'UR': (-2, 1)}
    state_dictionary = {}
    state_dictionary[(0, 0)] = True
    row, col = 0, 0

    for m in M:
        move = moves[m]
        row += move[0]
        col += move[1]
        state_dictionary[(row, col)] = not state_dictionary.get((row, col), False)

    answer = 0
    for state in state_dictionary.values():
        answer += state

    return answer


M = ["UL", "RD", "LU", "LU", "RD", "DL", "UR", "DR"]
print(jump(M))
