import seaborn as sns
import matplotlib.pyplot as plt
from random import random

# Tu función para generar una Bin(n, p)
def binomial_TI(n, p):
    c = p / (1 - p)
    prob = (1 - p) ** n
    F = prob
    i = 0
    U = random()
    while U >= F:
        prob *= c * (n - i) / (i + 1)
        F += prob
        i += 1
    return i

# Parámetros de la binomial
n = 10
p = 0.3

# Simulaciones
valores = [binomial_TI(n, p) for _ in range(10000)]

# Histograma
sns.histplot(valores, discrete=True)
plt.xlabel("Cantidad de éxitos")
plt.ylabel("Frecuencia")
plt.title(f"Simulación de Bin({n}, {p}) con TI")
plt.show()
