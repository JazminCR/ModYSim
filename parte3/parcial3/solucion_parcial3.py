from scipy.stats import chi2, norm
import numpy as np
from random import random
from math import log, exp, sqrt, comb

def ejercicio2():
    print("--------- Ejercicio 2 ----------\n")
    data = [15.22860536, 40.60145536, 33.67482894, 44.03841737, 15.69560109, 16.2321714, 25.02174735, 30.34655637, 3.3181228, 5.69447539, 10.1119561, 49.10266584, 3.6536329, 35.82047148, 3.37816632, 36.72299321, 50.67085322, 3.25476304, 20.12426236, 20.2668814, 17.49593589, 2.70768636, 14.77332745, 1.72267967, 23.34685662, 8.46376635, 9.18330789, 9.97428217, 2.33951729, 137.51657441, 9.79485269, 10.40308179, 1.57849658, 6.26959703, 4.74251574, 1.53479053, 34.74136011, 27.47600572, 9.1075566, 1.88056595, 27.59551348, 6.82283137, 12.45162807, 28.01983651, 0.36890593, 7.82520791, 3.17626161, 46.91791271, 38.08371186, 41.10961135]

    lam = 0.05

    # Calcular el estadístico
    def estadisticoD_ks(muestra, f):
        muestra.sort()
        D = 0
        n = len(muestra)
        for i in range(1, n+1):
            Fi = f(muestra[i-1])
            D = max(D, i/n - Fi, Fi - (i-1)/n)
        return D

    # Definir la función F
    def funcion_dist(x):
        return (1 - np.exp(-(0.05)*x))

    D = estadisticoD_ks(data, funcion_dist)

    print("\n--------- item b ----------\n")
    print("El valor del estadístico D es:", D)

    np.random.seed(32)

    n = len(data)  # tamaño de la muestra

    def p_valor_km_sim(Nsim, n, D):
        pvalor = 0
        for _ in range(Nsim):
            uniformes = np.random.uniform(0, 1, n)
            uniformes.sort()
            d_sim = estadisticoD_ks(uniformes, (lambda x: x))
            if d_sim >= D:
                pvalor += 1
        return pvalor/Nsim

    Nsim = 1000

    print("\n--------- item c ----------\n")
    print("El p-valor mediante simulación es:", p_valor_km_sim(Nsim, n, D))

    def rechazo(nivel, pvalor):
        if pvalor <= nivel:
            print(f"{pvalor} <= {nivel} por lo que la hipótesis nula se rechaza")
        else:
            print(f"{pvalor} > {nivel} por lo que la hipótesis nula no se rechaza")

    rechazo(0.04, p_valor_km_sim(Nsim, n, D))

    print("\n--------- item d ----------\n")

    # Defino la función de la distribución
    def exponencial(lamda):
        U = 1 - random()
        return -log(1-U) / lamda

    def p_valor_km_exp(Nsim, n, D):
        pvalor = 0
        for i in range(Nsim):
            x_gen = [exponencial(0.05) for _ in range(n)]
            x_gen.sort()
            d_exp = estadisticoD_ks(x_gen, funcion_dist)
            if d_exp >= D:
                pvalor += 1
        pvalor = pvalor / Nsim
        return pvalor

    print("El p-valor en la simulación con exponenciales es:", p_valor_km_exp(Nsim, n, D))

    rechazo(0.04, p_valor_km_exp(Nsim, n, D))


