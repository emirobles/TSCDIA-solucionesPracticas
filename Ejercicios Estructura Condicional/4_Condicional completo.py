#4. Condicional completo (if - else) con expresión lógica compuesta (or)

print("Condicional completo - Año bisiesto\n")

año = int(input("Ingrese un año: "))

# Condicional completo con expresión lógica compuesta (or)
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("El año es bisiesto.")
else:
    print("El año no es bisiesto.")