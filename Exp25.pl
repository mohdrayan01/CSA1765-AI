# Write a Prolog program to implement Monkey Banana Problem 
move(state(middle,onbox,middle,hasnot),
     grasp,
     state(middle,onbox,middle,has)).

move(state(P,onfloor,P,hasnot),
     climb,
     state(P,onbox,P,hasnot)).

move(state(P1,onfloor,P1,hasnot),
     push(P1,P2),
     state(P2,onfloor,P2,hasnot)).

move(state(P,onfloor,B,hasnot),
     walk(P,B),
     state(B,onfloor,B,hasnot)).