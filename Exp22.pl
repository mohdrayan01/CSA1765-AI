# Write a Prolog Program to print particular bird can fly or not. Incorporate required queries. 
bird(peacock).
bird(parrot).
bird(penguin).

can_fly(parrot).
can_fly(peacock).

fly(X) :-
    bird(X),
    can_fly(X).

not_fly(X) :-
    bird(X),
    \+ can_fly(X).