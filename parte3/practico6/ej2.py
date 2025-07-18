from random import random
# random() genera un nro aleatorio entre 0 y 1, o sea U ~ U(0, 1)
from math import exp, sqrt, tan, pi, cos
import numpy as np

def g(u):
    return exp(u) / sqrt(2*u)

# scuad representa a s**2 --> estimador de var de la media
# s representa al estimador del desvío de la media
def media_muestral():
    mediaX = g(random())
    n = 1
    scuad = 0
    s = np.inf  # desvío muestral
    # para que el ciclo pare, ambas condiciones deben ser falsas
    while n < 100 or s >= 0.01:
        n += 1
        X = g(random())
        media_ant = mediaX
        mediaX = media_ant + (X - media_ant) / n
        scuad = scuad * (1 - 1/(n-1)) + n * (mediaX-media_ant)**2
        s = sqrt(scuad/n)

    return mediaX   # estimación de la integral usando Monte Carlo

valor_integral = media_muestral()
print(f'Valor estimado de la integral = {valor_integral:.6f}')

# ------------------  ITEM ii  ------------------------------------------------------------------

def g_ii(x):  # Función a integrar
    return x**2 * exp(-x**2)

def h(u):  # Cambio de variable con diferencial
    # x = tan(pi * (u - 0.5)) transforma u in [0,1] a x in (-inf, inf)
    x = tan(pi * (u - 0.5))
    # Derivada del cambio de variable: dx/du = pi * sec^2(pi*(u - 0.5))
    return g_ii(x) * pi / (cos(pi * (u - 0.5)))**2

# scuad representa a s**2 --> estimador de var muestral
# s representa al estimador del desvío muestral
def media_muestral_ii():
    mediaX = h(random())
    n = 1
    scuad = 0
    s = np.inf  # desvío muestral
    # para que el ciclo pare, ambas condiciones deben ser falsas
    while n < 100 or s >= 0.01:
        n += 1
        X = h(random())
        media_ant = mediaX
        mediaX = media_ant + (X - media_ant) / n    # media muestral
        scuad = scuad * (1 - 1/(n-1)) + n * (mediaX-media_ant)**2   # varianza muestral
        s = sqrt(scuad) # desvío estándar muestral

    return mediaX   # estimación de la integral usando Monte Carlo

valor_integral_ii = media_muestral_ii()
print(f'Valor estimado de la integral = {valor_integral_ii:.6f}')