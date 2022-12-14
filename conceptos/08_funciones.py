def suma(a, b):
    print(f'La suma es: {a + b}')


# suma(1, 2)

def suma_rango(min, max):
    print(f' Mínimo: {min}, Máximo: {max}')
    sum = 0
    for x in range(min, max):
        sum += x
    print(sum)


# suma_rango(23, 40)

def suma_rango_1(min, max):
    print(f' Mínimo: {min}, Máximo: {max}')
    sum = 0
    for x in range(min, max):
        sum += x
    return sum


# suma_rango_1(30, 99)
# resultado = suma_rango_1(30, 99)
# print(resultado)

def find_volume(length, width, depth):  # función sin valores por defecto
    return length * width * depth


# find_volume()

def find_volume_1(length=1, width=1, depth=1):
    return length * width * depth


# find_volume_1()
# find_volume_1(width = 10)

def find_volume_2(length=1, width=1, depth=1):
    return length * width * depth, width, 'hola'


# result = find_volume_2(width=10)
# print(result)
# print(result[0])
result, width, text = find_volume_2(width=10)
print(result)
print(width)
print(text)
