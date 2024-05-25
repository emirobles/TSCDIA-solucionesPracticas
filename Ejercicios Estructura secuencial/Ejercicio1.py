#EJERCICIO 1: Un estudiante está cursando 5 materias, tiene la nota de cada
#materia y quiere saber cuál es su promedio.

print("PROMEDIO DE NOTAS\n")

notas = []

for i in range(1, 6):
    nota_valida = False
    while not nota_valida:
        nota = input("Ingrese la nota de la materia " + str(i) + ": ")
        try:
            nota = float(nota)
            notas.append(nota)
            nota_valida = True
        except ValueError:
            print("Error: Por favor ingrese una nota válida.")

total_notas = sum(notas)
cantidad_materias = len(notas)
promedio = total_notas / cantidad_materias

print("\nEl promedio de notas es:", promedio)