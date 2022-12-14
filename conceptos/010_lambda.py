def increment(x):
	return x + 1

lambda x : x + 1

increment_2 = lambda x : x + 1

full_name = lambda name, last_name : f'Full name is {name.title()} {last_name.title()}'
text = full_name('marco', 'osorio')
print(text)

def hof(x, function):
	return x + function(x)

# Solamente se pone el nombre de la función que interesa utilizar, no se hace el llamado normal
result = hof(2, increment)  # 2 + ( 2 + 1)
print(result)

increment= lambda x : x + 1
hof= lambda x, function : x + function(x)

result = hof(2, increment)
print(result)

hof= lambda x, function : x + function(x)
result = hof(2, lambda x: x + 5)
print(result)

result = hof(2, lambda x: x * 5)
print(result)