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
repetidos = 0

Tema = None
Contador = 0

print("Este es un juego que se puede jugar de manera grupal, en donde")
print("el objetivo es decir palabras de un tema en específico y ")
print("los jugadores deben tratar de no repetir la misma palabra.")
print()

Tema = input("Ingresa el tema del juego: ")

while repetidos == 0:
    Palabras = input(f"Ingresa la palabra {Contador} del tema de {Tema}: ")
    Palabras = Palabras.lower()
    for Conjunto_de_palabra in Conjuntos_de_palabras:
        if Conjunto_de_palabra == Palabras:
            repetidos = 1

    Conjuntos_de_palabras.add(Palabras)
    Contador += 1

print(f"!El juego ha terminado! Has dicho {Contador-1} palabras diferentes.")
print(f"Las palabras del tema {Tema} fueron: {Conjuntos_de_palabras}")