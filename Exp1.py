# Write the python program to solve 8-Puzzle problem
from queue import PriorityQueue

goal_state = (1,2,3,4,5,6,7,8,0)

def heuristic(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            goal_pos = goal_state.index(state[i])
            distance += abs(i//3 - goal_pos//3) + abs(i%3 - goal_pos%3)
    return distance

def get_neighbors(state):
    neighbors = []
    i = state.index(0)
    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    for dx, dy in moves:
        x, y = i//3 + dx, i%3 + dy
        if 0 <= x < 3 and 0 <= y < 3:
            new_index = x*3 + y
            new_state = list(state)
            new_state[i], new_state[new_index] = new_state[new_index], new_state[i]
            neighbors.append(tuple(new_state))

    return neighbors

def solve(start):
    pq = PriorityQueue()
    pq.put((heuristic(start), 0, start, []))
    visited = set()

    while not pq.empty():
        _, cost, state, path = pq.get()

        if state == goal_state:
            return path + [state]

        if state in visited:
            continue

        visited.add(state)

        for neighbor in get_neighbors(state):
            pq.put((heuristic(neighbor)+cost+1, cost+1, neighbor, path+[state]))

    return None

initial = (1,2,3,4,6,7,5,8,0)
solution = solve(initial)

if solution:
    for step in solution:
        print(step[0:3])
        print(step[3:6])
        print(step[6:9])
        print()
else:
    print("No solution found")