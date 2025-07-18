import numpy as np
from scipy import stats

def estimador_media_truncada(muestra):
    # Calcular media truncada al 10%
    media_trunc = stats.trim_mean(muestra, proportiontocut=0.1)
    '''
    La función utilizada arriba ordena la muestra de menor a mayor
    y elimina un porcentaje de datos por cada extremo
    En este caso, sería equivalente hacer:
    # Eliminar el mínimo y máximo (una sola vez cada uno)
    arr_sin_extremos = np.delete(arr, np.argmin(arr))
    arr_sin_extremos = np.delete(arr_sin_extremos, np.argmax(arr_sin_extremos))
    '''

    return media_trunc

def est_boot_var():
    # Datos
    muestra = np.array([2, 4, 6, 7, 11, 21, 81, 90, 105, 121])
    n = len(muestra)
    cant_muestras_boot = 1000 # cantidad de muestras bootstrap

    # Lista para guardar resultados muestras bootstrap
    est_boot = []
    for i in range(cant_muestras_boot):
        # Generar una muestra bootstrap (con reemplazo, es decir, los nros pueden repetirse)
        sample = np.random.choice(muestra, size=n, replace=True)

        # Replicar el estimador
        estimador_sample_boot = estimador_media_truncada(sample)

        # Guardar la replicación de cada muestra bootstrap
        est_boot.append(estimador_sample_boot)

    # Calcular la media de las replicaciones
    media_var_boot = np.mean(est_boot)

    var_bootstrap = np.sum((est_boot - media_var_boot)**2) / (cant_muestras_boot - 1)

    return var_bootstrap

print(f"\nEstimación bootstrap de Var(Ô): {est_boot_var():.4f}")