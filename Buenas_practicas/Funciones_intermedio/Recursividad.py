"""

Una función recursiva es una función que se llama a sí misma durante su propia ejecución.
Esto permite resolver problemas dividiéndolos en subproblemas más pequeños y manejables.

¿Cómo funciona la recursividad?
- Caso base: Toda función recursiva debe tener un caso base, que es una condición que detiene la recursión.
             Sin un caso base, la función se llamaría a sí misma infinitamente, lo que provocaría un error.
- Caso recursivo: Es la parte de la función que se llama a sí misma. En cada llamada recursiva,
                  el problema se divide en una versión más pequeña del mismo problema original.
- Llamadas sucesivas: La función se llama a sí misma repetidamente hasta que se cumple el caso base.
                      En ese momento, la función comienza a regresar a través de las llamadas anteriores,
                      combinando los resultados parciales hasta obtener la solución final.
"""


def funcion_recursiva_ascendente(numero: int) -> None:
    """
    Función que imprime un número de manera ascendente utilizando recursividad.
    :param numero: Se imprime del cero hasta este número.
    """

    # Caso base.
    if numero == 0:
        print(numero, end= ' ')

    # Caso recursivo. Busca imprimir un número menor antes de imprimir el número requerido.
    else:
        funcion_recursiva_ascendente(numero - 1)
        print(numero, end= ' ')



def funcion_recursiva_descendente(numero: int) -> None:
    """
    Función que imprime un número de manera descendente utilizando recursividad.
    :param numero: Se imprime del número hasta cero.
    """

    # Caso base.
    if numero == 0:
        print(numero, end= ' ')

    # Caso recursivo. Imprime el número y luego busca imprimir un número menor.
    else:
        print(numero, end= ' ')
        funcion_recursiva_descendente(numero - 1)



def es_numero_valido(cadena: str) -> bool:
    """
    Función que determina si el número ingresado se encuentra entre 0 y un entero positivo.
    :param cadena: Cadena a validar.
    :return: Si la cadena cumple con el formato
    """
    if cadena.isnumeric():
        return True

    else:
        return False



def main() -> None:
    """
    Función principal.
    """

    print("          ********  Programa que imprime los números de manera recursiva.  ********")
    print()

    # Se solicita un número y se valida que sea entre 0 y un entero positivo.
    num_cadena = input("Ingresa un número entre 0 y un entero positivo: ")
    print()

    # Si es un número válido, se llama a las funciones recursivas.
    # En caso contrario, finaliza el programa.
    if es_numero_valido(num_cadena):
        numero = int(num_cadena)

        print(f"Número del 0 al {numero} de manera ascendente:")
        funcion_recursiva_ascendente(numero)

        print()
        print(f"Número del 0 al {numero} de manera descendente:")
        funcion_recursiva_descendente(numero)



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()

# Nota:
# Revisar el modo depuración para ver cómo se están llamando y apilando las funciones de manera recursiva
# mediante step over y step into.
