import numpy as np
from scipy.integrate import quad

def integrand(x):
    return ( (x + x**(1/2))**(1/2) )

resultado, error = quad(integrand, 1, 7)

print(f"Integral:{resultado}")
print(f"Error estimado:{error}")