#!/usr/bin/python3
"""ejercicio para imprimir los numeros impares"""
numero_inicial = 0
lista_impares = []
while numero_inicial < 10:
    if (numero_inicial % 2 != 0):
        lista_impares.append(numero_inicial)
    numero_inicial += 1

print(lista_impares)
