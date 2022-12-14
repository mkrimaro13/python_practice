x = 3.3
y = 1.1 + 2.2
print(x)
print(y)
print(x == y)
print('*' * 30)
# Forma con Strings
y_str = format(y, ".2g")
print(y_str)
print(y_str == str(x))
print('*' * 30)
# Forma Matemática
print(x, y)
tolerance = 0.00001
print(abs(x - y) < tolerance)
print('*' * 30)
# Redondeando
print(round(y, 1))
print(type(round(y, 1)))
print(round(y, 1000) == x)
