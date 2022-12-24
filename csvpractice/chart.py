import matplotlib.pyplot as plt

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