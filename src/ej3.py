"""Ejercicio 2.3.3
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir uno correcto."""

def pedirNumero(n: int) -> str:
    """ Pedir un número entero positivo.
    
        Args:
            n (int): Valor introducido por el usuario
            
        Retuns:
            (str): El número es incorrecto
    """
    
    if n < 1:
        raise Exception("**Error** Introduzca un número positivo:")


def cuentaRegresiva(n: int) -> str:
    """Realiza una cuenta regresiva desde el número introducido
    
        Args:
            n (int): Valor introducido por el usuario
            
        Returns:
            (str): Cadena de la cuenta regresiva
    """

    result = ""
    for i in reversed(range(n + 1)): # Invierte el rango
        if i == 0:
             result += str(i)
        else:
            result += str(i) + ", "

    return result
        
            
 
def main():
    nCorrecto = False
    n = None
    while not nCorrecto:
        try:
            n = int(input("Introduce un número: "))
            pedirNumero(n)
            print(cuentaRegresiva(n))
            nCorrecto = True   
        except Exception:
            if n == None:
                print("Introduce un número: ")
            else:
                print("El número es incorrecto.")
        
    


if __name__ == "__main__":
    main()