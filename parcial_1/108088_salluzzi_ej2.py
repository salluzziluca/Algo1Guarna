"""
Escribi una funcion que devuelva verdadero si un alumno aprobo la cursada de la materia, o de lo contrario falso.
La funcion recibe dos listas: una de trabajos practicos (tps) y otra de notas.
La lista de tps puede tener tres valores: "no sat", "sat", "supera"; que se corresponden con: "No Satisfactorio", "Satisfactorio" y "Supera lo esperado".
La lista de notas es numerica con valores del 1 al 10 y puede tener desde una nota (si es 4 o mas) hasta tres notas (si las dos primeras son menores a 4).

Se aprueba la cursada cuando:

- La lista tps tiene TODOS los valores con "satisfactorio" o "supera lo esperado" Y 
- la lista notas tiene por lo menos un 4 o mas.

Comproba el correcto funcionamiento, mediante los siguientes casos de prueba usando la librería doctest.
Ademas, agrega DOS casos de prueba adicionales,en donde uno sea Falso y el otro Verdadero.
Casos de Prueba:

     aprobo_cursada(["sat", "supera", "sat"], [2, 2])
    False
     aprobo_cursada(["sat", "no sat", "supera", "sat"], [2, 8])
    False
    aprobo_cursada(["sat"], [6])
    True
"""
import doctest

def aprobo_cursada(trabajos_practicos, notas):
    """Recibe una lista de trabajos practicos y una de notas. Devuelve un booleano segun si el alumno aprobó (todos los tps con satisfactorio o supera y alguna nota mayor o igual a 4).
    >>> aprobo_cursada(["sat", "supera", "sat"], [2, 2])
    False
    >>> aprobo_cursada(["sat", "no sat", "supera", "sat"], [2, 8])
    False
    >>> aprobo_cursada(["sat"], [6])
    True
    """
    aprobacion_tps = True
    i = 0
    while i < len(trabajos_practicos) and aprobacion_tps:
        if trabajos_practicos[i] == 'no sat':
            aprobacion_tps = False
        i+=1
            
    aprobacion_examenes = False
    i = 0
    while i < len(notas) and not aprobacion_examenes:
        if notas[i] >= 4:
            aprobacion_examenes = True
        i+=1
    return (aprobacion_tps and aprobacion_examenes)

print(doctest.testmod())