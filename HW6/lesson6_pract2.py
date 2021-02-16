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

python = []

for i in names:
    if len(python) < 5:
        python.append(i)
    else:
        break
print(python)
