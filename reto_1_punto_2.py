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