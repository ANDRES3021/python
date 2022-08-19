#!/usr/bin/python3
"""funcion que verifica si un numero es primo"""

numero = int(input("ingrese un numero: "))

def numero_primo(numero):
    for n in range(2, numero):
        if numero % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True
    

resultado = numero_primo(numero)
print(resultado)
