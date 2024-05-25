#Mostrar sólo los números pares desde 0 hasta el número ingresado (input). Nota: para saber si un número es par hacer i % 2 == 0)


def mostrar_numeros_pares(numero):
    for i in range(numero + 1):
        if i % 2 == 0:
            print(i)

def main():
    print("NUMEROS PARES\n")
    numero_usuario = int(input("Ingrese un número entero: "))
    print("\nNúmeros pares desde 0 hasta", numero_usuario, ":")
    mostrar_numeros_pares(numero_usuario)

if __name__ == "__main__":
    main()