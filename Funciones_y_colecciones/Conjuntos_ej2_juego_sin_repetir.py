#Galilea Peralta Contreras.
#28 de noviembre del 2024.
#Descripción:
#Este programa almacena diversos puntos como coordenadas y permite obtener la ecuación de la recta entre dos de los puntos.
"""


Este es un juego que se puede jugar de manera grupal, en donde el objetivo es decir palabras de un tema en específico y los jugadores deben tratar de no repetir la misma palabra. Nota: no se debe mostrar las palabras en ningún caso. Además, se debe llevar un contador de la cantidad de palabras que llevan.
Se debe mostrar el siguiente menú:
  ***  Juego "sin repetir"  ***
    Mostrar las reglas del juego.
    Presiona 'enter' para comenzar.
Para ello:
a) Utilice un conjunto para almacenar las palabras ingresadas.
b) Utilice la lógica adecuada para realizar el juego.
c) Al final, se deben mostrar todas las palabras ingresadas.
"""

Conjuntos_de_palabras = set()
Conjuntos_de_repetidos = set()
Tema = None

def Menu():
    print("***  Juego sin repetir  ***")
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
    else:
        print()
        print("Opción incorrecta.")
    print("______________________________________________________")
    print()
