"""Ejercicio 2.3.5
Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje, "Incorrect Password!!"
"""

def pedirContraseña(contrase, contra):
    if contrase != contra:
        raise NameError("**Error** La contraseña es incorrecta.")


def main():
    try:
        contra = "Pepitodelospalotes"
        contrase = input("Introduzca la contraseña: ")
        print(pedirContraseña(contrase, contra))
    except NameError:
        print("Incorrect Password")

if __name__ == "__main__":
    main()