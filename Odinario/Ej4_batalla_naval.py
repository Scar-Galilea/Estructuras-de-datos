"""
Nombre: Galilea Peralta Contreras.
Fecha: 10 de febrero del 2025.
Descripción: Juego de Batalla Naval en consola donde dos jugadores colocan sus barcos y se turnan para atacar posiciones en el tablero del oponente.
"""
ROJO = "\033[91m"
AZUL = "\033[94m"
RESET = "\033[0m"
TOCADO = "Tocado"
AGUA = "Agua"


def menu() -> int:
    """
    Muestra el menú principal y obtiene la opción del usuario.
    :return: Un número entero que representa la opción seleccionada.
    """
    batalla = """
    BBBBB   AAAAA  TTTTT  AAAAA  L      L       AAAAA
    B    B A     A   T   A     A L      L      A     A
    BBBBB  AAAAAAA   T   AAAAAAA L      L      AAAAAAA
    B    B A     A   T   A     A L      L      A     A
    BBBBB  A     A   T   A     A LLLLL  LLLLL  A     A
    """

    naval = """
    N     N   AAAAA  V     V   AAAAA  L            
    NN    N  A     A  V     V  A     A L                 
    N N   N  AAAAAAA  V     V  AAAAAAA L            
    N  N  N  A     A   V   V   A     A L                 
    N   N N  A     A    VVV    A     A LLLLL       
    """

    # Imprimir el texto con colores
    print(ROJO + batalla + RESET)
    print(AZUL + naval + RESET)

    print("0) Salir.")
    print("1) Jugar.")
    print("2) instrucciones.")
    opcion = input("Ingrese la opcion: ")
    opcion = verificar(opcion) # Convierte la opción a número entero y verifica validez.

    # Bucle para validar la opción hasta que sea correcta.
    while not (opcion  == 0 or opcion == 1 or opcion == 2):
        print("Opción invalida.")
        print("___________________________________________________________________")
        opcion = input("Intenta nuevamente: ")
        opcion = verificar(opcion)
        print()

    return int(opcion)


def verificar(opcion:str) -> int:
    """
    Verifica si la entrada del usuario es un número entero.
    Si no lo es, sigue pidiendo la entrada hasta que sea válida.
    :return: La opción convertida a entero.
    """
    while not opcion.isnumeric(): # Verifica si la entrada es numérica.
        print("Opción invalida.")
        print("___________________________________________________________________")
        opcion = input("Intenta nuevamente: ")
        print()
    return  int(opcion)

def mostrar_posiciones():
    """
    Muestra un mapa de coordenadas de 10x10 para que los jugadores ubiquen sus barcos.
    """
    columna = 0
    fila = 0
    print("Posiciones de los barcos:")
    for i in range(100):  # Genera una cuadrícula de 10x10.
        print(f"{columna},{fila}", end="  ")  # Muestra coordenadas de cada posición.
        fila += 1
        if (i + 1) % 10 == 0: # Salto de línea cada 10 elementos para mantener el formato.
            print()
            columna += 1
            fila = 0

def desplegar_barcos(num_de_bracos : int ) -> list[int]:
    """
    Permite a un jugador colocar sus barcos en el tablero.
    :return: Una lista con las coordenadas de los barcos en formato fila-columna.
    """
    lista = [-1] * num_de_bracos * 2 # Lista para almacenar las coordenadas.
    contador = 0
    mostrar_posiciones() # Muestra la referencia del tablero.

    print()
    while contador < num_de_bracos:
        print(f"Escoge la posición del barco número {contador + 1}. ")
        columna = input("Columna: ")
        columna = verificar(columna)
        fila = input("Fila: ")
        fila = verificar(fila)

        # Verifica que las coordenadas estén dentro del tablero (0-9).
        while not (0 <= columna <= 9) and not (0 <= fila <= 9):
            print("la coordenadas son diferentes al tablero.")
            print("___________________________________________________________________")
            print("Intente nuevamente.")
            columna = input("Columna: ")
            columna = verificar(columna)
            fila = input("Fila: ")
            fila = verificar(fila)
        # Verifica si la coordenada ya está ocupada por otro barco.
        for k in range(num_de_bracos):
            if lista[k + 1 * k] == fila and lista[k + 1 + 1 * k] == columna:
                contador = contador - 1
                print()
                print("Opcion repetida.")
                print("Vuelva ingresar el anterio barco.")
        # Almacena las coordenadas en la lista.
        lista.insert(contador + 1 * contador, fila)
        lista.insert(contador + 1 + 1 * contador, columna)

        contador += 1
        print()
    return  lista

