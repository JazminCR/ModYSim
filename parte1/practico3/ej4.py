import numpy as np

def simular_prob_espera_menor_4(n_values):
    resultados = []

    # Datos del enunciado
    cajas = [0, 1, 2]
    probs = [0.4, 0.32, 0.28]  # Probabilidades de elegir cada caja
    medias = [3, 4, 5]         # Medias de las exponenciales
    lambdas = [1/m for m in medias]  # Lambdas = 1/media

    for n in n_values:
        # Elegimos qué caja elige cada cliente
        # Elige aleatoriamente n elementos del array cajas, respetando las probabilidades dadas en probs
        cajas_elegidas = np.random.choice(cajas, size=n, p=probs)

        # Simulamos los tiempos de espera según la caja que eligieron
        tiempos = np.array([
            np.random.exponential(scale=1/lambdas[c]) for c in cajas_elegidas
            # np.random.exponential(scale=medias[c]) for c in cajas_elegidas es lo mismo, le pasa directamente la media
            # Para cada cliente, según qué caja eligió (c), se le asigna un tiempo de espera exponencial con la media correspondiente a esa caja.
        ])

        # Calculamos la proporción de clientes que esperaron menos de 4 minutos
        prob_menor_4 = np.mean(tiempos < 4)
        # mean calcula el promedio de cuántos valores cumplen una condición
        # por ej → [True, False, True, False] → [1, 0, 1, 0] → 0.5
        resultados.append(prob_menor_4)

    return resultados

n_simulaciones = [100, 1000, 10000, 100000]
probs_estimadas = simular_prob_espera_menor_4(n_simulaciones)

for n, p in zip(n_simulaciones, probs_estimadas):
    print(f"Simulaciones: {n:>7}  -->  P(t ≤ 4) ≈ {p:.4f}")



def prob_caja_dado_espera_mayor_4(n=10000):
    cajas = [0, 1, 2]
    probs = [0.4, 0.32, 0.28]
    medias = [3, 4, 5]
    lambdas = [1/m for m in medias]

    # Simular elecciones de cajas
    cajas_elegidas = np.random.choice(cajas, size=n, p=probs)

    # Simular tiempos de espera según caja
    tiempos = np.array([
        np.random.exponential(scale=1/lambdas[c]) for c in cajas_elegidas
    ])

    # Filtrar los que esperaron más de 4 minutos
    indices_mayor_4 = tiempos > 4
    cajas_filtradas = np.array(cajas_elegidas)[indices_mayor_4]

    # Calcular proporciones
    total = len(cajas_filtradas)
    prob_caja_0 = np.sum(cajas_filtradas == 0) / total
    prob_caja_1 = np.sum(cajas_filtradas == 1) / total
    prob_caja_2 = np.sum(cajas_filtradas == 2) / total

    return prob_caja_0, prob_caja_1, prob_caja_2


p0, p1, p2 = prob_caja_dado_espera_mayor_4(n=10000)
print(f"P(caja 1 | espera > 4): {p0:.3f}")
print(f"P(caja 2 | espera > 4): {p1:.3f}")
print(f"P(caja 3 | espera > 4): {p2:.3f}")



