"""Ejercicio 2.3.5
Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje, "Incorrect Password!!"
"""

def pedirContraseña(contrase, contra):
    """Capturamos el error si la contraseña introducida no coincide con la guardada.

    Args:
        contra (str): cadena guardada
        contrase (str): cadena introducida por el usuario

    Return:
        (str): ValueError: Incorrect Password

        (str): Correct Password
    """
     
    if contrase != contra: # La contraseña debe ser idéntica. Tenemos enc uenta las mayúsculas.
        raise NameError("**Error** La contraseña es incorrecta.")
    else:
        return "Correct Password"


def main():
    try:
        contra = "Pepitodelospalotes"
        contrase = input("Introduzca la contraseña: ")
        print(pedirContraseña(contrase, contra))
    except NameError:
        print("Incorrect Password")

if __name__ == "__main__":
    main()