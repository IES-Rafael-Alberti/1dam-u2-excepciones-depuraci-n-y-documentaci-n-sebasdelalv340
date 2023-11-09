"""Ejercicio 2.3.3
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir uno correcto."""

def pedirNumero(n):
    if n < 1:
        raise Exception("**Error** Introduzca un número positivo:")



def cuentaRegresiva(n):

    for i in range(n, -1, -1):
        if i == 0:
            print(i)
        else:
            print(i, end= ", ")


def main():
    nCorrecto = False
    n = None
    while not nCorrecto:
        try:
            n = int(input("Introduce un número: "))
            print(pedirNumero(n))
            print(cuentaRegresiva(n))
            nCorrecto = True
        except Exception:
            if n == None:
                print("Por favor, introduce un número")
    


if __name__ == "__main__":
    main()