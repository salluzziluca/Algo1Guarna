torneo_1 =[['Boca', 'Racing',3, 1],['Ferro', 'River',4 , 1],['Ferro', 'Racing',0 , 1],['Boca', 'River',2 , 1]] 

def jugo_todos_partidos(torneo, equipo):
    partidos_jugados = 0
    for partido in torneo:
        partidos_jugados += partido.count(equipo)
    return partidos_jugados >= 2
def ganador(partido):
    diferencia_de_goles = partido[2] - partido[3]
    if diferencia_de_goles > 0:
        ganador = partido[0]
    if diferencia_de_goles < 0:
        ganador = partido[1]  
    else:
        ganador = False  

def sumatoria_puntos(torneo, equipo):
    puntos = 0
    for partido in torneo:
        if equipo == partido[0]:
            ganador = ganador()
            
        elif equipo == partido[1]:
            
        
        
jugo_todos_partidos(torneo_1, 'Boca')
