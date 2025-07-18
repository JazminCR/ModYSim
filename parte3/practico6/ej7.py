import numpy as np

np.random.seed(42)

# Datos
muestra = np.array([56, 101, 78, 67, 93, 87, 64, 72, 80, 69])
n = len(muestra)
a, b = -5, 5
cant_muestras_boot = 10_000  # cantidad de muestras bootstrap

# Paso 1: calcular X̄ (media muestral)
mediaX = np.mean(muestra)   # se usa para estimar mu

# Paso 2: generar muestras bootstrap y sus medias
contador = 0
for i in range(cant_muestras_boot):
    # Generar una muestra bootstrap (con reemplazo, es decir, los nros pueden repetirse)
    sample = np.random.choice(muestra, size=n, replace=True)
    
    # Calcular su media
    media_sample = np.mean(sample)

    # Ver si la muestra generada cumple la condición
    if np.abs(media_sample - mediaX) < 5:
       contador += 1

# Paso 3: estimar la proporción de veces que cae entre a y b
proporcion = contador / cant_muestras_boot

print(f"Estimación de p: {proporcion:.4f}")
