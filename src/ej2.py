"""Ejercicio 2.3.2
    Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas."""


def numerosImpares(n: int) -> str:
    """Obtener una serie de números impares


    Args:
        n (int): valor introducido por el usuario

    Return:
        (str): Cadena separada por comas hasta 'n'
    """
    
    if n < 1:
        raise ValueError("El número es incorrecto") # Capturo los números inferiores a 1

    result = ""

    for i in range (1, n +1):
        if i % 2 == 0 and i == n: # Si el bucle llega a 'n' termina
            result = result[:-2]
        elif i % 2 != 0 and i == n:
            result += str(n)
        elif i % 2 != 0: # Si el resto es distinto de 0 (impar), lo imprime
            result += str(i) + ", "

    return result
       


def main():
    nCorrecto = False
    n = None
    while not nCorrecto: # Mientras 'n' no sea un número válido no cambiará a True.
        try:
            n = int(input("Introduce un número: "))
            print(numerosImpares(n))
            nCorrecto = True
        except ValueError: # Capturo tanto si el valor es menor a 1 o está vacío.
            if n == None:
                print("Por favor, introduzca un número.")
            else:
                print("El número es incorrecto.")
    

if __name__ == "__main__":
    main()