"""
Nombre: Galilea Peralta Contreras.
Fecha: 30 de enero del 2025.
Descripción:

Este programa realiza la suma de todos los números pares ingresados por el usuario.
Para ello:
    a) Solicite al usuario los números enteros. Nota: Hay que validar que tengan el formato adecuado.
    b) Utilice una función con argumentos variables que devuelva la suma de los números pares.
    c) Muestre el resultado en consola.

"""


def suma_de_pares(titulo: str = None, *vargs) -> None:
    """
    Función que muestra la suma de los números pares con argumentos variables.
    :param titulo: Nombre de suma.
    :param vargs: Lista de números pares ingresados por el usuario.
    """

    # Se calcula la suma total.
    suma_total = None
    if len(vargs) != 0:
        suma_total = sum(vargs)
    print(f"El promedio de la materia {titulo} es: {suma_total}")



def cadena_a_entero(cadena: str) -> int | None:
    """
       Muestra el menu del programa
       :param cadena: Lo que ingresa el usuario
       :return: Un número entero o None
       """
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-")
    if revisar_cadena.isnumeric() and no_guiones in(0,1) :
        return  int(cadena)
    else:
        return None



def main() -> None:
    """
    Función principal.
    """

    print("          ******** Programa para Sumar números pares con argumentos variables. ********")
    print()

    materia = "suma"

    # Se solicitan los números mediante un ciclo, el cual termina hasta ingresar 'enter'.
    # Lista para almacenar los números pares ingresados por el usuario.
    suma = []
    num_cadena = input(f"Ingresa el número [{len(suma) + 1}] o presiona enter para continuar: ")

    while bool(num_cadena):
        # Se convierte la cadena ingresada a un número entero si es válido
        numero = cadena_a_entero(cadena= num_cadena)

        if numero is None:
            print("Formato no válido, intenta nuevamente.")
        # Si el número es impar, se ignora y no se suma.
        elif numero % 2 != 0:
            pass
        else:
            suma.append(numero)

        num_cadena = input(f"Ingresa el  número [{len(suma) + 1}] o presiona enter para continuar: ")
    # Se llama a la función para calcular la suma de los números pares.
    suma_de_pares(materia, *suma)



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()


