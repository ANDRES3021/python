#!/usr/bin/python3
"""funcion que verifica si un año es bisiesto"""
año = int(input("ingrese un año: "))
def año_bisiesto(año):
    if(año % 4 == 0 and año % 100 != 0):
        return True
    elif(año % 4 == 0 and año % 400 == 0):
        return True
    else:
        return False

resultado = año_bisiesto(año)
print(resultado)

