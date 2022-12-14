text = 'esternocleidomastoideo'
print(text)
print(text.count('e'))  # cuenta la cantidad de veces que hay una 'e'

text = 'eSteRnOclEIDOmastOIDeO'
print(text)
print(text.swapcase())  # Cambia entre mayúsculas y minúsculas

text = 'Buenos días'
print(text)
print(text.startswith('Buen'))  # Devuelve un Booleano, si la cadena inicia con una cadena que se le indique

text = 'Buenos días'
print(text)
print(text.replace('días', 'noches'))  # Reemplaza lo indicado en el primer espacio por lo que hay en el segundo espacio

text = 'esto es un título'
print(text)
print(text.title())  # Establece que sea un título poniendo el primer caracter em mayúsculas

text1 = '90'
text2 = 'Hola'
# Indica si el texto que hay indicado es un dígito/número y devuelve un booleano
print(text1.isdigit())  # True
print(text2.isdigit())  # False

# Indexing
i = 0
text = 'Hola'
while i < len(text):
    print(text[i])
    i += 1

# Slicing
text = "Hola, a mi me gustan las avongesas"
print(text)
print(text[0:4])
print(text[6:])
print(text[25:34:1])
print(text[25:34:2])
print(text[::-1])

lista = [1, 2, 3, 4, 5]
print(lista[:3])  # [1,2,3]
print(lista[::-1])  # [5, 4, 3, 2, 1]
