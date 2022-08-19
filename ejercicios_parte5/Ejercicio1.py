#!/usr/bin/python3
from math import pi

"""funciones para calcular area de triangulo  y circulo"""

altura = float(input("ingrese la altura: "))
base = float(input("ingrese la base del triangulo: "))
radio_circulo = float(input("ingrese el radio del circulo: "))

def area_triangulo(altura, base):
    Area = (base * altura)/(2) 
    return Area

def area_circulo(radio_circulo):
    Area = round((pi * (radio_circulo**2)),2)
    return Area


triangulo = area_triangulo(altura, base)
print(triangulo)

circulo = area_circulo(radio_circulo)
print(circulo)
