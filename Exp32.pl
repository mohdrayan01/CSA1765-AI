# Write a Prolog program to implement pattern matching 
% Pattern matching example

match_pattern([], _).   % Empty pattern always matches

match_pattern([H|T], [H|T2]) :-
    match_pattern(T, T2).
