#@title i
from scipy import stats
import random
import numpy as np

random.seed(42)
L = 2 * 0.001 # semiancho
cf = 0.95     # confianza
alfa = 1 - cf
# calculamos z_alpha/2 que cumple P(Z>z_alpha/2) = alpha/2
z_alfa_2 = stats.norm.ppf(1-alfa/2)
# calculamos el criterio de corte en base al semiancho y confianza
d = L / (2 * z_alfa_2)

def f(x):
  return np.sin(x) / x
# escaleo para llevar (pi,2pi)->(0,1)
def g(x):
  return f(np.pi * (1 + x)) * np.pi

############################################################################

media = g(random.random())
var, n = 0, 1
s = np.inf # desvio muestral
lista = []
while s > d:
  n += 1
  X = g(random.random())
  media_ant = media
  media = media_ant + (X - media_ant) / n
  var =  var * (1- 1 /(n-1)) + n*(media- media_ant)**2
  s = np.sqrt(var/n)
  if n in [1000,5000,7000]:
    lista.append(media)
    lista.append(s)
    lista.append((media - z_alfa_2 * s,media + z_alfa_2 * s))

lista.append(media)
lista.append(s)
lista.append((media - z_alfa_2 * s, media + z_alfa_2 * s))

print(f'Valor del corte (d) = {d},\nSimulaciones requeridas (n) = {n}')
print()
print('  #sim','|','  int  ','|','  s   ','|','  intervalo')
for i,j in zip([0,3,6,9],['  1000','  5000','  7000',n]):
  print(j,'|',f'{lista[i]:.4f}','|',f'{lista[i+1]:.4f}','|',f'({lista[i+2][0]:.4f},{lista[i+2][1]:.4f})')

#@title ii
from scipy import stats
import random
import numpy as np
random.seed(42)
L = 2 * 0.001 # semiancho
cf = 0.95     # confianza
alfa = 1 - cf
# calculamos z_alpha/2 que cumple P(Z>z_alpha/2) = alpha/2
z_alfa_2 = stats.norm.ppf(1-alfa/2)
# calculamos el criterio de corte en base al semiancho y confianza
d = L / (2 * z_alfa_2)

def f(x):
  return 3 / (3 + x**4)
# escaleo para llevar (0,infty)->(0,1)
def g(x):
  return f(1/x - 1) / x **2

############################################################################

media = g(random.random())
var, n = 0, 1
s = np.inf # desvio muestral
lista = []
while s > d:
  n += 1
  X = g(random.random())
  media_ant = media
  media = media_ant + (X - media_ant) / n
  var =  var * (1- 1 /(n-1)) + n*(media- media_ant)**2
  s = np.sqrt(var/n)
  if n in [1000,5000,7000]:
    lista.append(media)
    lista.append(s)
    lista.append((media - z_alfa_2 * s,media + z_alfa_2 * s))

lista.append(media)
lista.append(s)
lista.append((media - z_alfa_2 * s, media + z_alfa_2 * s))

print(f'Valor del corte (d) = {d},\nSimulaciones requeridas (n) = {n}')
print()
print('  #sim','|','  int  ','|','  s   ','|','  intervalo')
for i,j in zip([0,3,6,9],['  1000','  5000','  7000',n]):
  print(j,'|',f'{lista[i]:.4f}','|',f'{lista[i+1]:.4f}','|',f'({lista[i+2][0]:.4f},{lista[i+2][1]:.4f})')