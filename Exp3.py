# Write the python program for Water Jug Problem
from collections import deque
def water_jug_problem(capacity1, capacity2, target):
    visited = set()
    queue = deque()
    queue.append((0, 0, []))
    while queue:
        jug1, jug2, path = queue.popleft()
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))
        path = path + [(jug1, jug2)]
        if jug1 == target:
            return path
        queue.append((capacity1, jug2, path))
        queue.append((jug1, capacity2, path))
        queue.append((0, jug2, path))
        queue.append((jug1, 0, path))
        pour = min(jug1, capacity2 - jug2)
        queue.append((jug1 - pour, jug2 + pour, path))
        pour = min(jug2, capacity1 - jug1)
        queue.append((jug1 + pour, jug2 - pour, path))
    return None
capacity1 = 4  
capacity2 = 3   
target = 2
solution = water_jug_problem(capacity1, capacity2, target)
if solution:
    print("Path of states by jugs followed is :\n")
    for state in solution:
        print(f"{state[0]} , {state[1]}")
else:
    print("No solution found.")