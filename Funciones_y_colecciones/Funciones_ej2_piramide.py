#Galilea Peralta Contreras.
#25 de noviembre del 2024.
#Descripción:
#Usos de los tipos básico de datos en Python

"""
Escribe un programa de nombre Funciones_ej2_piramide.py que realice lo siguiente:
Este programa imprime una pirámide de caracteres '*' de cuatro formas y es la versión del ejercicio Ciclos_ej5_piramide.py, pero ahora utilizando funciones.
Cada pirámide debe estar en una función, la cual se llama en el código a nivel de módulo de acuerdo a las filas requeridas por el usuario.

1)
*
**
***

2)
***
**
*

3)
  *
 ***
*****

4)
  *
 **
***


Para ello:
a) Solicite el número de filas de la pirámide en el código a nivel de módulo.
b) Defina una función para cada pirámide, recibiendo el número de filas como parámetro.
"""
def Forma_1(Numero_de_filas):
    print()
    print("Forma 1:")
    for j in range(1, Numero_de_filas + 1):
        asteriscos = "*" * j
        print(f"{asteriscos}")
    print("________________________________________________________________")

def Forma_2(Numero_de_filas):
    print()
    print("Forma 2:")
    contador = Numero_de_filas
    for i in range(1, Numero_de_filas + 1):
        asteriscos = "*" * contador
        print(f"{asteriscos}")
        contador -= 1
    print("________________________________________________________________")

def Forma_3(Numero_de_filas):
    print()
    print("Forma 3:")
    contador = Numero_de_filas
    contador_2 = 0
    for m in range(1, Numero_de_filas + 1):
        espacio = " " * contador
        asteriscos = "*" * (m + contador_2)
        print(f"{espacio}{asteriscos}")
        contador -= 1
        contador_2 += 1
    print("________________________________________________________________")

def Forma_4(Numero_de_filas):
    print()
    print("Forma 4:")
    contador = Numero_de_filas
    contador_2 = 0
    for m in range(1, Numero_de_filas + 1):
        espacio = " " * contador
        asteriscos = "*" * m
        print(f"{espacio}{asteriscos}")
        contador -= 1
        contador_2 += 1
    print("________________________________________________________________")


Numero_de_filas = int(input("Ingrese el número de filas: "))
Forma_1(Numero_de_filas)
Forma_2(Numero_de_filas)
Forma_3(Numero_de_filas)
Forma_4(Numero_de_filas)

