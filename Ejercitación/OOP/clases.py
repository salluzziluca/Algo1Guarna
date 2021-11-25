class Estudiante:
    pass

def main():
    estudiante_1 = Estudiante()
    estudiante_2 = Estudiante()
    
    estudiante_1.nombre = 'Tato'
    estudiante_1.apellido = 'Conti'
    estudiante_2.nombre = 'Luca'
    estudiante_2.mail = 'salluzzi.luca@gmail.com'
    print(f'{estudiante_1.nombre} {estudiante_1.apellido}')
main()