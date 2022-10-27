from datetime import datetime

hoy = datetime.today()
hora_salida = datetime(hoy.year, hoy.month, hoy.day, 19, 0)
diferencia =  hora_salida - hoy
if hoy >= hora_salida:
    print("Es hora de ir a casa")
    
else:
    print("este es el tiempo que te queda antes de ir a casa")
    print(diferencia)