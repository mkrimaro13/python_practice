import random

x = input("Quieres lanzar?")
while x != '0':
    d1 = random.choices([1, 2, 3, 4, 5, 6], k=2)
    print("Los dados son: ", d1)
    print("La suma de los dados es: ", d1[0] + d1[1])
    x = input("Escribe '0' para salir. O cual otra cosa para volver a lanzar: ")
print("Adios!")
