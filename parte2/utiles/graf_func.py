import numpy as np
import matplotlib.pyplot as plt
from math import exp

# Definir la función que quieres graficar
# aca estamos usando np, no mezclar con sympy
def f(x):
    return 15*(x**2 - 2*x**3 + x**4)

# Crear un rango de valores de x (por ejemplo de -10 a 10)
x = np.linspace(0, 1, 400)

# Calcular los valores de y correspondientes a la función f(x)
y = f(x)

# Crear el gráfico
plt.plot(x, y, label='f(x) = (x - 2) / 2')

# Añadir título y etiquetas a los ejes
plt.title('Gráfico de la función f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')

# Mostrar leyenda
plt.legend()

# Mostrar el gráfico
plt.grid(True)  # Mostrar la cuadrícula
plt.show()
