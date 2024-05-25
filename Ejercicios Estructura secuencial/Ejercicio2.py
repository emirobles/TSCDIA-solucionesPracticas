#EJERCICIO 2: Un pintor de casas debe hacer un presupuesto para un cliente. Lo
#que cobra se calcula de acuerdo a los metros cuadrados que debe pintar. El
#cliente le indica que necesita conocer el costo de mano de obra para pintar una
#pared rectangular de un galpón. El pintor cobra un monto ﬁjo por cada metro
#cuadrado. Puedes hacer un algoritmo para calcular el costo de mano de obra para
#pintar la pared.

def calcular_costo_mano_obra(area_pared, costo_por_metro_cuadrado):
    costo_total = area_pared * costo_por_metro_cuadrado
    return costo_total

def main():
    print("PRESUPUESTO CLIENTE\n")

    # Entrada de datos
    print("Ingrese el área de la pared a pintar en metros cuadrados: ")
    area_pared = input()
    print("Ingrese el costo por metro cuadrado de pintura: ")
    costo_por_metro_cuadrado = input()

    # Conversión de datos
    area_pared = float(area_pared)
    costo_por_metro_cuadrado = float(costo_por_metro_cuadrado)

    # Verificación si los valores son positivos
    if area_pared > 0 and costo_por_metro_cuadrado > 0:
        costo_mano_obra = calcular_costo_mano_obra(area_pared, costo_por_metro_cuadrado)
        print("El costo de mano de obra para pintar la pared es: $", round(costo_mano_obra, 2))
    else:
        print("Error: El área de la pared y el costo por metro cuadrado deben ser valores positivos.")

if __name__ == "__main__":
    main()