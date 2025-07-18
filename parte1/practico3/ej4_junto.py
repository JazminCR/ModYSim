import numpy as np

# Cantidad de simulaciones
n = 10000

# Probabilidades de elegir cada caja
probabilidades = [0.4, 0.32, 0.28]

# Medias de las distribuciones exponenciales por caja (espera promedio)
medias = [3, 4, 5]

# Semilla para reproducibilidad, usarla si quiero repetibilidad
# np.random.seed(42)

# Simulación: elegir cajas según las probabilidades
cajas_elegidas = np.random.choice([0, 1, 2], size=n, p=probabilidades)

# Generar tiempos de espera según la media de cada caja
tiempos_espera = [np.random.exponential(scale=medias[c]) for c in cajas_elegidas]
tiempos_espera = np.array(tiempos_espera)

# Punto a: probabilidad de esperar menos de 4 minutos
p_menor_4 = np.mean(tiempos_espera < 4)
print(f"a) P(espera < 4 minutos) ≈ {p_menor_4:.3f}")

# Punto b: dado que esperó más de 4 minutos, ¿qué probabilidad hay de que haya elegido cada caja?
esperas_mayores_4 = cajas_elegidas[tiempos_espera > 4]
total_mayor_4 = len(esperas_mayores_4)

if total_mayor_4 > 0:
    prob_caja_dado_mayor_4 = [np.mean(esperas_mayores_4 == i) for i in range(3)]
else:
    prob_caja_dado_mayor_4 = [0, 0, 0]

print("b) Probabilidades condicionales dado que la espera fue mayor a 4 minutos:")
for i, prob in enumerate(prob_caja_dado_mayor_4):
    print(f"   Caja {i+1}: {prob:.3f}")
