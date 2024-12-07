#Galilea Peralta Contreras.
#06 de diciembre del 2024.
#Descripción:
#Este programa es una versión mejorada del juego "Piedra, papel, tijeras, lagarto, Spock".
#Utiliza un diccionario para definir las reglas del juego y permite llevar un registro de victorias, empates y derrotas.

"""
Escribe un programa de nombre Diccionarios_ej2_piedra_papel_tijera_lagarto_spock.py que realice lo siguiente:
Este programa es una versión mejorada del juego de piedra, papel y tijeras. Las reglas se muestran en el siguiente video:
Se debe mostrar el siguiente menú:

  ***  Juego de piedra, papel, tijeras, lagarto, spock  ***
1) Piedra.
2) Papel.
3) Tijeras.
4) Lagarto.
5) Spock.
6) Ver reglas.
0) Salir.

Cualquier otro caso -> Opción no válida.
Para ello:
a) Muestre el menú en una función que pida al usuario una de las opciones.
b) Utilice un diccionario para las distintas combinaciones.
c) Realice la lógica adecuada para determinar al ganador.
d) Muestre la elección del jugador y la del cpu.
e) Muestre la cantidad de victorias, empates y derrotas.
f) Repita nuevamente el menú hasta salir.
"""
from random import random, choice #Importamos choice para la selección aleatoria de la CPU.

#Constantes para las opciones del juego y los resultados.
PIEDRA = "Piedra."
PAPEL = "Papel."
TIJERA = "Tijera."
LAGARTO = "Lagarto."
SPOCK = "Spock."
JUGADOR = "Gana el jugador."
EMPATE = "Empate."
CPU = "Gana la CPU."

#Función que muestra el menú y devuelve la opción seleccionada por el jugador.
def Menu():
    print("  ***  Juego de piedra, papel o tijeras  ***")
    print(f"Victorias del jugador: {Victorias_del_jugador}, empates: {Empates} y victorias del CPU: {Victorias_del_CPU}  ")
    print("     1) Piedra.")
    print("     2) Papel.")
    print("     3) Tijera.")
    print("     4) Lagarto.")
    print("     5) Spock.")
    print("     6) Ver reglas.")
    print("     0) Salir.")
    print()
    Opcion = int(input("Ingresa una opción: "))
    return Opcion

#Función que realiza la elección del jugador y la del CPU.
def Eleccion(Opcion_del_jugador):
    Lista = []
    #Asigna la opción del jugador según la entrada seleccionada.
    if Opcion_del_jugador == 1:
        Jugador = PIEDRA
    elif Opcion_del_jugador == 2:
        Jugador = PAPEL
    elif Opcion_del_jugador == 3:
        Jugador = TIJERA
    elif Opcion_del_jugador == 4:
        Jugador = LAGARTO
    elif Opcion_del_jugador == 5:
        Jugador = SPOCK
    else:
        Jugador = None

    Lista.append(PIEDRA)
    Lista.append(PAPEL)
    Lista.append(TIJERA)
    Lista.append(LAGARTO)
    Lista.append(SPOCK)

    #CPU elige aleatoriamente entre las opciones.
    Opcion_del_CPU = choice(Lista)
    return Jugador,Opcion_del_CPU

#Inicialización de variables del programa.
Opcion = None #Opción del menú seleccionada por el jugador.
Victorias_del_jugador = 0 #Contador de victorias del jugador.
Empates = 0 #Contador de empates.
Victorias_del_CPU = 0  #Contador de victorias del CPU.

#Diccionario que define las reglas del juego.
Piedra_papel_tijera = {(PIEDRA, TIJERA): JUGADOR,
                       (PIEDRA, PAPEL): CPU,
                       (TIJERA, PAPEL): JUGADOR,
                       (TIJERA, PIEDRA): CPU,
                       (PAPEL, PIEDRA): JUGADOR,
                       (PAPEL, TIJERA): CPU,
                       (PIEDRA, LAGARTO): JUGADOR,
                       (LAGARTO, PIEDRA): CPU,
                       (LAGARTO, SPOCK): JUGADOR,
                       (SPOCK, LAGARTO): CPU,
                       (SPOCK, TIJERA): JUGADOR,
                       (TIJERA, SPOCK): CPU,
                       (TIJERA, LAGARTO): JUGADOR,
                       (LAGARTO, TIJERA): CPU,
                       (LAGARTO, PAPEL): JUGADOR,
                       (PAPEL, LAGARTO): CPU,
                       (PAPEL, SPOCK): JUGADOR,
                       (SPOCK, PAPEL): CPU,
                       (SPOCK, PIEDRA): JUGADOR,
                       (PIEDRA, SPOCK): CPU,
                       }
#Ciclo principal del juego.
while Opcion != 0: #El juego continúa mientras el jugador no elija salir.
    Opcion = Menu() #Muestra el menú y obtiene la opción del jugador.
    print()
    Opcion_del_Jugador, Opcion_del_CPU = Eleccion(Opcion)   #Obtiene la elección del jugador y del CPU.

    #Determina el resultado del juego usando el diccionario.
    Resultado = Piedra_papel_tijera.get((Opcion_del_Jugador, Opcion_del_CPU), EMPATE)

    if Opcion == 0: #Salir del programa.
        print("Fin del programa.")
    #Mostrar las reglas del juego.
    elif Opcion == 6:
        print("Reglas:")
        print("Selecciona una de las opciones de acuerdo a lo siguiente:")
        print("-Tijeras cortan papel.")
        print("-Papel cubre piedra.")
        print("-Piedra aplasta lagarto.")
        print("-Lagarto envenena Spock.")
        print("-Spock destruye tijeras.")
        print("-Tijeras decapitan lagarto.")
        print("-Lagarto come papel.")
        print("-Papel desaprueba Spock.")
        print("-Spock vaporiza piedra.")
        print("-Piedra aplasta tijeras.")

    #Actualiza los contadores y muestra el resultado.
    elif Resultado == JUGADOR:
        Victorias_del_jugador += 1
        print(f"Jugador: {Opcion_del_Jugador} CPU: {Opcion_del_CPU} {JUGADOR}")
    elif Resultado == CPU:
        Victorias_del_CPU += 1
        print(f"Jugador: {Opcion_del_Jugador} CPU: {Opcion_del_CPU} {CPU}")
    elif Resultado == EMPATE:
        Empates += 1
        print(f"Jugador: {Opcion_del_Jugador} CPU: {Opcion_del_CPU} {EMPATE}")
    else:
        print()
        print("Opción incorrecta.") #Mensaje para opciones no válidas.

    print("______________________________________________________")
    print()
