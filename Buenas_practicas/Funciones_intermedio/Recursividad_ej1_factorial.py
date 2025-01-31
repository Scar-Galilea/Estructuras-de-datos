"""
Nombre: Galilea Peralta Contreras.
Fecha: 30 de enero del 2025.
Descripción:

Este programa calcula el factorial de un número entero positivo ingresado por el usuario, utilizando recursividad.
¡Notar que: n! = n*(n-1)!
Para ello:
    a) Solicite al usuario el número al que se requiere calcular el factorial, validando que tenga el formato adecuado.
    b) Utilice una función recursiva para calcular el factorial, indicando el caso base y el caso recursivo.
    c) Muestre el resultado en consola.
"""


def funcion_recursiva_factorial(numero: int) -> int:
    """
    Función recursiva para calcular el factorial de un número entero positivo.
    :param numero: Número entero del cual se calculará el factorial.
    :return: Factorial del número ingresado.
    """

    # Caso base: el factorial de 0 y 1 es 1.
    if numero == 0 or numero == 1:
        return 1

    else:
        # Caso recursivo: n! = n * (n-1)!
         return numero * funcion_recursiva_factorial(numero-1)




def es_numero_valido(cadena: str) -> bool:
    """
    Función que determina si el número ingresado se encuentra entre 0 y un entero positivo.
    :param cadena: Cadena a validar.
    :return: Si la cadena cumple con el formato
    """
    # Se verifica si la cadena contiene solo caracteres numéricos.
    if cadena.isnumeric():
        return True

    else:
        print("Formato no válido.")
        return False



def main() -> None:
    """
    Función principal.
    """

    print("          ********  Programa que imprime el factorial de un número de manera recursiva.  ********")
    print()

    # Se solicita un número y se valida que sea entre 0 y un entero positivo.
    num_cadena = input("Ingresa un número entre 0 y un entero positivo: ")
    print()

    # Si es un número válido, se llama a las funciones recursivas.
    # En caso contrario, finaliza el programa.
    if es_numero_valido(num_cadena):
        numero = int(num_cadena)

        print(f"El factorial de {numero} es:")
        print(funcion_recursiva_factorial(numero))
    print()
    print("Fin del programa.")


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()
