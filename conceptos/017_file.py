###### Abriendo un archivo

file = open('conceptos/017_text.txt') # dentro de los parentesis va la ruta del archivo
# print(file.read()) # Todo el documento
# print(file.readline()) # 1er renglón
# print(file.readline()) # 2do renglón
# print(file.readline()) # 3er renglón

# for line in file:
 #   print(line)
    
# file .close()

# with open('conceptos/017_text.txt') as file:
#    for line in file:
#     print(line)
     

###### Modificando el archivo
with open('conceptos/017_text.txt', 'r+') as file:
    for line in file:
     print(line)
    
    file.write('\nhola\n')