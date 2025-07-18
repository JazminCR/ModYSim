from random import randint

def jugar():
    primer_dado = randint(1, 6)

    if primer_dado == 1 or primer_dado == 6:
        # Tira un solo dado y duplica
        segundo_dado = randint(1, 6)
        puntaje = 2 * segundo_dado
    else:
        # Tira dos dados y suma
        dado1 = randint(1, 6)
        dado2 = randint(1, 6)
        puntaje = dado1 + dado2

    return puntaje > 6

# Simulación
N = 1000
ganadas = sum(jugar() for _ in range(N))
# cuenta cuantas veces se gana de N partidas
estimacion = ganadas / N

print(f"Estimación P(ganar): {estimacion}")


#Otra forma
#
#def juego_ej_8(Nsim):
#    vict = 0
#    for i in range (Nsim):
#        dado = random.randint(1, 6)
#        if dado == 6 or dado == 1:
#            result = 2 * random.randint(1, 6)
#        else:
#            result = random.randint(1, 6) + random.randint(1, 6)
#        if result > 6:
#            vict += 1
#    return vict/Nsim