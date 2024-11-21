def mismos_caracteres(lista_cadena : list) -> dict:

    """
    Args: lista_cadena: una lista con datos de tipo string 
    Output: Un diccionario que registra como claves el orden lexicografico de las palabras en lista_cadena, y toma como valor una lista que guarda aquellas palabras que tienen el mismo orden lexicografico

    """
    palabras_unicas = {}
    for i in range(0,len(lista_cadena)):
        lista_cadena[i] = lista_cadena[i].lower()
    for i in range(0,len(lista_cadena)):
        analisis = "".join(sorted(lista_cadena[i]))
        if analisis not in palabras_unicas:
            palabras_unicas[analisis] = [lista_cadena[i]]
            continue
        if analisis in palabras_unicas:
            palabras_unicas[analisis].append(lista_cadena[i])
    return palabras_unicas

if __name__ == "__main__":
    try:
        len_lista : int = int(input("Digite el numero de datos para la lista de numeros: "))    # se ingresa el numero de datos para la lista
        lista = []  # se define la lista vacia
        for i in range(0, len_lista):   # se hace un recorrido para el ingreso de datos en la lista segun el numero registrado anteriormente
            dato = str(input("Ingrese la palabra para la lista: "))
            lista.append(dato)
        palabras_comp = mismos_caracteres(lista)    # se aplica la funcion sobre la lista ingresada 
        for k, v in palabras_comp.items():  # se recorre el diccionario para imprimir las listas con una longitud mayor a 1, es decir, que en la lista original tengan mas de una palabra con el mismo orden lexicografico 
            if len(v) > 1:
                print(v, end=" ")
    except ValueError:
        print("El dato ingresado no es una cadena de caracteres")