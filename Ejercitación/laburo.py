'''
Se pide construir un programa que nos permita obtener estadísticas del mercado laboral por localidad con el fin de poder realizar comparaciones.

Para comenzar, se deben comenzar cargando en un dict_laburo pares de datos localidad-personas, donde el valor de las personas hace referencia a la cantidad de personas que se encuentra en edad de trabajar.
Debe tenerse en cuenta que, como los datos se obtienen de distintas planillas, es posible que se ingrese más de un par clave-valor asociada a una localidad.

Una vez que el usuario terminar de realizar la carga, se deben imprimir:

a) El total de personas en edad laboral y el total de empleados para cada localidad.

b) Un listado ordenado de mayor a menor por porcentaje de desocupación. Debe tenerse en cuenta que para determinar el porcentaje de desocupación se puede utilizar la fórmula:

% desocupacion = (1 - empleados / personas en edad de trabajar) * 100

En el siguiente ejemplo se detallan los mensajes que deben ser mostrados al usuario. Recordar que para que el ejercicio pase las pruebas, se tiene que mostrar exactamente el mismo.
'''
dict_laburo={}
lista_desocupacion=[]
def cargar_datos(dict_laburo, localidad, personas_capaces, empleados):
    data_localidad = [personas_capaces, empleados]
    
    if localidad in dict_laburo.keys():
        zip_data_localidad= zip(dict_laburo[localidad], data_localidad)
        data_localidad = [x+y for(x,y) in zip_data_localidad]
        dict_laburo[localidad]=data_localidad
        
    else:
         dict_laburo[localidad]=data_localidad
    
    
def desocupacion(lista_desocupacion, dict_laburo, localidad):
    if localidad in lista_desocupacion:
        sdesocupacion_cuenta = (1 - empleados / personas_capaces) * 100
    else:
        desocupacion_cuenta = (1 - dict_laburo[localidad][1] / dict_laburo[localidad][0]) * 100
        lista_desocupacion.append([localidad, desocupacion_cuenta]) 
         
localidad=input('Ingrese localidad: ')
personas_capaces=int(input('Ingrese la cantidad de personas que pueden trabajar: '))
empleados=int(input('Ingrese la cantidad de empleados: '))
continuidad=input('Desea seguir ingresando?(s/n): ')

cargar_datos(dict_laburo, localidad, personas_capaces, empleados)
#desocupacion(lista_desocupacion, localidad, empleados, personas_capaces)

while continuidad == 's':
    localidad=input('Ingrese localidad: ')
    personas_capaces=int(input('Ingrese la cantidad de personas que pueden trabajar: '))
    empleados=int(input('Ingrese la cantidad de empleados: '))
    
    cargar_datos(dict_laburo, localidad, personas_capaces, empleados)
    #desocupacion(lista_desocupacion, localidad, empleados, personas_capaces)
    continuidad=input('Desea seguir ingresando?(s/n): ')


for item in dict_laburo.items():
    desocupacion_cuenta = (1 - item[1][1] / item[1][0])*100
    lista_desocupacion.append([item[0], desocupacion_cuenta]) 
    print(f'En la localidad de {item[0]} hay {item[1][0]} personas en edad laboral y {item[1][1]} trabajando.')
lista_desocupacion = sorted(lista_desocupacion, reverse= True, key =  lambda x: x[1])
for item in lista_desocupacion:
    
    print(f'La tasa de desocupacion en {item[0]} es {item[1]}%.')



