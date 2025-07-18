import math

def mcm(a, b):
    return abs(a*b) // math.gcd(a, b)

#print(mcm(32, 30))

def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#print(mcd(3, 512))

def coprimos(n):
    """Devuelve una lista de enteros entre 1 y n-1 que sean coprimos con n."""
    return [i for i in range(1, n) if mcd(i, n) == 1]

#print(f"Números coprimos: {coprimos(32)}")

def factores_primos(n):
    factores = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            factores.add(d)
            n //= d
        d += 1
    if n > 1:
        factores.add(n)
    return factores

def es_raiz_primitiva(a, p):
    if mcd(a, p) != 1:
        return False
    phi = p - 1
    factores = factores_primos(phi)
    for q in factores:
        if pow(a, phi // q, p) == 1:
            return False
    return True

def buscar_raices_primitivas(p):
    """
    Devuelve la lista de raíces primitivas módulo p.
    Requiere que p sea un número primo.
    """
    raices = []
    for a in range(1, p):
        if es_raiz_primitiva(a, p):
            raices.append(a)
    return raices

#print(buscar_raices_primitivas(71))

def tiene_periodo_maximo_genMixto(a, c, M):
    # 1. Verifica que c y M sean coprimos
    if mcd(c, M) != 1:
        return False

    # 2. Verifica que (a - 1) sea divisible por todos los factores primos de M
    factores = factores_primos(M)
    for p in factores:
        if (a - 1) % p != 0:
            return False

    # 3. Si M es divisible por 4, entonces (a - 1) debe ser múltiplo de 4
    if M % 4 == 0 and (a - 1) % 4 != 0:
        return False

    return True

#print(tiene_periodo_maximo_genMixto(123, 3, 512))

def es_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def tiene_periodo_maximo_genMult(a, M):
    if not es_primo(M):
        return False  # Solo se considera periodo máximo cuando M es primo
    return es_raiz_primitiva(a, M)

#print(tiene_periodo_maximo_genMult(7, 71))
