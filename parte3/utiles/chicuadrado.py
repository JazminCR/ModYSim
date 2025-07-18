from scipy.stats import chi2

# CDF (fda de chi cuadrado)
# valor de t , grados de libertads
p = chi2.sf(0.86, df=2)  # sf = survival function = 1 - cdf
print(p)

# calcular el estadístico de chi cuadrado

Ni = [158, 172, 164, 181, 160, 165]
pi = [1/6 for _ in range(6)]

def pearson_test(ni, pi):
    n_sim = sum(ni)
    T = 0
    for i in range(len(Ni)):
        npi = n_sim * pi[i]
        T += ((ni[i] - npi)**2) / npi
    return T

print("El estadístico es:", pearson_test(Ni, pi))