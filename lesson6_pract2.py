# Создать структуру данных для студентов из имен и фамилий, можно случайных.
# Придумать структуру данных, чтобы указывать, в какой группе учится студент (Группы Python, FrontEnd, FullStack, Java).
# Студент может учиться в нескольких группах. Затем вывести:
# cтудентов, которые учатся в двух и более группах
# студентов, которые не учатся на фронтенде
# студентов, которые изучают Python или Java
# SDgdzhnfgncvbmftyjdtxn

from random import choice

names = (
    'Joel Tucker', 'Erin Stephens', 'Vanesa Rosales', 'Mckenzie Goddard', 'Carley Cortes', 'Lilith Thomson',
    'Gail Arias',
    'Luci Bannister', 'Eoin Gallegos', 'Rayhan Davie', 'Patrik Odling', 'Umayr Rice', 'Karim Hernandez', 'Tea Cope',
    'Etienne Gallagher', 'Sanjeev Rhodes', 'Shelbie Black', 'Juan Stokes', 'Dominykas Richardson', 'Tabitha Bautista')
python = []
frontend = []
fullstac = []
java = []
while not len(python) == len(frontend) == len(fullstac) == len(java) == 3:
    python.append(choice(names))
    frontend.append(choice(names))
    fullstac.append(choice(names))
    java.append(choice(names))

python = set(python)
frontend = set(frontend)
fullstac = set(fullstac)
java = set(java)

print(python, '\n' + str(frontend), '\n' + str(fullstac),'\n' + str(java))

all1 = python & frontend & fullstac & java
not_front = python & fullstac & java - frontend
# print(all1)
print(not_front)
