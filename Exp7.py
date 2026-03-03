# Write the python program to implement BFS. 
from collections import deque
def bfs(adj_list, start, end):
    queue = deque([(start, [start])])
    visited = set()
    traversal = []
    shortest_path = None
    while queue:
        node, path = queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal.append(node)
            if node == end and shortest_path is None:
                shortest_path = path   # store shortest path but don't stop
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return shortest_path, traversal
if __name__ == '__main__':
    graph = {
        1: [2, 3],
        2: [1],
        3: [1, 4],
        4: [3]
    }
start_node = 1
end_node = 4
shortest_path, traversal = bfs(graph, start_node, end_node)
print("BFS Traversal:", traversal)
