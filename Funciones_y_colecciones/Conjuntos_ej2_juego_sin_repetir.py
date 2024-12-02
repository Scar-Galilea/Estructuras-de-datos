#Galilea Peralta Contreras.
#28 de noviembre del 2024.
#Descripción:
#Este programa es un juego grupal en el que los jugadores dicen palabras relacionadas con un tema específico.
#El objetivo es no repetir palabras ya dichas.

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

#Se inicializa un conjunto para almacenar las palabras ingresadas sin repetición.
Conjuntos_de_palabras = set()
#Variable para controlar si se detectan palabras repetidas.
Repetidos = 0

#Variable para almacenar el tema del juego.
Tema = None
#Contador para llevar el registro de la cantidad de palabras ingresadas.
Contador = 0

#Mensaje introductorio con las reglas del juego.
print("Este es un juego que se puede jugar de manera grupal, en donde")
print("el objetivo es decir palabras de un tema en específico y ")
print("los jugadores deben tratar de no repetir la misma palabra.")
print()

#Solicita al usuario que ingrese el tema del juego.
Tema = input("Ingresa el tema del juego: ")

#Ciclo principal del juego.
#Continúa mientras no se detecten palabras repetidas.
while Repetidos == 0:
    #Solicita al usuario que ingrese una palabra y la convierte a minúsculas para evitar errores por mayúsculas.
    Palabras = input(f"Ingresa la palabra {Contador} del tema de {Tema}: ")
    Palabras = Palabras.lower()
    #Verifica si la palabra ya se encuentra en el conjunto.
    for Conjunto_de_palabra in Conjuntos_de_palabras:
        if Conjunto_de_palabra == Palabras:
            Repetidos = 1 #Cambia el valor para parar el ciclo si hay una palabra repetida.


    Conjuntos_de_palabras.add(Palabras)
    #Incrementa el contador de palabras.
    Contador += 1

#Mensaje final indicando que el juego ha terminado.
print(f"!El juego ha terminado! Has dicho {Contador-1} palabras diferentes.")
print(f"Las palabras del tema {Tema} fueron: {Conjuntos_de_palabras}")
print("______________________________________________________")