"""Ejercicio 2.3.4
Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada."""

def pedirNumero(n):
    """Capturamos el error si el valor es decimal.

    Args:
        n (int): valor introducido por el usuario

    Return:
        (str): ValueError: La entrada no es correcta.
    """
    
    if n is float:
        raise ValueError("La entrada no es correcta.")
    else:
        return n
    

def main():

    try:
        n = int(input("Introduce un número: "))
        print(pedirNumero(n))    
    except ValueError: # Capturo si es 'float'
        print("La entrada no es correcta.")
    


if __name__ == "__main__":
    main()