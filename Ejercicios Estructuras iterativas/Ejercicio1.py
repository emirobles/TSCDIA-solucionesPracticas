# Mostrar los números desde el 0 al número solicitado al usuario (input)

def mostrar_numeros(numero):
    for i in range(numero + 1):
        print(i)

def main():
    print("MOSTRAR NUMEROS\n")
    numero_usuario = int(input("Ingrese un número entero: "))
    print("\nNúmeros desde 0 hasta", numero_usuario, ":")
    mostrar_numeros(numero_usuario)

if __name__ == "__main__":
    main()