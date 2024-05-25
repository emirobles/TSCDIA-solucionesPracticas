#Desarrollar en Python un módulo que gestione una agenda telefónica en un diccionario de Python utilizando los recursos ya vistos (variables, input, print, if, if - else, while, for) que consideren adecuados para cada uno de estos casos:
#Mostrar al usuario un menú de opciones
#Opción 1: Agregar una persona (apellido, nombre, dni, email y número de teléfono). Esta opción debe agregar al diccionario a la persona que el usuario ingrese
#Opción 2: Modificar una persona: dado su dni debe buscar la persona y preguntar si desea cambiar los demás campos de la persona, cambiando los que quiera.
#Opción 3: Eliminar una persona del diccionario. Elimina según el DNI
#Opción 4: Mostrar todos la agenda
#Opción 5: Salir


def mostrar_menu():
    print("\n︽︽︽︽ AGENDA TELEFÓNICA ︽︽︽︽")
    print("1. Agregar una persona")
    print("2. Modificar una persona")
    print("3. Eliminar una persona")
    print("4. Mostrar toda la agenda")
    print("5. Salir")

def agregar_persona(agenda):
    print("\nAgregar una persona:")
    apellido = input("Apellido: ")
    nombre = input("Nombre: ")
    dni = input("DNI: ")
    email = input("Email: ")
    telefono = input("Número de teléfono: ")
    agenda[dni] = {"apellido": apellido, "nombre": nombre, "email": email, "telefono": telefono}
    print("Persona agregada correctamente.")

def modificar_persona(agenda):
    dni = input("\nIngrese el DNI de la persona a modificar: ")
    if dni in agenda:
        print("\nModificar persona con DNI:", dni)
        for campo, valor in agenda[dni].items():
            nuevo_valor = input("Nuevo {} (dejar vacío para mantener el valor '{}'): ".format(campo, valor))
            if nuevo_valor:
                agenda[dni][campo] = nuevo_valor
        print("Persona modificada correctamente.")
    else:
        print("No se encontró ninguna persona con ese DNI.")

def eliminar_persona(agenda):
    dni = input("\nIngrese el DNI de la persona a eliminar: ")
    if dni in agenda:
        del agenda[dni]
        print("Persona eliminada correctamente.")
    else:
        print("No se encontró ninguna persona con ese DNI.")

def mostrar_agenda(agenda):
    print("\nAgenda telefónica:")
    for dni, datos in agenda.items():
        print("DNI:", dni)
        for campo, valor in datos.items():
            print(campo.capitalize() + ":", valor)
        print()

def main():
    agenda = {}
    while True:
        mostrar_menu()
        opcion = input("\nIngrese el número de opción que desea realizar: ")
        if opcion == "1":
            agregar_persona(agenda)
        elif opcion == "2":
            modificar_persona(agenda)
        elif opcion == "3":
            eliminar_persona(agenda)
        elif opcion == "4":
            mostrar_agenda(agenda)
        elif opcion == "5":
            print("Saliendo de la agenda telefónica. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 5.")

if __name__ == "__main__":
    main()