#Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos la unidad. 
#Si el cliente compra más de 12  unidades (y hasta 24 unidades), el costo tiene un descuento 
#del 10%. Si compra más de 24 unidades, el descuento es del 15%. Además posee la promoción a 
#los jubilados. La promoción de jubilados es sumarle un 10% de descuento (si posee otros descuentos, 
#se suma los descuentos). Desarrolle una solución algorítmica para saber cuento debe pagar el cliente.

def calcular_costo_total(cantidad):
    precio_unitario = 1000  # Precio unitario de la leche de vaca entera de litro
    costo_total = cantidad * precio_unitario  # Costo total sin descuentos

    # Aplicar descuentos según la cantidad comprada
    if cantidad > 24:
        descuento = 0.15  # Descuento del 15% para más de 24 unidades
    elif cantidad > 12:
        descuento = 0.10  # Descuento del 10% para más de 12 unidades
    else:
        descuento = 0  # Sin descuento para 12 unidades o menos

    costo_descuento = costo_total * descuento  # Monto del descuento
    costo_total -= costo_descuento  # Restar el descuento al costo total

    return costo_total

def aplicar_descuento_jubilado(costo_total):
    descuento_jubilado = 0.10  # Descuento del 10% para jubilados
    costo_total_descuento_jubilado = costo_total * (1 - descuento_jubilado)  # Aplicar descuento jubilado
    return costo_total_descuento_jubilado

def main():
    print("DESPENSA\n")

    cantidad = int(input("Ingrese la cantidad de unidades de leche de vaca entera de litro compradas: "))

    costo_total = calcular_costo_total(cantidad)

    opcion_jubilado = input("¿Es jubilado? (Sí/No): ")
    if opcion_jubilado.lower() == "sí" or opcion_jubilado.lower() == "si":
        costo_total = aplicar_descuento_jubilado(costo_total)

    print("El cliente debe pagar:", costo_total, "pesos")

if __name__ == "__main__":
    main()
