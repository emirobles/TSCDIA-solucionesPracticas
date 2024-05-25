#EJERCICIO 3: Un hincha de fútbol desea conocer la cantidad de puntos que su
#equipo lleva acumulados en el campeonato, para ello recibe cada semana la
#información de la cantidad total de partidos, desde el inicio del campeonato, que
#el equipo ha perdido, ha empatado y ha ganado. Por cada partido empatado
#recibe un punto, por cada partido ganado tres puntos y por los perdidos cero
#puntos.

def calcular_puntos(partidos_ganados, partidos_empatados):
    puntos_ganados = partidos_ganados * 3
    total_puntos = puntos_ganados + partidos_empatados
    return total_puntos

def main():
    print("PUNTAJE DE EQUIPO\n")
    print("Ingrese la cantidad de partidos ganados: ")
    partidos_ganados = input()
    print("Ingrese la cantidad de partidos empatados: ")
    partidos_empatados = input()

    # Conversión directa a enteros (asumiendo que el usuario ingresa valores válidos)
    partidos_ganados = int(partidos_ganados)
    partidos_empatados = int(partidos_empatados)

    # Verificación de que los valores son no negativos
    if partidos_ganados >= 0 and partidos_empatados >= 0:
        puntos = calcular_puntos(partidos_ganados, partidos_empatados)
        print("\nEl equipo acumula un total de", puntos, "puntos en el campeonato.")
    else:
        print("\nError: La cantidad de partidos ganados y empatados debe ser mayor o igual a cero.")

if __name__ == "__main__":
    main()