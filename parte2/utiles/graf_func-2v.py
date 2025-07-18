import numpy as np
import matplotlib.pyplot as plt

def f(x, n):
    return n * x**(n - 1)

# Valores de x en [0,1] excluyendo el 0 (por posibles problemas de derivadas si n < 1)
x = np.linspace(0.001, 1, 500)

# Elegí valores de n para comparar
valores_n = [1, 2, 3, 5, 10]

# Graficar
plt.figure(figsize=(8, 5))
for n in valores_n:
    plt.plot(x, f(x, n), label=f'n = {n}')

plt.title('Funciones f(x) = n * x^{n-1}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
