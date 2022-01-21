import random as rd
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {student:rd.randint(0,100) for student in names}

passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)