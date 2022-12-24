import utils

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
    
def run():
    keys, values = utils.get_population()
    print(keys, values)
    country = input('Ingresa el país que deseas consultar:  ')  # Se debe escribir el nombre bien para que se pueda realizar la consulta
    result = utils.population_by_country(data, country)
    print(result)

if __name__ == '__main__':
    run() # Entry point