# Write the python to implement Travelling Salesman Problem 
import math
def dist(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
def tsp(c):
    t = [0]
    u = set(range(1, len(c)))
    total = 0
    while u:
        cur = t[-1]
        nxt = min(u, key=lambda x: dist(c[cur], c[x]))
        total += dist(c[cur], c[nxt])
        t.append(nxt)
        u.remove(nxt)
    total += dist(c[t[-1]], c[0])
    t.append(0)
    return t, total
cities = [(0,0), (1,2), (3,1), (4,3)]
tour, d = tsp(cities)
print("Tour:", tour)
print("Total Distance:", round(d,2))