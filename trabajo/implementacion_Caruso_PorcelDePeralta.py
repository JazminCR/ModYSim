import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import kstest
from time import time

# Parámetros generales
seed = 32
valor_teorico = 20 / 3
R = 100
Ns = [1000, 10_000, 100_000]
simulaciones = {
    1000: "mil",
    10000: "diez mil",
    100000: "cien mil",
}

# Generador LCG
def gen_LCG(seed):
    return (16807 * seed) % (2**31 - 1)

def gen_variables_LCG(seed, n):
    variables = []
    for _ in range(n):
        seed = gen_LCG(seed)
        variables.append(seed / (2**31 - 1))
    return variables

# Generador xorshift
def xorshift(seed):
    mask = 0xFFFFFFFFFFFFFFFF
    seed &= mask # semilla 64 bits
    seed ^= (seed << 13) & mask
    seed ^= (seed >> 7) & mask
    seed ^= (seed << 17) & mask
    return seed & mask

def gen_variables_xorshift(seed, n):
    variables = []
    max_64bit = 0xFFFFFFFFFFFFFFFF
    for _ in range(n):
        seed = xorshift(seed)
        variables.append(seed / max_64bit)
    return variables

# Generador MT19937 (numpy)
def gen_variables_MT19937(seed, n):
    rng = np.random.Generator(np.random.MT19937(seed))
    return rng.random(size=n)

# Función a integrar
def g(u1, u2, u3, u4, u5):
    return (u1 + u2 + u3 + u4 + u5) ** 2

# Estimación Monte Carlo
def MonteCarlo(g, Nsim, generator, seed):
    integral = 0
    vars = generator(seed, Nsim*5) # vector de variables aleatorias
    subarrays = [vars[i:i+5] for i in range(0, len(vars), 5)]
    for sub in subarrays:
        integral += g(*sub)
    return integral / Nsim

# Métricas: ECM, varianza, tiempo, eficiencia
def estimar_ECM_var_tiempo_efic(g, Nsim, generator, seed, valor_teorico, R):
    start = time()
    estimaciones = []
    for r in range(R):
    # repetir Monte Carlo R veces
        resultado = MonteCarlo(g, Nsim, generator, seed + r) # cambiar semilla en cada repetición
        estimaciones.append(resultado)
    tiempo = (time() - start) / R
    media = sum(estimaciones) / R
    errores = [(x - valor_teorico)**2 for x in estimaciones]
    ECM = sum(errores) / R
    varianza = sum((x - media)**2 for x in estimaciones) / (R - 1)
    eficiencia = 1 / (varianza * tiempo)
    return ECM, varianza, tiempo, eficiencia, estimaciones

generadores = {
    "LCG": gen_variables_LCG,
    "XORShift": gen_variables_xorshift,
    "MT19937": gen_variables_MT19937
}

medias = {nombre: [] for nombre in generadores}
estimaciones_gen = {nombre: [] for nombre in generadores}
varianzas = {nombre: [] for nombre in generadores}

# Test de bondad de ajuste para distribuciones
def kolmogorov_smirnov(data, nombre, nivel):
    med = np.mean(data)
    desv = np.std(data, ddof=1)
    p_ks = kstest(data, 'norm', args=(med, desv)).pvalue
    print(f"\tH0 = Las estimaciones generadas por montecarlo tienen distribucion Normal ({med}, {desv})")
    print(f"\t\tTest KS para {nombre}: p-valor = {p_ks:.5f}")
    if p_ks <= nivel:
        print(f"\t\tp = {p_ks:.5f} <= {nivel} por lo que se rechaza la hipótesis nula")
    else:
        print(f"\t\tp = {p_ks:.5f} > {nivel} por lo que no se rechaza la hipótesis nula")

# Test de bondad de ajuste para aleatoriedad de generadores
def kolmogorov_smirnov_aleatoriedad(data, nombre, nivel):
        p_ks = kstest(data, 'uniform').pvalue
        print("\tH0 = Los datos generados por el generador siguen una distribucion Uniforme [0,1)")
        print(f"\t\tTest KS para {nombre}: p-value = {p_ks:.5f}")
        if p_ks <= nivel:
            print(f"\t\tp = {p_ks:.5f} <= {nivel} por lo que la hipótesis nula se rechaza")
        else:
            print(f"\t\tp = {p_ks:.5f} > {nivel} por lo que la hipótesis nula no se rechaza")

