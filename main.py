import random


def elec(a):  # Definición de opciones
    if a == 1:
        return ('piedra')
    elif a == 2:
        return ('papel')
    elif a == 3:
        return ('tijeras')
    else:
        return ('No hay elección, vuelve a intentar')


def text():  # Definición de textos
    print(f'Has elegido {elec(user)}')
    print(f'La máquina a elegido {elec(pc)}')


def game():  # Lógica del juego
    if user == pc:
        text()
        print('Empate')
    elif (user == 1 and pc == 3) or (user == 2 and pc == 1) or (user == 3 and pc == 2):
        text()
        print('Ganaste')
    else:
        text()
        print('Perdiste')


i = 0
print('Hola, bienvenido al juego de piedra, papel o tijeras: ')
while i != 1:  # Inicialización del juego
    user = int(input('Escoge entre \n 1. Piedra. \n 2. Papel. \n 3. Tijeras \n'))
    pc = random.randint(1, 3)
    game()
    i = int(input("¿Deseas salir?: \n 0. No \n 1. Si \n"))
print('¡Adios!')
