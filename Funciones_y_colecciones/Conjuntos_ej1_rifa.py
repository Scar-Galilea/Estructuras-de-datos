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

        else:
            print("No hay correos por ver")
        print("______________________________________________________")

    elif Opcion  == 2:
        print()
        Correo_electronico_a_añadir = input("Ingrese el correo electronico: ")
        Conjunto_de_correos.add(Correo_electronico_a_añadir)
        print("¡El correo wlwctronico se añadio con exito!")
        print("______________________________________________________")
        print()
    elif Opcion == 3:
        print()
        if len(Conjunto_de_correos) != 0:
        else:
            print("No hay correos por ver")
        print("______________________________________________________")

    elif Opcion  == 4:
        print()
        if len(Conjunto_de_correos) != 0:

        else:
            print("No hay correos por ver")
        print("______________________________________________________")
    else:
        print()
        print("Opción incorrecta.")
        print()
