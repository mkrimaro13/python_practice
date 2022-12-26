import csvpractice.filter as filter
import csvpractice.reader as reader
import csvpractice.chart as chart
'''
Este Script, toma la información de los módulos en el paquete csvpractice, para la lectura y filtrado de un archivo csv sacado de www.kaggle.com sobre la población mundial, adicional imprime dos graficas utilizando la librería matplotlib.
'''
def run():
    data = reader.read_csv('./conceptos/data.csv')
    country = input('Ingresa el país que deseas consultar: ').title()
    filtered_country = filter.country_filter(data, country)
    print(filtered_country)
    print(f'La información individual de la población de {country} es: ')
    filtered_population = filter.header_filter(filtered_country)
    print(filtered_population)
    labels = filtered_population.keys()
    values = filtered_population.values()
    chart.gen_bar_chart(labels, values)
    chart.gen_pie_chart(labels, values)
    labels = filter.column_filter(data).keys()
    values = filter.column_filter(data).values()
    chart.gen_pie_chart(labels, values)

if __name__ == '__main__':
    run()