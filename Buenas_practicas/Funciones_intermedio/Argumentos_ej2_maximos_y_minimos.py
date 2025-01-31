"""
Nombre: Galilea Peralta Contreras.
Fecha: 30 de enero del 2025.
Descripción:
Este programa encuentra el valor máximo y mínimo de todos los números ingresados por el usuario.
Para ello:
    a) Solicite los números con decimales, validando que tengan el formato adecuado.
    b) Utilice una función con argumentos variables que devuelva el valor máximo y mínimo.
    c) Muestre el resultado en consola.
"""


def calcular_minimo_y_maximos(materia: str = None, *vargs) -> None:
    """
    Función que muestra el máximo y mínimo con argumentos variables.
    :param materia: Título del cálculo (en este caso, "Máximo y mínimo").
    :param vargs: Tupla de números.
    """
    # Se inicializan las variables con el primer valor de la tupla.
    maximo = vargs[0]
    minimo = vargs[0]

    # Se recorre la tupla de números para determinar el mínimo y máximo.
    for i in vargs:
        if i > maximo:
            maximo = i # Se actualiza el valor máximo si se encuentra un número mayor.
        else:
            if i < minimo: # Se actualiza el valor mínimo si se encuentra un número menor.
                minimo = i

    # Se muestra el mínimo y máximo.
    print(f"El número mínimo es: {minimo}")
    print(f"El número máximo es: {maximo}")


def cadena_a_flotante(cadena: str) -> float | None:
    """
    Función que convierte una cadena a un número flotante.
    :param cadena: Cadena a convertir.
    :return: Regresa el número flotante si cumple con el formato, en caso contrario, devuelve None.
    """

    no_puntos = cadena.count(".")
    no_guiones = cadena.count("-")
    revisar_cadena =cadena.lstrip('-').replace(".","")

    if revisar_cadena.isnumeric() and no_guiones in (0, 1) and no_puntos in (0, 1):
        return float(cadena)
    else:
        return None



def main() -> None:
    """
    Función principal.
    """

    print("          ********  Programa para encontrar máximos y mínimos con argumentos variables. ********")
    print()

    Titulo = "Máximo y mínimo."


    # Lista para almacenar los números ingresados por el usuario.
    suma = []

    # Se solicitan los números mediante un ciclo, el cual termina hasta ingresar 'enter'.
    num_cadena = input(f"Ingresa el número [{len(suma) + 1}] o presiona enter para continuar: ")
    while bool(num_cadena):
        # Se convierte la cadena ingresada a número flotante si es válido.
        numero = cadena_a_flotante(cadena= num_cadena)

        if numero is None:
            print("Formato no válido, intenta nuevamente.")
        else:
            suma.append(numero)

        num_cadena = input(f"Ingresa el  número [{len(suma) + 1}] o presiona enter para continuar: ")

    # Se llama a la función para calcular el mínimo y el máximo de los números ingresados.
    calcular_minimo_y_maximos(Titulo, *suma)

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
        main()

