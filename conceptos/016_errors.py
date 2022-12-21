# print(0/0) # ZeroDivisionError: division by zero

print('hola 1')
suma = lambda x,y : x + y
assert suma(2,2) == 4  # Esta línea no retorna nada
print('hola 2')

''''
print('hola 1')
suma = lambda x,y : x + y
assert suma(2,2) != 4  # Genera error y finaliza el programa
print('hola 2')

age = 10
if age < 18:
    raise Exception('No se permiten menores de 18')
    
    try:
    print(0/0)
except ZeroDivisionError as error:
    print(error)

try: 
    assert 1 != 1, 'Uno no es igual que uno'
except AssertionError as error:
    print(error)

try:
    age = 10
    if age < 18:
        raise Exception('No se permiten menores de 18')
except Exception as error:
    print(error)
'''

try:
    print(0/0)
    assert 1 != 1, 'Uno no es igual que uno'
    age = 10
    if age < 18:
        raise Exception('No se permiten menores de 18')
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)

print('Ejecutado')