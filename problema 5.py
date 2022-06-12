"""Cree una clase Alumno e inicialícela con el nombre y el número de registro. Haga los métodos
para:
1. Display - Debe mostrar toda la información del estudiante (nombre y número de
registro).
2. setAge - Debe asignar la edad al estudiante
3. setNota - Debe asignar las notas al estudiante."""

class Alumno:
    # atributos por defecto

    # atributos de inicializacion
    def __init__(self, nombre, n_registro):
        self.nombre=str(nombre)
        self.n_registro=int(n_registro)
        self.edad=[]
        self.nota=[]
    pass
    # metodos
    def display(self):
        print(f'''Nombre: {self.nombre}   Numero de registro: {self.n_registro}''')
    def setAge(self, edad):
        self.edad.append(edad)
    def setNota(self, nota):
        self.nota.append(nota)
    
alumno1=Alumno('Piero',14)
alumno1.display()
alumno1.setAge(21)
alumno1.setNota(13)
print(f'edad {alumno1.edad}')
print(f'nota {alumno1.nota}')


  