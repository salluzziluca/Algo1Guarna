def cargar_voto(diccionario, partido, votos):
    if partido in votacion.keys():
        votacion[partido]+=votos
    else:
         votacion[partido]=votos

votacion = {}
seguir = 's'
partido = input('Ingrese el partido a sumarle votos: ')
votos = int(input('Ingrese la cantidad de votos a sumarle: '))
cargar_voto(votacion, partido, votos)
seguir = input('Desea seguir ingresando?(s/n): ')
while seguir != 'n':
    partido = input('Ingrese el partido a sumarle votos: ')
    votos = int(input('Ingrese la cantidad de votos a sumarle: '))
    cargar_voto(votacion, partido, votos)
    seguir = input('Desea seguir ingresando?(s/n): ')
    
lista_votos = list(votacion.items())
lista_votos.sort(reverse = True)
for item in lista_votos:
    print(f'El partido {item[0]} obtuvo {item[1]} votos.')