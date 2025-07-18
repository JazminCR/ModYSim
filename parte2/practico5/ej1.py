from random import random
from math import sqrt, log

def generarX_TI_eja():
    U = random()
    if U < 0.25:
        return 2*sqrt(U) + 2
    else:
        return -2*sqrt(3 - 3*U) + 6
    
print("X gen eja:" , generarX_TI_eja()) # para chequear que los valores caigan dentro de 0, 6

def generarX_TI_ejb():
    U = random()
    if U < 0.6:
        return sqrt(105*U+81)/3 - 3
    else:
        return (35*U/2 - 9.5)**(1/3)
    
print("X gen ejb:" , generarX_TI_ejb())

def generarX_TI_ejc():
    U = random()
    if U < 0.0625:
        return log(16*U)/4
    else:
        return 4*U - 1/4
    
print("X gen ejc:" , generarX_TI_ejc())
