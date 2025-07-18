import numpy as np
from math import sqrt

def n_va_normal_est():
    mediaX = np.random.normal() # genera v.a normal estandar
    muestra = [mediaX]   # guardar valores generados
    n = 1
    scuad = 0
    while n < 100 or sqrt(scuad/n) >= 0.1: # condiciones dadas
        n += 1
        X = np.random.normal()  # sigue generando v.a normal
        muestra.append(X)
        media_ant = mediaX
        mediaX = media_ant + (X - media_ant) / n
        scuad = scuad * (1 - 1 /(n-1)) + n*(mediaX - media_ant)**2
    return len(muestra), mediaX, scuad, n

generados, media, varianza, cantidad = n_va_normal_est()
print("Cantidad de datos generados:", generados)
print("Media muestral de datos generados:", media)
print("Varianza muestral de datos generados:", varianza)
print("Valor n:", cantidad) # es lo mismo que la longitud de la muestra
