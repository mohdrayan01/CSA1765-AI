# Write the python program to implement A* algorithm 
import heapq
def astar(s, g, nb, h):
    pq = []
    heapq.heappush(pq, (0, s))
    cf = {s: None}
    cost = {s: 0}
    while pq:
        _, cur = heapq.heappop(pq)
        if cur == g:
            break
        for n in nb(cur):
            nc = cost[cur] + 1
            if n not in cost or nc < cost[n]:
                cost[n] = nc
                pr = nc + h(n, g)
                heapq.heappush(pq, (pr, n))
                cf[n] = cur
    p = [g]
    while g != s:
        g = cf[g]
        p.append(g)
    return p[::-1], cost[p[0]]
gr = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}
def nb(x):
    return gr[x]
hv = {'A': 3, 'B': 2, 'C': 1, 'D': 0}
def h(x, g):
    return hv[x]
path, c = astar('A', 'D', nb, h)
print("Shortest Path:", path)
print("Cost:", c)