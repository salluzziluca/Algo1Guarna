"""
El diccionario runners tiene cargados a corredores desesperados por volver a correr. 
El nombre de cada corredor es la clave y se le asocia una lista de dos numeros:
    - el primero es la cantidad de kilometros que corria asiduamente antes de la cuarentena (flotante),
    - el segundo es el tiempo que tardaba en hacerlo (entero dado en minutos).

Se pide que hagas un programa en Python, compuesto por funciones, que:

Indique el promedio de kilometros corridos por todos los corredores.
Liste los corredores ordenados de mayor a menor por velocidad promedio.
Indicando:

corredor - velocidad (km / min)
"""
from corredores import raners

NOMBRE = 0
DATOS = 1
KILOMETROS_CORRIDOS = 0
TIEMPO_TOTAL = 1
VELOCIDAD = 1

def obtener_diccionario():
    return raners

def promedio_kilometros(runners):
    """
    recibe un diccionario con nombres, velocidades y tiempo, devuelve el promedio de kilometros recorridos.
    """
    kilometros_totales = 0
    
    for informacion_corredor in runners.values():
        
        kilometros_totales+= informacion_corredor[KILOMETROS_CORRIDOS]
        promedio =kilometros_totales/len(runners.values())
        
    return(promedio)


def crear_ranking_velocidades(runners):
    """
    recibe un diccionario con nombres, velocidades y tiempo, devuelveuna lista ordenada de mayor a menor con las velocidades promedio de todos los correodes.
    """
    lista_velocidades_promedio=[]
    
    for corredor in runners.items():
        velocidades_promedio=corredor[DATOS][KILOMETROS_CORRIDOS]/corredor[DATOS][TIEMPO_TOTAL]
        lista_velocidades_promedio.append([corredor[NOMBRE], velocidades_promedio])
        lista_velocidades_promedio.sort(reverse= True, key = lambda x:x[1])
        
    return lista_velocidades_promedio
    
def imprimir_ranking_velocidades(lista):
    """
    recibe una lista de velocidades y corredores, la imprime por pantalla
    """
    
    for item in lista:
        print(f'{item[NOMBRE]} - {item[VELOCIDAD]}(km/min)')



def main():
    runners = obtener_diccionario()
    
    promedio_distancia=promedio_kilometros(runners)
    print(f'El promedio de kilometros corridos fue de {promedio_distancia}')
    lista_velocidades_promedio = crear_ranking_velocidades(runners)
    imprimir_ranking_velocidades(lista_velocidades_promedio)
     
main()

