print('Lista inicial: ')
num = [1, 2, 3, 4]
print(num)

print('Utilizando un ciclo')
num_2 = []
for i in num:
  num_2.append(i * 2)
print(num_2)

print('Definiendo una función y utilizando la clase map')


def m2(a):
  return a * 2


num_2 = map(m2, num)
print(list(num_2))

print('Definiendo una función lambda y utilizando la clase map')
num_2 = map(lambda x: x * 2, num)
print(list(num_2))

print(
  '******************************************************************************************************'
)

print('Manejo de listas de diferentes tamaños')
n1 = [1, 2, 3, 4]
n2 = [5, 6, 7]
print(f'n1: {n1}\nn2: {n2}')
result = map(lambda x, y: x + y, n1, n2)
print(list(result))

print(
  '******************************************************************************************************'
)

print("Manejo de diccionarios en map")
inventory = [{
  'product': 'shirt',
  'price': 100,
  'stock': True
}, {
  'product': 'T-shirt',
  'price': 101,
  'stock': False
}, {
  'product': 'Jean',
  'price': 209,
  'stock': True
}, {
  'product': 'Cap',
  'price': 40,
  'stock': False
}]

print('Lista de precios: ')
prices = list(map(lambda item: item['price'], inventory))
print(prices)

print('Anexión de impuestos: ')


def add_taxes(item):
  new_inv = item.copy()
  new_inv['taxes'] = new_inv[
    'price'] * 0.19  # Añade el nuevo atributo "taxes" y le añade el 19% de impuestos
  return new_inv


inventory_w_taxes = list(map(add_taxes, inventory))
print(inventory_w_taxes)