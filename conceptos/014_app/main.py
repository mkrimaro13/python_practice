import mod

keys, values = mod.get_population()
print(keys, values)

data = [
    {
        'country' : 'Colombia',
        'Population' : 500
    },
    {
        'country' : 'Bolivia',
        'Population' : 300
    }
]
country = input('Ingresa el país que deseas consultar:  ')  # Se debe escribir el nombre bien para que se pueda realizar la consulta
result = mod.population_by_country(data, country)
print(result)