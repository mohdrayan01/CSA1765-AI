# Write a Prolog Program to suggest Dieting System based on Disease. 
diet(diabetes, low_sugar).
diet(bp, low_salt).
diet(obesity, low_fat).

suggest_diet(Disease, Diet) :-
    diet(Disease, Diet).