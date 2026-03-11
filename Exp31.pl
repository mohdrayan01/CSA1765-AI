# Write a Prolog program to find the number of vowels 
% Check if a character is a vowel
vowel(a).
vowel(e).
vowel(i).
vowel(o).
vowel(u).

% Base case: empty list has 0 vowels
count_vowels([], 0).

% If head is vowel, increment count
count_vowels([H|T], Count) :-
    vowel(H),
    count_vowels(T, Rest),
    Count is Rest + 1.

% If head is not vowel, skip
count_vowels([H|T], Count) :-
    \+ vowel(H),
    count_vowels(T, Count).