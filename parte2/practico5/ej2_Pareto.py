
from random import random

# GENERAR X CON TI

def generarX_TI_Pareto(a):     # a > 0
    U = random()
    return (1/(1-U))**(1/a)

if __name__ == "__main__":

    import sympy as sp
    from sympy import symbols, solve, Eq, exp

    # CALCULAR F

    # Variables simbólicas
    x, t = sp.symbols('x t', real=True, positive=True)
    alpha = sp.Symbol('alpha', real=True, positive=True)

    # Definir la densidad de Pareto: f(t) = α / t^(α + 1)
    f = alpha * t ** -(alpha + 1)

    # Calcular F(x): integral de f desde 1 hasta x
    F = sp.Piecewise(
        (0, x < 1),
        (sp.integrate(f, (t, 1, x)), x >= 1)
    )

    # Mostrar la función de distribución acumulada
    sp.pprint(F, use_unicode=True)

    F = sp.integrate(f, (t, 1, x))  # Solo calcula la integral de f desde 1 a x
    print("F(x) =", F)

    # CALCULAR LA INVERSA

    # Definir las variables
    x, u, alpha = symbols('x u alpha')

    # Función F(x)
    F = 1 - 1 / x**alpha

    # Resolver la ecuación F(x) = u para despejar x
    Fx_inv = solve(Eq(F, u), x)

    # Imprimir el resultado
    print(Fx_inv)

