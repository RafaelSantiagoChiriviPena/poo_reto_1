def suma_consecutivos(lista_enteros: list) -> list:

    """
    Args: lista_enteros: analiza un arreglo de numeros enteros
    Output: Crea una matriz que guarda los resultados de las sumas de datos consecutivos junto a la posicion de los mismos, organizandolo en orden descendente y retornando el primer dato de la matriz
    """
    sumas = []
    for i in range(0, len(lista_enteros)-1):
        posiciones = []
        posiciones.append(lista_enteros[i]+lista_enteros[i+1])
        posiciones.append([i, i+1])
        sumas.append(posiciones)
    sumas.sort(reverse= True)
    return sumas[0]

if __name__ == "__main__":
    try:
        len_lista : int = int(input("Digite el numero de datos para la lista de numeros: "))    # se ingresa el numero de datos para la lista
        lista = []  # se define la lista  vacia
        for i in range(0, len_lista):   # se hace un recorrido para el ingreso de datos en la lista segun el numero registrado anteriormente
            dato = int(input("Ingrese dato numerico entero para la lista: "))
            lista.append(dato)
        print(f"la lista de numeros enteros ingresados fue {lista}")    # se muestra la lista ingresada
        mayor_suma = suma_consecutivos(lista)   # se aplica la funcion sobre la lista ingresada
        print(f"La mayor suma obtenida es {mayor_suma[0]}, que se encuentra en las posiciones de lista {mayor_suma[1][0]+1} y {mayor_suma[1][1]+1}")    # se retorna la suma mayor y muestra las posiciones en la lista que corresponden a la misma
    except ValueError:
        print("El dato ingresado no es un numero entero")