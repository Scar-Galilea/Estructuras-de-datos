#Galilea Peralta Contreras.
#08 de enero de 2025.
#Descripción:
#Este programa calcula la suma acumulativa desde 0 hasta un número ingresado por el usuario.

#TODO imprementar menú
def menu():
    pass

def cadena_a_entero(cadena: str) -> int | None:
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-")

    if revisar_cadena.isnumeric() and no_guiones in(0,1) :
        return  int(cadena)
    else:
        return None
#TODO
def cadena_a_flotante(cadena):
    def cadena_a_flotante(cadena):
        no_puntos = cadena.count(".")
        no_guiones = cadena.count("-")
        revisar_cadena = cadena.lstrip("-").replace(".", "")

        if revisar_cadena.isnumeric() and no_guiones in (0, 1) and no_puntos in (0, 1):
            return float(cadena)
        else:
            return None
opcion = menu()
while opcion != 0:
    if opcion == 1:
        num_cadena = input("Ingresa un número a converir: ")
        num_cadena = cadena_a_entero(num_cadena)
        print(f"el resultado final es {num_cadena}")
    else:
        if opcion == 2:
            num_cadena = input("Ingresa un número a converir: ")
            num_cadena = cadena_a_flotante(num_cadena)
            print(f"el resultado final es {num_cadena}")

print("Salio del programa")





