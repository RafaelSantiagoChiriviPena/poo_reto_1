def lista_primos(lista: list) -> list:

    """
    Args: lista: recibe un arreglo de numeros enteros sobre los cuales aplicar la funcion deteccion_primos
    Output: Si se detecta que un numero es primo, es añadido a una lista de primos, misma la cual es el retorno de la funcion
    """
    list_primos = []
    for i in range(0, len(lista)):
        if deteccion_primos(lista[i]) == True:
            list_primos.append(lista[i])
    return list_primos

def deteccion_primos(dato: int) -> bool:
    
    """
    Args: dato: toma un numero entero sobre el cual obtener sus divisores para determinar si es primo
    Output: se añaden 1's o 0's a una lista vacia segun si se obtiene residuo 0 en divisiones desde 1 hasta el dato obtenido, para luego contar el numero de 1's y determinar si es primo o no, retornando un booleano
    """
    divisores = []
    for i in range(1, dato+1):
        if dato%i == 0:
            divisores.append(1)
        if dato%i != 0:
            divisores.append(0)
    if divisores.count(1) == 2:
        return True
    if divisores.count(1) != 2:
        return False

if __name__ == "__main__":
    try:
        len_lista : int = int(input("Digite el numero de datos para la lista de numeros: "))    # se define el numero de datos para la lista
        lista = []  # se define la lista vacia
        for i in range(0, len_lista):   # se hace un recorrido para el ingreso de datos en la lista segun el numero registrado anteriormente
            dato = int(input("Ingrese dato numerico entero para la lista: "))
            lista.append(dato)
        print(f"la lista de numeros enteros ingresados fue {lista}")    # se imprime la lista ingresada
        print(f" de esta lista, se obtienen los siguientes numeros primos: {lista_primos(lista)}")  # se aplica la funcion lista_primos sobre la lista ingresada se imprime esta misma
    except ValueError:
        print("El dato ingresado no es un numero entero")