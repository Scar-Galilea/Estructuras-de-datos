#Galilea Peralta Contreras.
#07 de noviembre de 2024.
#Descripción:
#Este programa imprime una pirámide de caracteres '*' en cuatro formas diferentes según la cantidad de filas.

"""
Escribe un programa de nombre Ciclos_ej5_piramide.py que realice lo siguiente:
Este programa imprime una pirámide de caracteres '*' de cuatro formas:
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

En donde el usuario ingresa el número de filas. Para ello:
a) Solicite el número de filas de la pirámide.
b) Muestre los tres tipos de pirámides utilizando la lógica adecuada.

"""
#Solicitar al usuario el número de filas para las pirámides.
Numero_de_filas = int(input("Ingrese el número de filas: "))

print()
print("Forma 1:")
for j in range (1,Numero_de_filas + 1):
    asteriscos = "*" * j
    print(f"{asteriscos}")
print("________________________________________________________________")

print()
print("Forma 2:")
contador = Numero_de_filas
for i in range (1,Numero_de_filas + 1):
    asteriscos = "*" * contador
    print(f"{asteriscos}")
    contador -= 1
print("________________________________________________________________")

print()
print("Forma 3:")
contador = Numero_de_filas
contador_2 = 0
for m in range (1,Numero_de_filas + 1):
    espacio = " " * contador
    asteriscos = "*" * (m + contador_2)
    print(f"{espacio}{asteriscos}")
    contador -= 1
    contador_2 += 1
print("________________________________________________________________")


print()
print("Forma 4:")
contador = Numero_de_filas
contador_2 = 0
for m in range (1,Numero_de_filas + 1):
    espacio = " " * contador
    asteriscos = "*" * m
    print(f"{espacio}{asteriscos}")
    contador -= 1
    contador_2 += 1
print("________________________________________________________________")

