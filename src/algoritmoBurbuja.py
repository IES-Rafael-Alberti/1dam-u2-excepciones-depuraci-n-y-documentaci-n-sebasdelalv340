"""El algoritmo burbuja te permite ordenar valores de un array. Funciona revisando cada elemento con el elemanto adyacente. Si ambos elementos no están ordenados, se procede a intercambiarlos, si por el contrario los elementos ya estaban ordenados se dejan tal como estaban. Este proceso sigue para cada elemento del arreglo hasta que quede completamente ordenado."""



def ordLista(a):
    """Ordenar una lista de la que no conocemos sus elementos."""

    """
    Args:
        a (list) = lista que contiene los elementos a ordenar
        
    Return:
        Lista ordenada de menor a mayor.
    """

    """ El primer bucle (padre) nos da el número de pasadas sobre la lista.
        Mientras que el segundo bucle (hijo) nos dá el número de comparaciones por pasada.
    """

    for i in range(len(a) - 1): # 'i' es el número de pasada en el rango.
        for j in range(len(a) - 1 - i): # 'j' es el índice dentro del rango 'i'.
            if a[j] > a[j+1]: # Comparo el valor de la posición 'j' con la siguiente.
                a[j], a[j+1] = a[j+1], a[j] # Intercambio la posición si se cumple.


def main():
    a = [8, 3, 1, 19, 14]
    print(ordLista(a))
    

    
if __name__ == "__main__":
    main()



