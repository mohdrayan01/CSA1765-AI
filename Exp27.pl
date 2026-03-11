# Write a Prolog Program to implement Best First Search algorithm 
best_first(Start, Goal, Path) :-
    bfs([[Start]], Goal, Path).

bfs([[Goal|Rest]|_], Goal, [Goal|Rest]).
bfs([[Node|Rest]|Others], Goal, Path) :-
    findall([Next,Node|Rest],
            (edge(Node,Next), \+ member(Next,[Node|Rest])),
            NewPaths),
    append(Others, NewPaths, UpdatedQueue),
    bfs(UpdatedQueue, Goal, Path).

edge(a,b).
edge(a,c).
edge(b,d).
edge(c,e).