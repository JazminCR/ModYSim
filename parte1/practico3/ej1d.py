import math
import random

def generador_multiplicativo(a, M, semilla, cantidad):
    vals = [semilla]
    for _ in range(cantidad - 1):
        vals.append((a * vals[-1]) % M)
    return vals

def porcentaje_en_esfera(valores, M):
    centro = M / 2
    radio = M / 10
    radio2 = radio ** 2

    dentro = 0
    total_puntos = len(valores) // 3

    for i in range(0, len(valores) - 2, 3):
        x, y, z = valores[i:i+3]
        d2 = (x - centro) ** 2 + (y - centro) ** 2 + (z - centro) ** 2
        if d2 < radio2:
            dentro += 1

    return dentro / total_puntos

# Configuraciones
cant = 30000  # cantidad total de valores generados (múltiplo de 3)

# RANDU
a1 = 2**16 + 3
M1 = 2**31
semilla1 = random.randint(1, M1-1)
print("Semilla usada en randu:", semilla1)
valores1 = generador_multiplicativo(a1, M1, semilla1, cant)
porc1 = porcentaje_en_esfera(valores1, M1)

# Otro generador
a2 = 75
M2 = 2**31 - 1
semilla2 = random.randint(1, M2-1)
random.seed(semilla2)
print("Semilla usada en generador mult:", semilla2)
valores2 = generador_multiplicativo(a2, M2, semilla2, cant)
porc2 = porcentaje_en_esfera(valores2, M2)

print(f"RANDU estima: {porc1:.5f}")
print(f"Otro generador estima: {porc2:.5f}")
print("Valor real esperado: 0.00419")
