# Write the python program for Missionaries Cannibal problem
from collections import deque
def is_valid(m_left, c_left):
    m_right = 3 - m_left
    c_right = 3 - c_left
    if (m_left > 0 and c_left > m_left):
        return False
    if (m_right > 0 and c_right > m_right):
        return False
    return True
def missionaries_cannibals():
    initial = (3, 3, 1)  
    goal = (0, 0, 0)
    queue = deque([(initial, [])])
    visited = set()
    while queue:
        (m, c, boat), path = queue.popleft()
        if (m, c, boat) in visited:
            continue
        visited.add((m, c, boat))
        path = path + [(m, c, boat)]
        if (m, c, boat) == goal:
            return path
        moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
        for dm, dc in moves:
            if boat == 1: 
                new_state = (m-dm, c-dc, 0)
            else:          
                new_state = (m+dm, c+dc, 1)
            nm, nc, nb = new_state
            if 0 <= nm <= 3 and 0 <= nc <= 3 and is_valid(nm, nc):
                queue.append((new_state, path))
    return None
solution = missionaries_cannibals()
if solution:
    print("\nSolution Steps:\n")
    for step in solution:
        m_left, c_left, boat = step
        m_right = 3 - m_left
        c_right = 3 - c_left
        print(f"Left Side  -> Missionaries: {m_left}, Cannibals: {c_left}")
        print(f"Right Side -> Missionaries: {m_right}, Cannibals: {c_right}")
        if boat == 1:
            print("Boat is on LEFT side")
        else:
            print("Boat is on RIGHT side")
        print("--------------------------------")
else:
    print("No solution found.")