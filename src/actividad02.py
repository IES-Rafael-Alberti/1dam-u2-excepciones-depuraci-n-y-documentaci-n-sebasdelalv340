"""
Actividad 2:
    Reescribe el programa conversor de temperaturas para que lea repetidamente la temperatura hasta que sea correcta, debe detectar los fallos usando try y except."""

import pytest

def fahr2cel(fahr:float) -> float:
    ''' Convertir grados Fahrenheit a grados Celsius
    
    Args:
        fahr (float): número que vamos a transformar a celsius.
            (no puede ser inferior a -459.67)
            
    Return:
        float: valor en celsius.
    '''

    if fahr < -459.67:
        raise ValueError('Temperatura Fahrenheit incorrecta: ' + str(fahr))

    cel = (fahr - 32.0) * 5.0 / 9.0
    return cel

if __name__ == '__main__':
    numeroCorrecto = False  # Para iniciar el bucle, pero no retornar si es correcto
    fahr = None
    while not numeroCorrecto:
        try:
            ent = input('Introduzca la Temperatura Fahrenheit:')
            fahr = float(ent)
            cel = fahr2cel(fahr)
            numeroCorrecto = True
        except ValueError:   # Si no se puede convertir a float
            if fahr == None:
                print('Por favor introduzca un número.')
            else:
                print('La temperatura Fahrenheit es incorrecta: ' + str(fahr))

    print(cel)



def test_fahr2cel():
    with pytest.raises(ValueError):
        fahr2cel(-500)