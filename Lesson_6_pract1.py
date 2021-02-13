# Создать словарь оценок предполагаемых студентов (Ключ - ФИ студента, значение - список оценок студентов).
# Найти самого успешного и самого отстающего по среднему баллу.

students = {'Ivan Ivanov': [5, 4, 3, 5], 'Petr Petrov': [5, 3, 2, 1], 'Sidor Sidorov': [1, 3, 5, 5]}
average_mark_stud = dict((name, sum(mark)/len(mark)) for name, mark in students.items())
print(average_mark_stud)

best = max(average_mark_stud, key=average_mark_stud.get)
bed = min(average_mark_stud, key=average_mark_stud.get)

print(best + " is the most successful student")
print(bed + " is student with  bad academic results")