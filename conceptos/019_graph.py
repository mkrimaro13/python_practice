import matplotlib.pyplot as plt

'''
def gen_bar_chart():
    labels = ['a', 'b', 'c'] # Etiquetas, es el eje X
    values = [ 100, 200, 300] # Valores, es el eje Y
    fig, ax = plt.subplots() # Crea una figura y un conjunto de subramas
    ax.bar(labels, values) # función que toma los valores necesarios para convertirlo en un gráfico de barras
    plt.show() # muestra el gráfico
'''
# Gráfico de barras
def gen_bar_chart(labels, values): 
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

# Gráfico de torta
def gen_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()

if __name__ == '__main__':

    labels = ['a', 'b', 'c']
    values = [ 100, 80, 20]
    gen_bar_chart(labels, values)
    gen_pie_chart(labels, values)