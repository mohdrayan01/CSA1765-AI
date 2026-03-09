# Write a Prolog Program for STUDENT-TEACHER-SUB-CODE. 
student(101, ramesh).
student(102, suresh).

teacher(t1, math).
teacher(t2, physics).

teaches(t1, 101).
teaches(t2, 102).

student_teacher(StudentID, TeacherID) :-
    teaches(TeacherID, StudentID).