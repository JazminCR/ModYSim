import numpy as np

np.random.seed(42)

def est_boot_var():
    # Datos
    muestra = np.array([1, 3])
    n = len(muestra)
    cant_muestras_boot = n ** n # cantidad de muestras bootstrap

    # Lista para guardar varianzas bootstrap
    var_boot = []
    for i in range(cant_muestras_boot):
        # Generar una muestra bootstrap (con reemplazo, es decir, los nros pueden repetirse)
        sample = np.random.choice(muestra, size=n, replace=True)

        # Calcular su media muestral
        media_sample_boot = np.mean(sample)

        # Calcular su varianza muestral
        var_sample_boot = np.sum((sample - media_sample_boot)**2) / (n-1)

        # Guardar las varianza de cada muestra bootstrap
        var_boot.append(var_sample_boot)

    # Calcular el promedio de las varianzas muestrales bootstrap
    media_var_boot = np.mean(var_boot)

    var_bootstrap = np.sum((var_boot - media_var_boot)**2) / (cant_muestras_boot - 1)

    return var_bootstrap

print(f"\nEstimación bootstrap de Var(S²): {est_boot_var():.4f}")

def est_boot_var_N():
    # Datos
    muestra = np.array([5, 4, 9, 6, 21, 17, 11, 20, 7, 10, 21, 15, 13, 16, 8])
    n = len(muestra)
    cant_muestras_boot = 1000 # cantidad de muestras bootstrap

    # Lista para guardar varianzas bootstrap
    var_boot = []
    for i in range(cant_muestras_boot):
        # Generar una muestra bootstrap (con reemplazo, es decir, los nros pueden repetirse)
        sample = np.random.choice(muestra, size=n, replace=True)

        # Calcular su media muestral
        media_sample_boot = np.mean(sample)

        # Calcular su varianza muestral
        var_sample_boot = np.sum((sample - media_sample_boot)**2) / (n-1)

        # Guardar las varianza de cada muestra bootstrap
        var_boot.append(var_sample_boot)

    # Calcular el promedio de las varianzas muestrales bootstrap
    media_var_boot = np.mean(var_boot)

    var_bootstrap = np.sum((var_boot - media_var_boot)**2) / (cant_muestras_boot - 1)

    return var_bootstrap

print(f"\nEstimación bootstrap de Var(S²): {est_boot_var_N():.4f}")