#Galilea Peralta Contreras.
#08 de enero de 2025.
#Descripción:
#Este programa calcula la suma acumulativa desde 0 hasta un número ingresado por el usuario.
from Ciclos.Ciclo_for import cadena


def menu() -> int:
    """
    Muestra el menu del programa
    :return: La opción del usuario
    """
    print("1) Convertir el número a entero.")
    print("2) Convertir el número a flotante.")
    print("0) Salir.")
    opcion = input("Selecciona una opción: ")

    while not opcion.isnumeric():
        print("Opción invalida")
        opcion = input("Intenta nuevamente: ")
    print()
    return opcion

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


def cadena_a_flotante(cadena: str) -> float | None:
    no_puntos = cadena.count(".")
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-").replace(".", "")
    if revisar_cadena.isnumeric() and no_guiones in (0, 1) and no_puntos in (0, 1):
        return float(cadena)
    else:
        return None

opcion = None

while opcion != 0:
    opcion = menu()
    opcion = int(opcion)
    if opcion == 1:
        num_cadena = input("Ingresa un número a converir: ")
        num_cadena = cadena_a_entero(num_cadena)
        print(f"El resultado final es {num_cadena}.")
    elif opcion == 2:
            num_cadena = input("Ingresa un número a converir: ")
            num_cadena = cadena_a_flotante(num_cadena)
            print(f"El resultado final es {num_cadena}.")
    else:
        print("Opción invalida.")

print("Salio del programa.")