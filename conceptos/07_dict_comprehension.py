import random

dict = {}
for i in range(1, 5):  # Forma con ciclo
    dict[i] = i * 2
print(f'dict: {dict}')

dict_2 = {i: (i * 2) for i in range(1, 5)}  # Sintaxis reducida
print(f'dict_2: {dict_2}')

countries = ['col', 'mex', 'bol', 'pe']
population_1 = {}
for country in countries:  # Forma con ciclo
    population_1[country] = random.randint(1, 100)
print(f'population_1: {population_1}')

population_2 = {country: random.randint(1, 100) for country in countries}  # Sintaxis reducida
print(f'population_2: {population_2}')

# Para crear diccionarios a partir de dos listas:
names = ['marco', 'manuela', 'claudia', 'lucas']
ages = [21, 20, 49, 10]
zp = list(zip(names, ages))  # Se puede usar la función "zip"y convertirla en una lista.
print(f'zip: {zp}')
people = {name: age for (name, age) in zp}  # Luego con este nuevo objeto se crea el diccionario
print(f'people_1: {people}')

names = ['marco', 'manuela', 'claudia', 'lucas']
ages = [21, 20, 49, 10]
people = {names[i]: ages[i] for i in range(len(names))}  # Se crea el diccionario directamente usando los índices

population = [random.randint(1, 100) for n in range(len(countries))]
print(f'population: {population}')
population_3 = {countries[i]: population[i] for i in range(len(countries))}
print(f'population_3: {population_3}')

population_4 = {countries[i]: population[i] for i in range(len(countries)) if population[i] > 20}
population_5 = {countries[i]: population[i] for i in range(len(countries)) if population[i] < 20}
print(f'population_4 > 20: {population_4}')
print(f'population_5 < 20: {population_5}')

text = 'Hola, me llamo marco y estoy bien'
unique = {c: c.upper() for c in text if c in 'aeiou'}  # Crea un diccionario reemplazando la minúscula por la mayuscula
print(f'unique: {unique}')
unique_2 = {c: text.count(c) for c in text if c in 'aeiou'}  # Crea un diccionario indicando la frecuencia de cada vocal
print(f'unique_2: {unique_2}')
