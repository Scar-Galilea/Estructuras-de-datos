#Galilea Peralta Contreras.
#23 de octubre de 2024.
#Descripción:
#Uso de la sentencia de control if.

"""
La sentencia de control if es una estructura de control fundamental que permite ejecutar diferentes bloques de código
 dependiendo de si una condición se cumple o no.

Sintaxis:

if condición:
    # Código a ejecutar si la condición es verdadera. Notar que hay que dejar un espacio de tabulador.

# Código que se continúa ejecutando. Notar que ya no hay espacio y está a la misma altura que el if.
"""


# Ejemplo en donde se imprime un mensaje si el usuario tiene la mayoría de edad.
print("*** Programa que determina si es mayor de edad +++")

Variable_1 = input("Ingresa tu edad: ")
Variable_1 = int(Variable_1)
if Variable_1 >= 18 :

# Código a ejecutar si la condición es verdadera
    print("Eres mayor de edad")

# Probar qué pasa con espacios simples, no dejando una línea entre ambas funciones print()
# y que ambos print() se encuentren a la misma altura.
