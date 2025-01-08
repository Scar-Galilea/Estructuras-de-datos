#Galilea Peralta Contreras.
#08 de enero de 2025.
#Descripción:
#Este programa calcula la suma acumulativa desde 0 hasta un número ingresado por el usuario.

#TODO imprementar menú
def menu():
    pass

def cadena_a_entero(cadena):
    ...

#TODO
def cadena_a_flotante(cadena):
    raise NotImplementedError("Implemenrtar función")


opcion = menu()
while opcion != 0:
    if opcion == 1:
        num_cadena = input("Ingresa un número a converir: ")
        num_cadena = cadena_a_entero(num_cadena)
    else:
        if opcion == 2:
            num_cadena = input("Ingresa un número a converir: ")
            num_cadena = cadena_a_flotante(num_cadena)
print("Salio del programa")





