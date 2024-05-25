#En una escuela, luego de tomar un determinado examen, es necesario calcular el promedio de notas (las notas van de 0 a 10) de los alumnos de un curso. Se necesita saber si el rendimiento ha sido elevado (el promedio es mayor a 8), aceptable (el promedio está comprendido entre 6 y 8) o bajo (promedio es inferior a 6). Desarrollar un algoritmo que resuelva este problema. Para tener en cuenta: las autoridades del colegio saben cuántos estudiantes del curso han rendido el examen.

def calcular_promedio(notas):
    total_notas = sum(notas)
    cantidad_alumnos = len(notas)
    promedio = total_notas / cantidad_alumnos
    return promedio

def clasificar_rendimiento(promedio):
    if promedio > 8:
        return "elevado"
    elif 6 <= promedio <= 8:
        return "aceptable"
    else:
        return "bajo"

def main():
    print("PROMEDIO DE NOTAS\n")
    cantidad_alumnos = int(input("Ingrese la cantidad de alumnos del curso: "))
    notas = []

    # Solicitar las notas de cada alumno
    for i in range(cantidad_alumnos):
        nota = float(input("Ingrese la nota del alumno {}: ".format(i + 1)))
        notas.append(nota)

    # Calcular el promedio de notas
    promedio_notas = calcular_promedio(notas)

    # Clasificar el rendimiento
    rendimiento = clasificar_rendimiento(promedio_notas)

    # Mostrar resultados
    print("\nEl promedio de notas del curso es:", promedio_notas)
    print("El rendimiento del curso es:", rendimiento)

if __name__ == "__main__":
    main()