# Ejecución principal
for N in Ns:
    texto = simulaciones.get(N, str(N))
    print(f"\033[4mCantidad de simulaciones: {N} ({texto})\033[0m")
    print()
    for nombre, generador in generadores.items():
        resultado = MonteCarlo(g, N, generador, seed)
        medias[nombre].append(resultado)

        ECM, varianza, tiempo, eficiencia, estimaciones = estimar_ECM_var_tiempo_efic(
            g, N, generador, seed, valor_teorico, R
        )
        estimaciones_gen[nombre].append(estimaciones)
        varianzas[nombre].append(varianza)

        datos = generador(seed, N)

        print(f"{nombre}: Integral = {resultado:.5f}, ECM = {ECM:.10f}, Varianza = {varianza:.10f}, Tiempo = {tiempo:.5f} seg, Eficiencia = {eficiencia:.5f}")
        kolmogorov_smirnov(estimaciones, nombre, 0.05)
        kolmogorov_smirnov_aleatoriedad(datos, nombre, 0.05)
        print()
        print()

# Funciones gráficas para testear y comparar
def graficar_kdes_por_generador(estimaciones_gen, nombre_generador, Ns):
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    for i, N in enumerate(Ns):
        ax = axes[i]
        estimaciones = estimaciones_gen[nombre_generador][i]
        sns.histplot(estimaciones, bins=42, color='skyblue', stat="density", alpha=0.6, ax=ax)
        sns.kdeplot(estimaciones, color='purple', ax=ax)
        ax.set_title(f'N = {N}')
        ax.set_xlabel('Estimación integral')
        ax.set_ylabel('Densidad')
    fig.suptitle(f'Distribuciones para {nombre_generador}', fontsize=16)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()


def graficar_convergencia(Ns, medias, valor_teorico):
    plt.figure(figsize=(10, 5))
    plt.plot(Ns, medias["LCG"], label="LCG", marker='o')
    plt.plot(Ns, medias["XORShift"], label="XORShift", marker='o')
    plt.plot(Ns, medias["MT19937"], label="MT19937", marker='o')
    plt.axhline(valor_teorico, color='red', linestyle='--', label='Valor teórico')
    plt.xscale('log')
    plt.title('Convergencia de la media estimada')
    plt.xlabel('Cantidad de simulaciones (N)')
    plt.ylabel('Media estimada')
    plt.legend(loc='lower right')
    plt.grid(True)
    plt.show()

def graficar_varianza(Ns, varianzas):
    plt.figure(figsize=(10, 5))
    plt.plot(Ns, varianzas["LCG"], label="LCG", marker='o')
    plt.plot(Ns, varianzas["XORShift"], label="XORShift", marker='o')
    plt.plot(Ns, varianzas["MT19937"], label="MT19937", marker='o')
    plt.xscale('log')
    plt.yscale('log')
    plt.title('Disminución de la varianza estimada')
    plt.xlabel('Cantidad de simulaciones (N)')
    plt.ylabel('Varianza')
    plt.legend(loc='upper right')
    plt.grid(True, which="both", ls="--", linewidth=0.5)
    plt.show()

def graficar_boxplot(estimaciones_gen, valor_teorico):
    valores = (
        [x for sublist in estimaciones_gen["LCG"] for x in sublist] +
        [x for sublist in estimaciones_gen["XORShift"] for x in sublist] +
        [x for sublist in estimaciones_gen["MT19937"] for x in sublist]
    )
    labels = (
        ["LCG"] * sum(len(sublist) for sublist in estimaciones_gen["LCG"]) +
        ["XORShift"] * sum(len(sublist) for sublist in estimaciones_gen["XORShift"]) +
        ["MT19937"] * sum(len(sublist) for sublist in estimaciones_gen["MT19937"])
    )
    palette = {
        "LCG": "#1f77b4",
        "XORShift": "#ff7f0e",
        "MT19937": "#2ca02c"
    }
    sns.boxplot(x=labels, y=valores, hue=labels, palette=palette, legend=False)
    plt.title("Variabilidad de las estimaciones por generador")
    plt.xlabel("Generador")
    plt.ylabel("Estimación de la integral")
    plt.axhline(y=valor_teorico, color='red', linestyle='--', label='Valor teórico')
    plt.legend()
    plt.show()

graficar_kdes_por_generador(estimaciones_gen, "LCG", Ns)
graficar_kdes_por_generador(estimaciones_gen, "XORShift", Ns)
graficar_kdes_por_generador(estimaciones_gen, "MT19937", Ns)
graficar_convergencia(Ns, medias, valor_teorico)
graficar_varianza(Ns, varianzas)
graficar_boxplot(estimaciones_gen, valor_teorico)
