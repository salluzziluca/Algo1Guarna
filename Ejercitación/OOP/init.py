class Estudiante:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.university_email=f'{nombre[0]}{apellido}@fi.uba.ar'
      
def main():
    
    estudiante_1=Estudiante('Tato', 'Conti', 'abusto@gmail.com')
    estudiante_2=Estudiante('Luca', 'Salluzzi', 'salluzzi.luca@gmail.com')
    print(estudiante_1 .apellido)
    print(estudiante_2.university_email)
    print(vars(estudiante_1))
    print(vars(estudiante_2))
    
main()