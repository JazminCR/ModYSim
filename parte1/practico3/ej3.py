import random 

def juego_acierto():
    u = random.random()
    if u < 1/3:
        w1 = random.random()
        w2 = random.random()
        x = w1 + w2
    else:
        w1 = random.random()
        w2 = random.random()
        w3 = random.random()
        x = w1 + w2 + w3
    return x

nsim = 1000
aciertos = 0

for i in range(0, nsim):
    x = juego_acierto()
    if x <= 2:
        aciertos += 1
prob = aciertos / nsim

print(prob)