import functools
numbers = [1,2,3,4]
result =  functools.reduce(lambda counter, item : counter + item, numbers)
print(result)

def accum(counter, item):
    print(f'counter: {counter}')
    print(f'item: {item}')
    return counter + item
result =  functools.reduce(accum, numbers)
print(result)

