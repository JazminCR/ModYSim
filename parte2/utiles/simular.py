import numpy as np

def simulate(X,n_sim,ddof=0,**kwargs):
    s = np.empty(n_sim)
    for i in range(n_sim):
      s[i]=X(**kwargs)
    mean_sim = np.mean(s)
    median_sim = np.median(s)
    var_sim = np.var(s,ddof=ddof)
    std_sim = np.std(s,ddof=ddof)
    return s,mean_sim,median_sim,var_sim,std_sim

# devuelve el array s con todas las simulaciones
# media: valor esperado
# mediana: valor del medio
# varianza: cuánto se dispersan los datos respecto a la media
# desvío: raíz cuadrada de la varianza

"""
ejemplo de uso:

def generarX_TI_Weibull(b, l):
    return l * (-log(random()))**(1/b)

simulate(generarX_TI_Weibull, n_sim=10000, b=2, l=1)
"""