#25 de noviembre del 2024.
#Descripción:
#Este programa te introduce 7 formas en las que estarán los equipos.

"""
Escribe un programa de nombre ej3_rol_de_juegos.py que realice lo siguiente:
Este programa almacena 8 jornadas en 2 equipos, los cuales compiten entre sí.
a) Se requiere realizar 7 grupos diferentes en donde las jornadas compiten sin repetir el enfrentamiento.

b) El movimiento de las jornadas será al contrario de las manecillas del reloj.

c) La jornada 1 no se moverá en ningún caso.
"""

# Inicialización de las jornadas
Equipo_1 = ["Jornada 1", "Jornada 2", "Jornada 3", "Jornada 4"]
Equipo_2 = ["Jornada 5", "Jornada 6", "Jornada 7", "Jornada 8"]


Auxiliar = None
Grupo = 1
#Mostrar los Grupos de jornadas.
while Grupo <= 7:
    Contador = 0
    print(f"Grupo {Grupo}:")
    #Mostrar los enfrentamientos del grupo actual.
    while Contador < 4:
        print(Equipo_1[Contador],end = " ")
        print(Equipo_2[Contador])
        Contador += 1
    print("_______________________________________________")

    """
    Otra forma en las cuales se hacen los movimientos de las jornadas.
    Auxiliar = Equipo_2[1]
    Auxiliar_2 = Equipo_2[2]
    Auxiliar_3 = Equipo_2[3]
    Auxiliar_4 = Equipo_1[3]

    Equipo_1.insert(1, Equipo_2[0])
    Equipo_2.insert(0, Auxiliar)
    Equipo_2.insert(1, Auxiliar_2)
    Equipo_2.insert(2, Auxiliar_3)
    Equipo_2.insert(3, Auxiliar_4)
    """

    #Realizar el movimiento de las jornadas al contrario de las manecillas del reloj.
    #Jornada 1 permanece fija, rotamos los demás elementos.
    #Movimiento en Equipo 1 y Equipo 2
    Equipo_1.insert(1, Equipo_2.pop(0))  #Insertar el primer elemento de Equipo_2 en la segunda posición de Equipo_1.
    Equipo_2.append(Equipo_1.pop(-1))  #Mover el último elemento de Equipo_1 al final de Equipo_2.

    Grupo += 1


