from random import random
import numpy as np

def valorPi(NSim):
    enCirculo = 0
    for _ in range(NSim):
        u = 2 * random() - 1
        v = 2 * random() - 1
        if u**2 + v**2 <= 1:
            enCirculo += 1
    return 4 * enCirculo / NSim

for N in [1000, 10000, 100000]:
    print(valorPi(1000))

print(np.pi)