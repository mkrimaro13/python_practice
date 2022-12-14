price = 100  # Variable global

def increment():
    price = 100  # Variable local
    result = price + 5  # Variable local
    price = price + 1
    return price

print(price)
price_2 = increment()
print(price_2)