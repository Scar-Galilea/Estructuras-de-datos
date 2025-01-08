#Galilea Peralta Contreras.
#07 de enero de 2025.
#Descripción:
#Este programa calcula la suma acumulativa desde 0 hasta un número ingresado por el usuario.

"""
prueba_numero = int(input("Ingresa n: "))
print()
cadena = input ("Ingresa cadena: ").strip()

print(cadena.isnumeric())
print(cadena.isalpha())
print(cadena.isalnum())

numero = input("Ingresa n: ")
print()
while not numero.isnumeric():
    print("Opción invalida")
    numero = input("Intenta nuevamente: ")
print()
numero = int(numero)
print(f"El número {numero} es el tipo { type(numero)}")
"""

"""
def cadena_a_entero(cadena):
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-")

    if revisar_cadena.isnumeric() and no_guiones in(0,1) :
        return  int(cadena)
    else:
        return None

num_cadena = input("Ingresa Z: ")
numero = cadena_a_entero(num_cadena)

while numero is None:
    print("Opcion invalida")
    num_cadena = input("Intenta nuevamente: ")
    numero = cadena_a_entero(num_cadena)

print(f"El número {numero} es tipo {type(numero)}")
"""

def cadena_a_flotante (cadena):
    no_puntos = cadena.count(".")
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-").replace(".","")

    if revisar_cadena.isnumeric() and no_guiones in(0,1) and no_puntos in(0,1) :
        return  float(cadena)
    else:
        return None

num_cadena = input("Ingresa Z: ")
numero = cadena_a_flotante(num_cadena)

while numero is None:
    print("Opcion invalida")
    num_cadena = input("Intenta nuevamente: ")
    numero = cadena_a_flotante(num_cadena)

print(f"El número {numero} es tipo {type(numero)}")
