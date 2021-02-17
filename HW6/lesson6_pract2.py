# Создать структуру данных для студентов из имен и фамилий, можно случайных.
# Придумать структуру данных, чтобы указывать, в какой группе учится студент (Группы Python, FrontEnd, FullStack, Java).
# Студент может учиться в нескольких группах. Затем вывести:
# cтудентов, которые учатся в двух и более группах
# студентов, которые не учатся на фронтенде
# студентов, которые изучают Python или Java

from random import choice

names = (
    'Joel Tucker', 'Erin Stephens', 'Vanesa Rosales', 'Mckenzie Goddard', 'Carley Cortes', 'Lilith Thomson',
    'Gail Arias',
    'Luci Bannister', 'Eoin Gallegos', 'Rayhan Davie', 'Patrik Odling', 'Umayr Rice', 'Karim Hernandez', 'Tea Cope',
    'Etienne Gallagher', 'Sanjeev Rhodes', 'Shelbie Black', 'Juan Stokes', 'Dominykas Richardson', 'Tabitha Bautista')

python = set()
frontend = set()
fullstack = set()
java = set()

while len(java) < 6:
    python.add(choice(names))
    frontend.add(choice(names))
    fullstack.add(choice(names))
    java.add(choice(names))



student_dict = {'python': list(python), 'frontend': list(frontend),
                'fullstack': list(fullstack), 'java': list(java)}

several_group = python & frontend & fullstack & java
not_front = (python | java | fullstack) - frontend
py_or_java = python ^ java

if len(several_group) == 0:
    print('Никто из студентов не учиться в двух и более группах')
else:
    print('Вот список студентов, которые обучаются в двух и более группах:\n'
          + str(several_group))

if len(not_front) == 0:
    print('На данный все студенты учаться на Frontend.')
else:
    print('Вот список студентов, которые не учатся на Frontend:\n'
          + str(not_front))

if len(py_or_java) == 0:
    print('На данный момент все студенты обучаются в обеих группах.')
else:
    print('Вот список студентов, которые изучают Python или Java:\n'
          + str(py_or_java))