#Pedir al usuario que ingrese 10 nombres de personas (input en un ciclo) no repetidas, guardarlos en una lista y mostrarlos. 
#Eliminar la tercer y la última persona de la lista del ejercicio 1, luego ordenar la lista y mostrarlo
#Guardar en un diccionario los datos de una persona: nombre, apellido, dni, email, fecha de nacimiento.
#En un nuevo diccionario llamado familia guardar 4 personas, cada una de ellas con los mismos 5 datos (nombre, apellido, dni, email, fecha de nacimiento)
#Guardar en una tupla los primeros n números pares. El valor de n que lo ingrese el usuario (input). Luego mostrar los datos de la tupla.

def ingresar_nombres():
    nombres = []
    for i in range(10):
        nombre = input("Ingrese el nombre de la persona {}: ".format(i + 1))
        while nombre in nombres:
            print("Este nombre ya fue ingresado. Por favor, ingrese otro nombre.")
            nombre = input("Ingrese el nombre de la persona {}: ".format(i + 1))
        nombres.append(nombre)
    return nombres

def mostrar_lista(lista):
    print("Lista de nombres:")
    for nombre in lista:
        print(nombre)

def eliminar_tercero_ultimo(lista):
    del lista[2]  # Eliminar el tercer elemento
    del lista[-1]  # Eliminar el último elemento
    lista.sort()  # Ordenar la lista
    return lista

def main():
    print("NOMBRES DE PERSONAS\n")
    # Ejercicio 1
    print("Ingrese 10 nombres de personas:")
    nombres = ingresar_nombres()
    mostrar_lista(nombres)

    # Ejercicio 2
    nombres_modificados = eliminar_tercero_ultimo(nombres[:])
    print("\nLista de nombres después de eliminar el tercer y último elemento y ordenar:")
    mostrar_lista(nombres_modificados)

    # Ejercicio 3
    persona = {
        "nombre": input("\nIngrese el nombre: "),
        "apellido": input("Ingrese el apellido: "),
        "dni": input("Ingrese el DNI: "),
        "email": input("Ingrese el email: "),
        "fecha_nacimiento": input("Ingrese la fecha de nacimiento: ")
    }
    print("\nDatos de la persona:", persona)

    # Ejercicio 4
    familia = {}
    for i in range(4):
        nombre = input("\nIngrese el nombre de la persona {}: ".format(i + 1))
        apellido = input("Ingrese el apellido de la persona {}: ".format(i + 1))
        dni = input("Ingrese el DNI de la persona {}: ".format(i + 1))
        email = input("Ingrese el email de la persona {}: ".format(i + 1))
        fecha_nacimiento = input("Ingrese la fecha de nacimiento de la persona {}: ".format(i + 1))
        familia["persona{}".format(i + 1)] = {
            "nombre": nombre,
            "apellido": apellido,
            "dni": dni,
            "email": email,
            "fecha_nacimiento": fecha_nacimiento
        }
    print("\nDatos de la familia:", familia)

    # Ejercicio 5
    n = int(input("\nIngrese un número entero para determinar la cantidad de números pares: "))
    numeros_pares = tuple(i for i in range(2, n * 2 + 1, 2))
    print("Los primeros {} números pares son:".format(n), numeros_pares)

if __name__ == "__main__":
    main()