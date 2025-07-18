import numpy as np
import sympy as sp
from scipy.integrate import quad
from math import exp

# Calcular integral definida
def integrand(x):
    return ( x )

resultado, error = quad(integrand, 0, 1)

print(f"Integral:{resultado}")
print(f"Error estimado:{error}")

# np.inf o -np.inf si los limites son infinitos

# CALCULAR INTEGRAL CON LIMITE X (para calcular F)

# -sp.oo usar este infinito para mejor compatibilidad, y funciones matemáticas de simpy
# Variables
x = sp.Symbol('x', real=True)
t = sp.Symbol('t', real=True)  # variable de integración

# Definís f(t)
f = 2 - t

# Definís F(x) = ∫ desde l a x f(t) dt
l = 1
F = sp.integrate(f, (t, l, x))

# Mostrás F(x)
print("F(x) =", F)