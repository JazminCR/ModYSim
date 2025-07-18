import sympy as sp
from sympy import symbols, solve, Eq, exp, log
from random import random

# GENERAR X CON TI

def generarX_TI_Weibull(b, l):
    U = random()
    return l*(-log(1 - U))**(1/b)

if __name__ == "__main__":

    # CALCULAR F

    # Variables simbólicas
    x, t, b, l = sp.symbols('x t b l', real=True, positive=True)

    # Definir la densidad de Pareto: f(t) = α / t^(α + 1)
    f = (b/l) * (t/l)**(b-1) * exp(-(t/l)**b)

    F = sp.integrate(f, (t, 0, x))  # Solo calcula la integral de f desde 1 a x
    print("F(x) =", F)

    # CALCULAR LA INVERSA

    # Definir las variables
    x, u, alpha = symbols('x u alpha')

    # Función F(x)
    F = 1 - exp(-(x/l)**b)

    # Resolver la ecuación F(x) = u para despejar x
    Fx_inv = solve(Eq(F, u), x)

    # Imprimir el resultado
    print("inversa de F:" , Fx_inv)

