campeonato={'River': (2, 1, 4, 2, 5), 'Ferro':(5, 2, 2, 8, 3), 'Velez':(0, 1, 5, 2, 10), 'Boca':(3, 1, 2, 5, 6)}
campeon= ['Equipo', 0]
desciende=['Equipo', 100000]
mas_empates=['Equipo', 0]
goleador=['Equipo', 0]
for equipo in campeonato.items():
    nombre_equipo = equipo[0]
    estadisticas_equipo = equipo[1]


    puntos_equipo = estadisticas_equipo[0] *3 +estadisticas_equipo[1]
    if puntos_equipo > campeon[1]:
        campeon[0]=nombre_equipo
        campeon[1]= puntos_equipo

    
    if puntos_equipo < desciende[1]:
       desciende[0]=nombre_equipo
       desciende[1]= puntos_equipo

    
    
    empates = estadisticas_equipo[1] 
    if empates > mas_empates[1]:
        mas_empates[0] = nombre_equipo
        mas_empates[1]= empates
    
    
    ratio_goles = estadisticas_equipo[3]/estadisticas_equipo[4]
    if ratio_goles >goleador[1]:
        goleador[0]=nombre_equipo
        goleador[1]= ratio_goles

print(f'El equipo campeon es {campeon[0]} con {campeon[1]} puntos.')
print(f'El equipo que desciende es {desciende[0]} con {desciende[1]} puntos.')
print(f'El equipo que mas partidos empato es {mas_empates[0]} con {mas_empates[1]} partidos.')
print(f'El equipo con mejor proporcion goleadora es {goleador[0]} con {goleador[1]}.')

