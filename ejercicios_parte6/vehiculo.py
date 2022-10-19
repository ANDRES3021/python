"""Ejercicio de clases la clase coche hereda de la clase vehiculo"""


class Vehiculo:
    color = False
    Ruedas = 4
    Puertas = 4

class Coche(Vehiculo):
    Velocidad = 180
    Cilindrada = 4

C = Coche()
print(C.Velocidad, C.Puertas)