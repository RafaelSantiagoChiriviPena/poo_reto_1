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