def mostrar_barcos(indice : int):
    """
    Función que muestra la posición de un barco en un tablero de 10x10.
    :param indice: Posición en la lista donde se colocará el barco.
    """
    # Se crea una lista de 100 elementos representando el tablero con agua ("~").
    lista = ["~"] * 100

    # Se inserta el barco ("⛴") en la posición indicada.
    lista.insert(indice, "⛴")

    # Se muestra el tablero en formato de matriz (10x10).
    print()
    for i in range(100):
        print(lista[i], end="  ")  # Imprime cada elemento con un espacio.

        # Cada 10 elementos, se hace un salto de línea para mantener el formato.
        if (i + 1) % 10 == 0:
            print()
    print()  # Salto de línea final para mejor presentación.



def ganador(lista:list[str],numero: int) -> tuple[int, int]:
    """
    Verifica si el jugador ha ganado. Si todos los barcos han sido hundidos, devuelve (0,0).
    Si aún quedan barcos, devuelve (1,1).
       """
    bandera = 0
    for i in lista:
        if i != "~": # Si hay barcos restantes, el juego continúa.
            bandera = 1
            break

    if bandera == 0:
        print(f"Felicidades, gana el jugador {numero}.")  # Si no quedan barcos, el jugador gana.
        return 0,0
    else:
        return 1,1


