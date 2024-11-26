#Galilea Peralta Contreras.
#12 de noviembre del 2024.
#Descripción:
#Usos de los tipos básico de datos en Python
"""
Escribe un programa de nombre Listas_ej1_playlist.py que realice lo siguiente:
Este programa es una playlist de videos de YouTube.
Se debe mostrar el siguiente menú:
  ***  Playlist de videos de YouTube  ***
1) Ver playlist por videos añadidos.
2) Ver playlist por orden ascendente (A-Z).
3) Ver playlist por orden descendente (Z-A).
4) Añadir video de YouTube a la playlist.
5) Añadir varios videos de YouTube a la playlist.
6) Eliminar video de la playlist.
0) Salir.
Cualquier otro caso -> Opción no válida.

Para ello:
a) Utilice funciones para modular el código.
b) Utilice una lista para la playlist.
c) Utilice índices para mostrar los videos.
"""
def Menu():
    print("*** Playlist de videos de YouTube **+")
    print()
    print("0) Salir.")
    print("1) Ver playlist por videos añadido.")
    print("2) Ver playlist por orden ascendente (A-Z).")
    print("3) Ver playlist por orden descendente (Z-A).")
    print("4) Añadir videos.")
    print("5) Añadir varios videos.")
    print("6) Eliminar videos.")
    print()
    Opcion = int(input("Ingresa una opción: "))
    return Opcion

Videos_de_YT = []
Opcion = None

while Opcion != 0:
    Opcion = Menu()
    if Opcion  == 0:
        print()
        print("Fin del programa.")
    elif Opcion  == 1:
        Numero = 1
        for Video_de_YT in Videos_de_YT:
            print(f"{Numero}._ {Video_de_YT}")
            Numero += 1
    elif Opcion  == 2:
        print()
        Videos_de_YT.sort()
        for Video_de_YT in Videos_de_YT:
            print(Video_de_YT, end=",")
            print()
    elif Opcion  == 3:
        print()
        Videos_de_YT.sort(reverse = True)
        for Video_de_YT in Videos_de_YT:
            print(Video_de_YT, end=",")
            print()
    elif Opcion  == 4:
        print()
        Videos = input("Ingrese el video: ")
        Videos_de_YT.append(Videos)
        print()
    elif Opcion  == 5:
        print()
        Añadidos = int(input("¿Cuántos videos desea añadir? "))
        Contador_2 = 0
        while Contador_2 <= Añadidos:
            Videos = input("Ingrese el video: ")
            Videos_de_YT.append(Videos)
            Contador_2 += 1
        print()
    elif Opcion  == 6:
        Eliminar_video = input("Ingrese el video que desea eliminar: ")
        Videos_de_YT.remove(Eliminar_video)
    else:
        print()
        print("Opción incorrecta.")
        print()
