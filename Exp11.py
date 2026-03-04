# Write the python program for Map Coloring to implement CSP. 
class CSP:
    def __init__(self, variables, domains, neighbors):
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
    def is_valid(self, var, value, assignment):
        for neighbor in self.neighbors[var]:
            if neighbor in assignment and assignment[neighbor] == value:
                return False
        return True
    def backtrack(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment
        var = [v for v in self.variables if v not in assignment][0]
        for value in self.domains[var]:
            if self.is_valid(var, value, assignment):
                assignment[var] = value
                result = self.backtrack(assignment)
                if result:
                    return result
                del assignment[var]
        return None
variables = ['A', 'B', 'C', 'D']
domains = {v: ['Red', 'Green', 'Blue'] for v in variables}
neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}
csp = CSP(variables, domains, neighbors)
solution = csp.backtrack({})
print("Solution:", solution)