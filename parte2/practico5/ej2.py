from simular import simulate
from ej2_Erlang import Erlang_suma_exp
from ej2_Pareto import generarX_TI_Pareto
from ej2_Weibull import generarX_TI_Weibull

sim = 10000
a = 2
mu = 2
k = 2
l = 1
b = 2

_, media_pareto, _, _, _ = simulate(generarX_TI_Pareto, sim, a=a)
_, media_erlang, _, _, _ = simulate(Erlang_suma_exp, sim, k=k, mu=mu)
_, media_weibull, _, _, _ = simulate(generarX_TI_Weibull, sim, b=b, l=l)

print("Media estimada Pareto:", media_pareto)
print("Media estimada Erlang:", media_erlang)
print("Media estimada Weibull:", media_weibull)
