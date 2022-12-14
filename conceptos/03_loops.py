i=0
while i <= 10:
	print(i)
	i+=1

i=0
while i < 10:
	print(i)
	if i == 5:
		break # Rompe al llegar a 5
	i+=1 

# Elementos iterables

#Listas
lista=[23, 45, 67, 89, 43]
for elemento in lista:
	print(elemento)

tupla=('marco', 'manuela', 'lucas', 'claudia')
for elemento in tupla:
	print(elemento)

producto ={
	'name': 'camisa',
	'price': 1, 
	'stock': 100
}

for elemento in producto:
	print(elemento) # Imprime solo las llaves

for elemento in producto:
	print(producto[elemento]) # Imprime solo los valores

for llave in producto:
	print(llave, ':', producto[llave]) # Imprime llaves y valores

for llave, valor in producto.items():
	print(llave,':', valor) # Imprime llaves y valores

people = [
	{
		'name':'marco',
		'age': 21
	},
	{
		'name':'manuela',
		'age': 20
	},
	{
		'name':'claudia',
		'age': 49
	}
]

for persona in people:
	print(persona)



matriz = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]

for renglon in matriz:
	for numero in renglon:
		print(numero)

