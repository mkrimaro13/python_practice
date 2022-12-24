import csv

def read_csv(path):
    with open(path, 'r') as csvfile: 
        reader = csv.reader(csvfile, delimiter=';') 
        header = next(reader) 
        data = []
        for row in reader: 
            population = {header[i]:row[i] for i in range(len(row))} 
            data.append(population) 
        return data

