# calcular frecuencia Ni

datos = []

N = [0 for i in range(max(datos)+1)]
for i in datos:
    N[i] += 1
for i in range(len(N)):
    print(f"Frecuencia de N{i} = {N[i]}")