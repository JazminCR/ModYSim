
def generador_von_neumann(x):
    contador = 1
    lista_generada = [x]
    lista_u = [x / 10000]  # u0 = y0 / 10000

    for i in range(10000):
        x = (x**2 // 100) % 10000  # extrae las 4 cifras
        if x in lista_generada:
            break
        lista_generada.append(x)
        lista_u.append(x / 10000)
        contador += 1

    print("Valores generados (yᵢ):", lista_generada)
    print("Valores uᵢ = yᵢ / 10⁴:", lista_u)
    print(f"Período del generador: {contador}")
    return contador

generador_von_neumann(3009)
print("------------------------")
generador_von_neumann(7600)
print("------------------------")
generador_von_neumann(1234)
print("------------------------")
generador_von_neumann(4321)
