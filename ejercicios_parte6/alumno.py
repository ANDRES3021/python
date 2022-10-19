"""clase Alumno con metodos para inicializar sus atributos y mostrarlos por pantalla"""

class Alumno:
    Nombre: False
    Nota: False

    def nombrar(self):
        self.Nombre = input()
        self.Nota = int(input())

    def calificacion(self):
        
        if self.Nota >= 4:
            print("estudiante", self.Nombre, "aprobado")
        else:
            print("estudiante", self.Nombre, "reprobado") 
        
a = Alumno()
a.nombrar()
a.calificacion()