def main() -> None:
    """
    Función principal.
    """
    opcion = None

    while opcion != 0:
        print()
        opcion = menu() # Muestra el menú y obtiene la opción del usuario.

        # Inicialización de variables y estructuras del juego.
        posiciones_del_jugador_1 = []  # Lista que almacenará las posiciones de los barcos del jugador 1.
        posiciones_del_jugador_2 = []  # Lista que almacenará las posiciones de los barcos del jugador 2.
        tablero_1 = ["~"] * 100  # Tablero del jugador 1 con agua inicialmente.
        tablero_2 = ["~"] * 100  # Tablero del jugador 2 con agua inicialmente.
        contador = 0  # Contador para la colocación de barcos.
        detener = None  # Variable de control para verificar si el juego debe continuar.
        bandera = None  # Variable de control para manejar los turnos de los jugadores.

        print()

        if opcion == 0:
            print("Fin del programa.")
        elif opcion == 1:
            print("Fase de preparación")
            # Solicita el número de barcos a los jugadores.
            num_de_barcos = input("Ingrese el número de barcos (el limite es de 70 barcos): ")
            num_de_barcos = verificar(num_de_barcos)
            contador_del_jugador_1 = 0
            contador_del_jugador_2 = 0

            # Verifica que el número de barcos esté dentro del rango permitido.
            while not (num_de_barcos >= 1 and num_de_barcos <= 70):
                print("Opción invalida.")
                print("___________________________________________________________________")
                num_de_barcos = input("Intenta nuevamente: ")
                num_de_barcos = verificar(num_de_barcos)
                print()

            # Despliegue de los barcos en los tableros de los jugadores.
            print("Despliegue de barcos del jugador 1:")
            posiciones_del_jugador_1 = desplegar_barcos(num_de_barcos)
            print("Despliegue de barcos del jugador 2:")
            posiciones_del_jugador_2 = desplegar_barcos(num_de_barcos)

            # Asignar los barcos en los tableros.
            while contador < num_de_barcos:
                indice = posiciones_del_jugador_1[contador + 1 * contador] * 10 + posiciones_del_jugador_1[contador + 1 + 1 * contador]
                tablero_1[indice] = "⛴"
                indice = posiciones_del_jugador_2[contador + 1 * contador] * 10 + posiciones_del_jugador_2[contador + 1 + 1 * contador]
                tablero_2[indice] = "⛴"
                contador += 1
            print()
            print("Comienza el juego.")
            while detener != 0 and contador_del_jugador_1 < num_de_barcos and contador_del_jugador_1 < num_de_barcos:

                while bandera != 0 and contador_del_jugador_1 < num_de_barcos:
                    print("Turno del jugador 1")
                    fila = input("Fila: ")
                    fila = verificar(fila)
                    columna = input("Columna: ")
                    columna = verificar(columna)
                    # Válida que la coordenada ingresada esté dentro del tablero.
                    while not (0 <= columna <= 9) and not (0 <= fila <= 9):
                        print("la coordenadas son diferentes al tablero.")
                        print("___________________________________________________________________")
                        print("Intente nuevamente.")
                        columna = input("Columna: ")
                        columna = verificar(columna)
                        fila = input("Fila: ")
                        fila = verificar(fila)

                    indice = fila * 10 + columna
                    # Verifica si el disparo impactó un barco.
                    if tablero_2[indice] == "⛴":
                        print(TOCADO)  # Mensaje de impacto.
                        print("___________________________________________________________________")
                        tablero_2[indice] = "~"
                        mostrar_barcos(indice)
                        bandera = 1
                        contador_del_jugador_1 += 1
                        print()

                    else:
                        print(AGUA)  # Mensaje de fallo en el disparo.
                        print("___________________________________________________________________")
                        bandera = 0

                print()

                detener,bandera = ganador(tablero_2,1) # Verifica si el jugador 1 ha ganado.

                while bandera != 0 and contador_del_jugador_2 < num_de_barcos:
                    print("Turno del jugador 2")
                    fila = input("Fila: ")
                    fila = verificar(fila)
                    columna = input("Columna: ")
                    columna = verificar(columna)
                    # Válida que la coordenada ingresada esté dentro del tablero.
                    while not (0 <= columna <= 9) and not (0 <= fila <= 9):
                        print("la coordenadas son diferentes al tablero.")
                        print("___________________________________________________________________")
                        print("Intente nuevamente.")
                        columna = input("Columna: ")
                        columna = verificar(columna)
                        fila = input("Fila: ")
                        fila = verificar(fila)

                    indice = fila * 10 + columna
                    # Verifica si el disparo impactó un barco.
                    if tablero_1[indice] == "⛴":
                        print(TOCADO)
                        print("___________________________________________________________________")
                        mostrar_barcos(indice)
                        tablero_1[indice] = "~"
                        bandera = 1
                        contador_del_jugador_2 += 1
                        print()
                    else:
                        print(AGUA) # Mensaje de falló en el disparo.
                        print("___________________________________________________________________")
                        bandera = 0 # Finaliza el turno del jugador 2.
                        print()
                detener, bandera = ganador(tablero_1, 2) # Verifica si el jugador 2 ha ganado.
                print()


        else:
            print("La batalla naval es un emocionante juego de estrategia y deducción que simula un combate naval entre dos jugadores. ")
            print("Cada jugador despliega secretamente su flota de barcos en un tablero cuadriculado que representa el océano.")
            print("El objetivo del juego es hundir todos los barcos del oponente antes de que él hunda los tuyos. Los jugadores se turnan")
            print("para disparar  a una casilla del tablero del oponente, anunciando las coordenadas de la casilla elegida (por ejemplo, 6,4).")
            print("El oponente responde si el disparo ha alcanzado uno de sus barcos (Tocado) o si ha caído al agua (Agua).")
            print("Si el disparo toca un barco, el jugador que dispara tiene derecho a seguir disparando hasta fallar. El objetivo es acertar ")
            print("todas las casillas que ocupa un barco para hundirlo por completo.")
        print("_________________________________________________________________________________________________________________________________")


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()