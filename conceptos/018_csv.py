import csv # módulo estándar de python para trabajar con archivos csv

'''
def read_csv(path): # Definición de una función para leer el archivo, se incluye una variable que es la ruta donde se encuentra el archivo
    with open(path, 'r') as csvfile: # método para abrir y cerrar el archivo, con permiso de SOLO lectura (r, read)
        reader = csv.reader(csvfile, delimiter=';') # Creación de una variable con la función reader del módulo csv, incluye el archivo, y luego el delimitador de los datos dentro del archivo
        for row in reader: # Ciclo for para iterar por cada línea o renglón dentro del archivo
            print('***' * 70) # Separador de cada línea
            print(row) # Imprime cada línea

if __name__ == '__main__':
    read_csv('./conceptos/data.csv') # Imprime la información en forma de lista
'''

### Convirtiendo la información en diccionarios
def read_csv(path):
    with open(path, 'r') as csvfile: 
        reader = csv.reader(csvfile, delimiter=';') 
        header = next(reader) # Imprime la primera lista, es decir los encabezados que son las llaves para los diccionarios
        data = []
        for row in reader: 
            population = {header[i]:row[i] for i in range(len(row))} # Creación de diccionario con sintaxis reducida, se usa la cabecera como la llave, y cada línea es el contenido
            data.append(population) # Se añade el contenido a una lista vacía.
        return data

if __name__ == '__main__':
    info = read_csv('./conceptos/data.csv') # Imprime la información en forma de lista
    print(info[0])