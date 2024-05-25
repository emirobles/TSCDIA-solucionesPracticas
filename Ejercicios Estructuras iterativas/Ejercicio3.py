#Pedir que el usuario ingrese (input) nombre de personas y mostrarlos hasta que el valor de lo que ingresa sea “fin”

def main():
    print("LISTA DE NOMBRES\n")
    nombres = []  # Lista para almacenar los nombres ingresados

    # Bucle para solicitar nombres hasta que se ingrese "fin"
    while True:
        nombre = input("Ingrese un nombre (o escriba 'fin' para terminar): ")
        if nombre.lower() == "fin":
            break  # Salir del bucle si se ingresa "fin"
        nombres.append(nombre)  # Agregar el nombre a la lista de nombres

    # Mostrar los nombres ingresados
    print("\nNombres ingresados:")
    for nombre in nombres:
        print(nombre)

if __name__ == "__main__":
    main()