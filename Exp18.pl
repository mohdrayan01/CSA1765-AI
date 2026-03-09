# Write a Prolog Program for A DB WITH NAME, DOB. 
person(john, date(12,5,1998)).
person(mary, date(3,8,2000)).
person(raj, date(15,1,1999)).

get_dob(Name, DOB) :-
    person(Name, DOB).