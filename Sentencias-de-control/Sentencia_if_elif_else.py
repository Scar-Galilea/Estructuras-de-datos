#Galilea Peralta Contreras.
#23 de octubre de 2024.
#Descripción:
#Usos de los tipos básico de datos en Python.
#Uso de la sentencia de control if - elif - else.

"""
La sentencia elif es una extensión del if-else y permite evaluar múltiples condiciones de forma secuencial.
Es como tener varias opciones a elegir, ejecutándose el bloque de código correspondiente a la primera condición
que sea verdadera.

Sintaxis:

if condicion_1:
    # Código a ejecutar si la condición_1 es verdadera.

elif condición_2:
    # Código a ejecutar si la condición_2 es verdadera.
  .
  .
  .
else:
    # Código que se ejecuta si todas las condiciones fueron falsas.
"""

#Ejemplo que determina el grupo al que pertenece de acuerdo a su edad.
print("*** Programa que grupo de edad pertenece ***")

Variable_1 = input("Ingresa su edad: ")
Variable_1 = int(Variable_1)

#Lógica para determinar el grupo usando la estrucutra if-elif-else.
if Variable_1 <= 14:
    print(f"la edad de {Variable_1} pertenece al grupo de niños y adolecentes")

elif Variable_1 >= 15 and Variable_1 <= 25:
    print(f"la edad de {Variable_1} pertenece al grupo de jóvenes")

elif Variable_1 >= 26 and Variable_1 <= 45:
    print(f"la edad de {Variable_1} pertenece al grupo de adultos jóvenes")

elif Variable_1 >= 46 and Variable_1 <= 60:
    print(f"la edad de {Variable_1} pertenece al grupo de adultos maduros")

else:
    print(f"la edad de {Variable_1} pertenece al grupo de mayores")

