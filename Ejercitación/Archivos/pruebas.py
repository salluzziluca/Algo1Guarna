archivo = open(r'\archivo.txt', 'r')
lineas = archivo.readlines()
for linea in lineas:
    print(linea, end = '')
archivo.close()