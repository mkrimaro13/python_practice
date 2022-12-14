# Union
a = {1, 2, 3, 4}
b = {4, 5, 6, 7}
c = a.union(b)
print(c)
c = a | b
print(c)

# Interseccion
a = {1, 2, 3, 4}
b = {4, 5, 6, 7}
c = a.intersection(b)
print(c)
c = a & b
print(c)

# Diferencia
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
c = a.difference(b)
print(c)
c = a - b
print(c)

# Diferencia Simétrica
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
c = a.symmetric_difference(b)
print(c)
c = a ^ b
print(c)
