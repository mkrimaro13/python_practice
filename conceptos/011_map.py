def myfunc(a):
  return len(a)

x = map(myfunc, ('apple', 'banana', 'cherry'))

print(x)

#convert the map into a list, for readability:
print(list(x))

print('***********************************************************************************************************************')

def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

print(x)

#convert the map into a list, for readability:
print(list(x))

print('***********************************************************************************************************************')

num = [1, 2, 3 ,4]
print(num)

print('Utilizando un ciclo')
num_2 =[]
for i in num:
    num_2.append(i * 2)
print(num_2)

print('Definiendo una función y utilizando la clase map')
def m2(a):
    return a * 2
num_2 = map(m2, num)
print(list(num_2))

print('Definiendo una función lambda y utilizando la clase map')
num_2 = map(lambda x: x*2, num)
print(list(num_2))

print('***********************************************************************************************************************')

n1=[1,2,3,4]
n2=[5,6,7]
print(f'n1: {n1}, n2: {n2}')
result = map(lambda x, y : x + y, n1, n2)
print(list(result))