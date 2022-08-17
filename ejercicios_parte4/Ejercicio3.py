#!/usr/bin/python3
"""imprimir los numeros de 1 a 100 en orden inverso"""
numero_inicial = 100
lista_inversos = []
while numero_inicial > 0:
    lista_inversos.append(numero_inicial)
    numero_inicial -= 1

print(lista_inversos)
