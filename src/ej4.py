"""Ejercicio 2.3.4
Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada."""

def pedirNumero(n):
    """Capturamos el error si elvalor es decimal."""
    
    if n is float:
        raise ValueError("La entrada no es correcta.")
    

def main():
    n = None
    try:
        n = int(input("Introduce un número: "))
        print(pedirNumero(n))    
    except ValueError: # Capturo tanto si es 'float' como si está vacío.
        if n == None:
            print("Por favor, introduzca un número.")
        else:
            print("El número es incorrecto.")
    


if __name__ == "__main__":
    main()