"""Ejercicio 2.3.1
    Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""
def pedirEdad(edad: int) -> str:
    """Mostrar el rango de la edad introducida

    
    Args:
        edad (int): El valor introducido por el usuario.
        
    Return:
        (str): Una cadena con la serie desde el 1 hasta edad separado por guiones.
    """

    if edad < 1:
        raise ValueError("La edad es incorrecta") # Capturar valores menores a 1
    
    result = ""
    for i in range (1, edad + 1):
        if i < edad:
            result += str(i) + ", "
        else:
            result += str(edad)
            
    return result

    
def main():
    edadCorrecta = False
    edad = None
    while not edadCorrecta:
        try:
            edad = int(input("Introduce tu edad: "))
            print(pedirEdad(edad))
            edadCorrecta = True
        except ValueError: # Si el valor introducido es menor a 1
            if edad == None:
                print("Por favor, introduzca un número.")
            else:
                print("La edad es incorrecta.")


if __name__ == "__main__":
    main()