def ejercicio3():
    print("--------- Ejercicio 3 ----------\n")
    Ni = [38, 144, 342, 287, 164, 25]    # enunciado
    yi = [0, 1, 2, 3, 4, 5]   # enunciado, valores que toma la muestra
    n = sum(Ni)

    # Reconstruir la muestra completa
    muestra = np.repeat(yi, Ni)

    # la estimación de p está dada por (X_barra) / n_b
    n_b = 5
    p_hat = np.mean(muestra) / n_b

    print("\n--------- item b ----------\n")
    print("El valor estimado de p es:", p_hat)

    # Calcular pi   
    def prob_binomial(x, n, p):
        c = comb(n, x)
        return c * (p ** x) * ((1 - p) ** (n - x))

    pi = [prob_binomial(i, n_b, p_hat) for i in range(n_b + 1)]

    print("Las probabilidades pi son aprox::",pi)

    # Calcular el estadístico
    def estadisticoT_cc(pi, Ni):
        n = sum(Ni)
        T = 0
        for i in range(len(Ni)):
            npi = n*pi[i]
            T += ((Ni[i] - npi)**2) / npi
        return T

    T = estadisticoT_cc(pi, Ni)
    print(f"El estadístico T es: {T}")

    # Calcular el p-valor con la distribución chi cuadrado
    pvalor_cc = chi2.sf(T, df=(len(Ni)-1-1))
    print(f"El p-valor con aproximación chi-cuadrada es: {pvalor_cc:.7f}")

    print("\n--------- item c ----------\n")
    # Calcular el p-valor mediante simulación

    # Definir la distribución para poder generar variables
    def binomial(n_b, p):
        c = p / (1 - p)
        prob = (1 - p) ** n_b
        F = prob
        i = 0
        U = random()
        while U >= F:
            prob *= c * (n_b - i) / (i + 1)
            F += prob
            i += 1
        return i
    
    # Calcular Ni
    def frecuencias_discretas(muestra):
        N = [0 for i in range(max(muestra)+1)]
        for i in muestra:
            N[i] += 1
        return N

    def p_valor_sim(Nsim, n, T):
        pvalor = 0
        for i in range(Nsim):
            x_gen = [binomial(n_b, p_hat) for _ in range(n)]
            p_sim = np.mean(x_gen) / n_b
            pi_sim = [prob_binomial(i, n_b, p_sim) for i in range(n_b + 1)]
            Ni_sim = frecuencias_discretas(x_gen)
            t = estadisticoT_cc(pi_sim, Ni_sim)
            if t >= T:
                pvalor += 1
        pvalor = pvalor/ Nsim
        return pvalor

    Nsim = 1000
    pvalor_sim = p_valor_sim(Nsim, n, T)
    print("El p-valor con simulación es:", pvalor_sim)

    print("\n--------- item d ----------\n")
    # Determinar si la hipótesis nula se rechaza o no

    def rechazo(nivel, pvalor):
        if pvalor <= nivel:
            print(f"{pvalor} <= {nivel} por lo que la hipótesis nula se rechaza")
        else:
            print(f"{pvalor} > {nivel} por lo que la hipótesis nula no se rechaza")

    print("Para el pvalor obtenido por aprox chi cuadrada")
    rechazo(0.05, pvalor_cc)

    print("Para el pvalor obtenido por simulación")
    rechazo(0.05, pvalor_sim)


def ejercicio4():
    print("\n--------- Ejercicio 4 ----------\n")

    def f(x):
        return exp(-x) * (1 - x**4)
    
    # Escalo para llevar (2, 3) a (0, 1)
    def g(x):
        return f(2+(3-2)*x)*(3-2)

    semiancho = 0.001
    L = 2 * semiancho   # ancho
    cf = 0.95           # confianza
    alfa = 1 - cf

    # calcular z_(alpha/2) que cumple P(Z > z_(alpha/2)) = alpha/2
    z_alfa_2 = norm.ppf(1 - alfa/2)

    def media_muestral(z_alfa_2, L):
        d = L / (2 * z_alfa_2)
        mediaX = g(random())
        n = 1
        scuad = 0
        s_media = np.inf
        lista = []
        while s_media >= d:
            n += 1
            X = g(random())
            media_ant = mediaX
            mediaX = media_ant + (X - media_ant) / n
            scuad = scuad * (1 - 1/(n-1)) + n * (mediaX-media_ant)**2
            s_media = sqrt(scuad/n)
            s = sqrt(scuad)
            if n in [1000, 5000, 7000]:
               lista.append(mediaX)
               lista.append(s)
               lista.append((mediaX - z_alfa_2 * s_media, mediaX + z_alfa_2 * s_media))
        lista.append(mediaX)
        lista.append(s)
        lista.append((mediaX - z_alfa_2 * s_media, mediaX + z_alfa_2 * s_media))

        print(f'Simulaciones requeridas (n) = {n}')
        print()
        print('  # sim','|','I_barra','|','  S   ','|','  IC (95%)')
        for i,j in zip([0,3,6,9],['   1000','   5000','   7000',n]):
            print(j,'|',f'{lista[i]:.4f}','|',f'{lista[i+1]:.4f}','|',f'({lista[i+2][0]:.4f},{lista[i+2][1]:.4f})')

        return mediaX   # estimación de la integral usando Monte Carlo

    valor_integral = media_muestral(z_alfa_2, L)
    print(f'\nValor estimado de la integral = {valor_integral:.6f}')


ejercicio2()
ejercicio3()
ejercicio4()