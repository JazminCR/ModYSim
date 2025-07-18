from random import random
from math import log, pi, sqrt, cos, sin, exp

def normal_rechazo():
    while True:
        X = -log(1 - random())
        Y = -log(1 - random())
        if Y > (X-1)**2 / 2:
            U = random()
            if U < 0.5:
                return X
            else:
                return -X
"""   
método para generar 2 normales   
def normal_polar():
    Rcuad = -log(1 - random())*2
    Theta = random()*2*pi
    X = sqrt(Rcuad)*cos(Theta)
    Y = sqrt(Rcuad)*sin(Theta)
    return X, Y
"""

# variable global para guardar el valor sobrante
sobrante = None

# forma de escribirlo para aprovechar la generación doble de normales
def normal_polar():
    global sobrante
    if sobrante is not None:
        val = sobrante
        sobrante = None
        return val
    else:
        Rcuad = -2 * log(1 - random())
        Theta = 2 * pi * random()
        X = sqrt(Rcuad) * cos(Theta)
        Y = sqrt(Rcuad) * sin(Theta)
        sobrante = Y
        return X

def normal_razon_unif():
    c = (2*pi)**(1/4)
    b = sqrt(2 / exp(1)*c**2)
    while True:
        U = random()/c
        V = (random() - 0.5)*2*b
        if V**2 < -4*U**2*log(c*U):
            return V/U
        
def media(fun, nsim):
    suma = 0
    for _ in range(nsim):
        va = fun()
        suma += va
    return suma / nsim

def varianza(fun, media, nsim):
    suma = 0
    for _ in range(nsim):
        calc = (fun() - media)**2
        suma += calc
    return suma / nsim

nsim = 10000
media_rechazo = media(normal_rechazo, nsim)
print("Media con rechazo:" , media_rechazo)
print("Varianza con rechazo:" , varianza(normal_rechazo, media_rechazo, nsim))

media_polar = media(normal_polar, nsim)
print("Media con polar:" , media_polar)
print("Varianza con polar:" , varianza(normal_polar, media_polar, nsim))

media_razon = media(normal_razon_unif, nsim)
print("Media con razon:" , media_razon)
print("Varianza con razon:" , varianza(normal_razon_unif, media_razon, nsim))