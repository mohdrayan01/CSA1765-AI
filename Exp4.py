# Write the python program for Cript-Arithmetic problem
from itertools import permutations
def solve_cryptarithmetic(puzzle):
    words = puzzle.split()
    letters = set(''.join(words))
    if len(letters) > 10:
        return None
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        if all(mapping[word[0]] != 0 for word in words):
            SEND = sum(mapping[c] * (10 ** i) for i, c in enumerate("SEND"[::-1]))
            MORE = sum(mapping[c] * (10 ** i) for i, c in enumerate("MORE"[::-1]))
            MONEY = sum(mapping[c] * (10 ** i) for i, c in enumerate("MONEY"[::-1]))
            if SEND + MORE == MONEY:
                return mapping
    return None
puzzle = "SEND + MORE = MONEY"
mapping = solve_cryptarithmetic(puzzle)
if mapping:
    print(mapping)
else:
    print("No solution found.")