#Galilea Peralta Contreras.
#28 de noviembre del 2024.
#Descripción:
#Este programa almacena diversos puntos como coordenadas y permite obtener la ecuación de la recta entre dos de los puntos.
"""
Escribe un programa de nombre Conjuntos_ej1_rifa.py que realice lo siguiente:
Este programa es una rifa, en donde se registra el correo electrónico y solamente permite ingresar un correo por participante.
Se debe mostrar el siguiente menú:

  ***  Rifa de una computadora  ***
1) Ver correos de participantes.
2) Agregar correo de participante.
3) Eliminar correo de participante.
4) Seleccionar ganador.
0) Salir.

Cualquier otro caso -> Opción no válida.
Para ello:
a) Utilice un conjunto para almacenar los correos de los participantes.
b) Utilice un valor aleatorio utilizando la función random.choice(lista). Notar que hay que convertir primero a una lista.
"""
from random import random, choice


#Función para mostrar el menú y devolver la opción seleccionada.
def Menu():
    print("***  Rifa de una computadora  ***")
    print()
    print("0) Salir.")
    print("1) Ver correos de participantes.")
    print("2) Agregar correo de participante.")
    print("3) Eliminar correo de participante.")
    print("4) Seleccionar ganador.")
    print()

    Opcion = int(input("Ingrese la opción: "))
    return Opcion


Conjunto_de_correos = set()
Opcion = None

while Opcion != 0:
    Opcion = Menu()
    if Opcion == 0:
        print()
        print("Fin del programa.")
    elif Opcion == 1:
        print()
        if len(Conjunto_de_correos) != 0:
            print("El conjunto de correos electronicos es:")
            for Correo_electronico in Conjunto_de_correos :
                print(f"-{Correo_electronico}")
        else:
            print("No hay participantes por mostrar.")

    elif Opcion  == 2:
        print()
        Correo_electronico_a_añadir = input("Ingrese el correo electronico del participante a agregar: ")
        Conjunto_de_correos.add(Correo_electronico_a_añadir)
        print(f"¡El correo electronico {Correo_electronico_a_añadir} se añadio con exito!")
    elif Opcion == 3:
        print()
        if len(Conjunto_de_correos) != 0:
            for Correo_electronico in Conjunto_de_correos :
                print(f"-{Correo_electronico}")
            print()
            Correo_electronico_a_eliminar =input("Ingrese el correo electronico del participante a eliminar: ")
            Conjunto_de_correos.remove(Correo_electronico_a_eliminar)
            print(f"¡El correo electronico se elimino con exito!")
        else:
            print("No hay participantes por eliminar.")
    elif Opcion  == 4:
        print()
        if len(Conjunto_de_correos) != 0:
            print()
            Lista_de_correos = list(Conjunto_de_correos)
            Ganador = choice(Lista_de_correos)
            print(f"El correo ganador es {Ganador}")
            print("¡Muchas felicidades!")
        else:
            print("No hay correos por seleccionar.")
    else:
        print()
        print("Opción incorrecta.")
    print("______________________________________________________")
    print()