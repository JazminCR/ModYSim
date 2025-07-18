import numpy as np
from random import random
from scipy import stats
from math import sqrt

def N():
    suma = 0
    n = 0
    while suma < 1:
        X = random() # genera uniforme en 0,1
        suma += X
        n += 1
    return n

'''
La esperanza de N es conocida y cumple que 
E[N] = e = 2.718

Este experimento es clásico y tiene como resultado que se necesitan 
e variables uniformes en (0, 1) para que su suma supere 1

La esperanza se estima con la media muestral cuando se hacen suficientes simulaciones
'''

def media_muestral(Nsim):
    mediaX = 0
    scuad = 0
    for n in range(2, Nsim+2):
        X = N()
        media_ant = mediaX
        mediaX = media_ant + (X - media_ant) / n
        scuad = scuad * (1 - 1/(n-1)) + n * (mediaX - media_ant)**2
    return mediaX, scuad

Nsim = 1000
esperanza, varianza = media_muestral(Nsim)
print("La esperanza (media muestral) de N es:", esperanza)
print("La varianza muestral de la media es:", varianza/Nsim)

###################################################################################################

L = 0.025   # ancho
cf = 0.95   # confianza
alfa = 1 - cf

# calcular z_(alpha/2) que cumple P(Z > z_(alpha/2)) = alpha/2
z_alfa_2 = stats.norm.ppf(1 - alfa/2)

def media_muestral_intervalo(z_alfa_2, L):
    d = L / (2 * z_alfa_2)
    media = N()
    n = 1
    scuad = 0
    while n <= 100 or sqrt(scuad / n) > d:
        n += 1
        X = N()
        media_ant = media
        media = media_ant + (X - media_ant) / n
        scuad = scuad * (1 - 1 / (n - 1)) + n * (media - media_ant) ** 2
    return media, media - z_alfa_2 * sqrt(scuad/n), media + z_alfa_2 * sqrt(scuad/n)
# devuelve los extremos del intervalo

media_ic , a, b = media_muestral_intervalo(z_alfa_2, L)
print("Estimación de e mediante IC de 95%:", media_ic)
print("Intervalo:", (float(a), float(b)))
