# Write a Prolog Program for forward Chaining. Incorporate required queries. 
fact(a).
fact(b).

rule(c) :- fact(a), fact(b).

forward(X) :-
    rule(X).
    