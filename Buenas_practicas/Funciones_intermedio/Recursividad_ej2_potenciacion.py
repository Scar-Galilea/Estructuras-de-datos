"""
Nombre: Galilea Peralta Contreras.
Fecha: 31 de enero del 2025.
Descripción:

Este programa calcula la potencia de un número a otro número de manera recursiva. Ambos son números enteros positivos ingresados por el usuario.
Notar que: a^b = a*(a^(b-1)).
Para ello
    a) Solicite al usuario ambos números, validando que tengan el formato adecuado.
    b) Utilice una función recursiva para calcular la potencia, indicando el caso base y el caso recursivo.
    c) Muestre el resultado en consola.
"""


def funcion_recursiva_potenciacion(a: int ,b: int) -> int:
    """
    Función recursiva para calcular la potencia de un número entero positivo.
    :param a: Base de la potencia.
    :param b: Exponente de la potencia.
    :return: Resultado de la operación a^b.
    """
    # Caso base: cualquier número elevado a 0 es 1.
    if b == 0 :
        return 1
    # Caso especial: 0 elevado a cualquier número mayor que 0 es 0.
    elif a == 0:
        return 0
    # Caso recursivo: a^b = a * a^(b-1).
    else:
         return a * funcion_recursiva_potenciacion(a^(b-1))




def es_numero_valido(cadena: str,cadena_2: str) -> bool:
    """
    Función que determina si las cadenas ingresadas representan números enteros positivos válidos.
    :param cadena: Base de la potenciación.
    :param cadena_2: Exponente de la potenciación.
    :return: True si ambos números son enteros positivos y válidos, False en caso contrario.
       """
    # Se verifica si la cadena contiene solo caracteres numéricos.
    if cadena.isnumeric() and cadena_2.isnumeric():
        # Se maneja el caso especial 0^0 que es una indeterminación.
        if cadena == "0" and cadena_2 == "0":
            print("0 ^ 0 = Indeterminado.")
            return False
        else:
            return True
    else:
        print("Formato no válido.")
        return False



def main() -> None:
    """
    Función principal.
    """

    print("          ********  Programa que imprime la potenciación de un número de manera recursiva.  ********")
    print()

    # Se solicita al usuario la base y el exponente.
    base = input("Ingresa la base a: ")
    exponente = input("Ingresa el exponente b: ")
    print()

    # Si los valores ingresados son válidos, se convierten a enteros y se calcula la potencia.
    # Si es un base y el exponente son igual 0, finaliza el programa.
    # En caso contrario, finaliza el programa.
    if es_numero_valido(base,exponente):
        base = int(base)
        exponente = int(exponente)
        # Se muestra el resultado de la potenciación calculada recursivamente.
        print(f"{base} ^ {exponente} = ",end=" ")
        print(funcion_recursiva_potenciacion(base,exponente))
    print()
    print("Fin del programa.")


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()
