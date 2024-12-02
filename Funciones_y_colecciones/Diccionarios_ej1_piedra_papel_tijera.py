#Galilea Peralta Contreras.
#02 de diciembre del 2024.
#Descripción:
#Usos de los tipos básico de datos en Python.

"""


Escribe un programa de nombre Diccionarios_ej1_piedra_papel_tijera.py que realice lo siguiente:
Este programa es una nueva versión del juego realizado de piedra, papel y tijeras, pero utilizando un diccionario para las reglas del juego.
El juego mostrará las victorias del jugador, los partidos empatados y las victorias del CPU. Se debe mostrar el siguiente menú:

  ***  Juego de piedra, papel o tijeras  ***
1) Piedra.
2) Papel.
3) Tijeras.
0) Salir.
Cualquier otro caso -> Opción no válida.
Para ello:
a) Muestre el menú en una función que pida al usuario una de las opciones: piedra, papel o tijeras.
b) Utilice un diccionario para las distintas combinaciones.
c) Realice la lógica adecuada para determinar al ganador. Se requiere que utilice al menos una función.
d) Muestre la elección del jugador y la del cpu.
e) Muestre la cantidad de victorias, empates y derrotas.
f) Repita nuevamente el menú hasta salir.
"""

from random import random, randint

PIEDRA = "Piedra"
PAPEL = "Papel"



def Menu():
    print("*** Juego de piedra, papel o tijera. **+")
    print(f"Victorias del jugador: {Victorias_del_jugador}, empates: {Empates} y victorias del CPU: {Victorias_del_CPU}  ")
    print("     1) Piedra.")
    print("     2) Papel.")
    print("     3) Tijera.")
    print("     0) Salir")
    print()
    Opcion = int(input("Ingresa una opción: "))
    return Opcion

def Eleccion(Opcion_del_jugador,Opcion_del_CPU):
    Opciones = []
    if Opcion_del_jugador == 1:
        Jugador = "Piedra"
    elif Opcion_del_jugador == 2:
        Jugador = "Papel"
    elif Opcion_del_jugador == 3:
        Jugador = "Tijera"
    Opciones = (Jugador)
    return Opciones


Opcion_del_jugador = None
Victorias_del_jugador = 0
Empates = 0
Victorias_del_CPU = 0

while Opcion_del_jugador != 0:
    Opcion_del_jugador = Menu()
    Opcion_del_CPU = randint(1, 3)  #La CPU elige aleatoriamente entre 1, 2 y 3.

    Jugador, CPU = Eleccion(Opcion_del_jugador,Opcion_del_CPU)

    Jugador = Opcion_del_jugador
    #Comprobación de condiciones para jugar o salir.
    if Opcion_del_jugador != 0:
        # Si ambos eligen lo mismo, es empate.
        if (Opcion_del_jugador == 1 and Opcion_del_CPU == 1) or (Opcion_del_jugador == 2 and Opcion_del_CPU == 2) or (Opcion_del_jugador == 3 and Opcion_del_CPU == 3):
            print()
            Empates += 1
            print(f"Jugador: {Jugador}. CPU: {CPU}. El resultado es empate.")
            print("------------------------------------")
            print()

        elif (Opcion_del_jugador == 1 and Opcion_del_CPU == 2) or (Opcion_del_jugador == 2 and Opcion_del_CPU == 3) or (Opcion_del_jugador == 3 and Opcion_del_CPU == 1):
            print()
            print(f"Jugador: {Jugador}. CPU: {CPU}. El ganador es el CPU.")
            Victorias_del_CPU += 1
            print("------------------------------------")
            print()
        elif (Opcion_del_jugador == 1 and Opcion_del_CPU == 3) or (Opcion_del_jugador == 2 and Opcion_del_CPU == 1) or (Opcion_del_jugador == 3 and Opcion_del_CPU == 2):
            print()
            print(f"Jugador: {Jugador}. CPU: {CPU}. El ganador es el jugador.")
            Victorias_del_jugador += 1
            print("------------------------------------")
            print()

        else:
            print()
            print("Opción inválida")
            print("-----------------------------------")
            print()
print()
print("Salio del programa")