# Write a Prolog Program for fruit and its color using Back Tracking. 
fruit(apple, red).
fruit(banana, yellow).
fruit(grapes, green).
fruit(orange, orange).

fruit_color(Fruit, Color) :-
    fruit(Fruit, Color).