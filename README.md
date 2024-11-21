# poo_reto_1
### Soy Rafael Santiago Chirivi Peña y pertenezco al grupo de "Fenomenoides", adelante se muestra nuestro logo 

<details><summary>Preparense para ver el grandioso logo: </summary><p>
<div align='center'>
<figure> <img src="https://i.postimg.cc/NFbwf57S/logo-def.png" alt="Defensa Civil" width="400" height="auto"/></br>
<figcaption><b> "somos programadores, no diseñadores" </b></figcaption></figure>
</div>
</p></details><br>

A manera de practica y para refrescar los distintos conceptos abordados en el curso de programacion de computadores, se propusieron distintos retos como practica, a continuacion se muestra la solucion propuesta a los mismos:

1. Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. *entrada:* `(1,2,"+")`, *salida* `(3)`.
```python
def operaciones (n1: float, n2: float, oper: str) -> float:

    """
    args: n1: numero real, n2: numero real, oper: cadena que representa una operacion a realizar
    output: toma en cuenta dos numeros ingresados y segun el ingreso del usuario para la operacion, se retorna esta misma en una estructura    n1 (operacion) n2 = (operacion de n1 con n2)
    """
    match oper:
        case "+":
            print(f"{n1} + {n2} = {n1 + n2}")
        case "-":
            print(f"{n1} - {n2} = {n1 - n2}")
        case "*":
            print(f"{n1} * {n2} = {n1 * n2}")
        case "/":
            print(f"{n1} / {n2} = {n1 / n2}")
            
if __name__ == "__main__":
    try:
        num1 = float(input("Ingrese el numero 1 a operar: "))   # ingreso de primer numero real
        num2 = float(input("Ingrese el numero 2 a operar: "))   # ingreso de segundo numero real
        oper = str(input("Ingrese la operacion a realizar (+, -, *. /): ")) # ingreso de operacion
        operaciones(num1, num2, oper)   # aplicacion de la funcion operaciones sobre los datos ingresados
    except ValueError:
        print("El dato ingresado no es un numero real")
```
La solucion para este ejercicio no requirio de un proceso de pensamiento extenso, puesto que solo se trataba de hacer uso de funciones y retornar un print adecuado segun el caso de la operacion, para un mejor entendimiento de la funcion, opte por utilizar `match case` como una alternativa a cadenas de `elifs`

2. Realice una función que permita validar si una palabra es un palíndromo. **Condición:** No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.
```python
def lista_texto (text: str) -> list:
    
    """
    args: text: recibe una cadena de caracteres
    output: retorna una lista donde cada letra de la palabra es un dato dentro de la lista
    """
    lista = []
    for i in range(0, len(text)):
        lista.append(text[i])
    return lista
def palindromo (text : str) -> str:

    """
    args: text: recibe una cadena de caracteres
    output: luego de aplicar la funcion lista_texto sobre el texto recibido, se crea una nueva lista donde se ingresan los datos de la lista desde el ultimo hasta el primero, paa luego comparar si tienen los mismos datos en mismo orden, determinando asi si es palindromo o no
    """
    text = text.lower()
    text = lista_texto(text)
    text_inv = []
    for i in range(0,len(text)):
        text_inv.append(text[-1-i])
    if text == text_inv:
        print(f"La palabra {"".join(text)} es un palindromo")
    if text != text_inv:
        print(f"La palabra {"".join(text)} NO es un palindromo")

if __name__ == "__main__":
    palabra : str = str(input("Ingrese la palabra para verificar si es un palindromo")) # se ingresa la palabra a la cual analizar
    palindromo(palabra) # se aplica la funcion palindromo sobre la palabra ingresada
```
La solucion a esste ejercicio se vio dada en torno a la flexibilidad de indexacion que ofrece python, haciendo que indexaciones negativas hagan un recorrido "inverso" para el dato que se este analizando, por lo cual me aproveche de esta caracteristica para poder plantear el inverso de una palabra sin uso de slicing, y luego solo hacer una comparacion logica entre el inverso y la palabra original.

3. Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.
```python
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
```
La solucion de este ejercicio recayo principalmente en como modelar una funcion que detectara si un numero es primo o no, y aunque habiendo diferentes metodos, decidi optar por algo que se me ocurrio en el momento, permitiendome contar el numero de divisores para un mismo numero y a partir de la idea de que un primo solo tiene dos divisores (1 y si mismo), esto fuera lo que determinara que el numero analizado era primo

4. Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.
```python
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
```
Aunque el ejercicio solo solicitaba retornar la mayor suma entre los numeros consecutivos, como parte de mi idea para hallar esa suma mayor, derivo tambien el obtener las posiciones de la lista de las cuales se obtenia la mayor suma, creando asi una matriz que gracias a como python ordena listas dentro de listas, permitiendo hacer un orden ascendente o descendente si el primer dato de las listas es un numero, me aproveche de esto para llegar al resultado esperado

5. Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: `["amor", "roma", "perro"]`, salida `["amor", "roma"]`
```python
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
```
Por ultimo, y recordando el ultimo tema visto en el semestre pasado, surgio la idea de usar diccionarios para poder recopilar las palabras que encajaran en el orden esperado para cada palabra, asi, luego de recorrida toda la lista de cadenas de caracteres, terminara un diccionario con claves del orden lexicografico y valores de palabras que se encontraban en ese orden, pero segun lo solicitado por el ejercicio, solo se imprime aquellos valores cuyas listas tengan mas de 1 elemento
