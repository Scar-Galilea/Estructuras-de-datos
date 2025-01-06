#Galilea Peralta Contreras.
#02 de diciembre del 2024.
#Descripción:
#Este programa es una versión del juego "Piedra, papel o tijeras" que utiliza un diccionario.
#Permite registrar las victorias del jugador, los empates y las victorias del CPU.

from random import random, choice #Importamos choice para la selección aleatoria de la CPU.

#Constantes para las opciones del juego y los resultados.
PIEDRA = "Piedra"
PAPEL = "Papel"
TIJERA = "Tijera"
JUGADOR = "Gana el jugador."
EMPATE = "Empate."
CPU = "Gana la CPU."

#Función que muestra el menú y devuelve la opción seleccionada por el jugador.
def Menu():
    Eleccion_1 = None
    Eleccion_2 = None
    print("  ***  Juego del calamar ***")
    print(f"Victorias del jugador: {Victorias_del_jugador}, empates: {Empates} y victorias del CPU: {Victorias_del_CPU}  ")
    print("     0) Salir.")
    print("     1) Jugar.")
    Opcion = int(input("Ingresa una opción: "))
    if Opcion == 1:
        print()

        print("Comienza el juego")
        print("     1) Piedra.")
        print("     2) Papel.")
        print("     3) Tijera.")
        Eleccion_1 = int(input("Ingrese la primera opción: "))
        Eleccion_2 = int(input("Ingrese la segunda opción: "))
    return Opcion,Eleccion_1,Eleccion_2

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
    else:
        Jugador = None

    Lista.append(PIEDRA)
    Lista.append(PAPEL)
    Lista.append(TIJERA)

    #CPU elige aleatoriamente entre las opciones.
    Opcion_del_CPU = choice(Lista)
    return Jugador,Opcion_del_CPU

def Segunda_ronda(Opcion_1,Opcion_2,Opcion_1_CPU,Opcion_2_CPU):
    Lista = [Opcion_1_CPU,Opcion_2_CPU]
    print("Elección final")
    print(f"1) {Opcion_1}")
    print(f"2) {Opcion_2}")
    Opcion_del_jugador = int(input("Ingrese una opción: "))

    if Opcion_del_jugador == 1:
        Jugador = Opcion_1
    elif Opcion_del_jugador == 2:
        Jugador = Opcion_2
    else:
        Jugador = None

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
                       }
#Ciclo principal del juego.
while Opcion != 0: #El juego continúa mientras el jugador no elija salir.
    Resultado = None
    Opcion,Eleccion_1,Eleccion_2 = Menu() #Muestra el menú y obtiene la opción del jugador.

    if Opcion == 1:
        Opcion_1_del_Jugador, Opcion_1_del_CPU = Eleccion(Eleccion_1)
        Opcion_2_del_Jugador, Opcion_2_del_CPU = Eleccion(Eleccion_2)
        print()
        print("Resultados elegidos:")
        print(f"Jugador: {Opcion_1_del_Jugador} y {Opcion_2_del_Jugador}")
        print(f"CPU: {Opcion_1_del_CPU} y {Opcion_2_del_CPU}")
        print()
        Opcion_del_Jugador, Opcion_del_CPU = Segunda_ronda(Opcion_1_del_Jugador, Opcion_2_del_Jugador, Opcion_1_del_CPU,Opcion_2_del_CPU)
        # Determina el resultado del juego usando el diccionario.
        Resultado = Piedra_papel_tijera.get((Opcion_del_Jugador, Opcion_del_CPU), EMPATE)
        print()

    if Opcion == 0: #Salir del programa.
        print()
        print("Fin del programa.")
    #Actualiza los contadores y muestra el resultado.
    elif Resultado == JUGADOR:
        Victorias_del_jugador += 1
        print(f"Jugador: {Opcion_del_Jugador}. CPU: {Opcion_del_CPU}.")
        print(JUGADOR)
    elif Resultado == CPU:
        Victorias_del_CPU += 1
        print(f"Jugador: {Opcion_del_Jugador}. CPU: {Opcion_del_CPU}.")
        print(CPU)
    elif Resultado == EMPATE:
        Empates += 1
        print(f"Jugador: {Opcion_del_Jugador}. CPU: {Opcion_del_CPU}.")
        print(EMPATE)
    else:
        print()
        print("Opción incorrecta.") #Mensaje para opciones no válidas.

    print("______________________________________________________")
    print()
