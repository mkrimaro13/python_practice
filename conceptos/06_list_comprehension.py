numbers = []
for num in range(1, 11):  # Forma con ciclos
    numbers.append(num)
print(f'numbers: {numbers}')

numbers_2 = [num for num in range(1, 11)]  # sintaxis reducida
print(f'numbers_2: {numbers_2}')

numbers = []
for num in range(1, 11):  # Forma con ciclos
    numbers.append(num * 2)
print(f'numbers * 2: {numbers}')

numbers_2 = [num * 2 for num in range(1, 11)]  # sintaxis reducida
print(f'numbers_2 * 2: {numbers_2}')

numbers_pairs = []
for num in range(1, 11):  # Forma con ciclos
    if num % 2 == 0:
        numbers_pairs.append(num)
print(f'numbers_pairs: {numbers_pairs}')

numbers_pairs_2 = [num for num in range(1, 11) if num % 2 == 0]  # sintaxis reducida
print(f'numbers_pairs_2: {numbers_pairs_2}')
