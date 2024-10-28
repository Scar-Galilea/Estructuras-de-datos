#Galilea Peralta Contreras.
#28 de octubre de 2024.
#Descripción:
#Programa para calcular el costo de un tour turístico de acuerdo con el número de adultos, niños y el día de la visita.

"""
Escribe un programa de nombre Sentencias_ejercicio6.py que realice lo siguiente:

Este programa mostrará los detalles del tour turístico Ecoturixtlán de acuerdo a las siguientes tarifas:

Precio de un adulto: $ 200.00
Precio de un niño: $ 100.00
Además, si la visita son los lunes, martes y jueves, se tiene un descuento del 10 %.

Para ello:

a) Solicite al usuario el nombre de la persona a cargo.

b) Defina con valores constantes el precio del boleto del adulto y del niño.

c) Solicite el número de adultos y de niños.

d) Pregunte el día de la semana.

e) Calcule el costo total.

f) Muestre los detalles del cliente y el día, así como el costo total.

"""

print("*** Tour turístico Ecoturixtlán ***")
# Entrada de datos
Variable_1 = input("Ingresa el nombre del cliente: ")
Variable_2 = input("Ingresa el número de adultos: ")
Variable_3 = input("Ingresa el número de niños: ")
Variable_4 = input("Ingresa el día de la semana: ")

Variable_2 = int(Variable_2)
Variable_3 = int(Variable_3)

Variable_4 = Variable_4.lower()

# Cálculo del total
Total = (Variable_2 * 200) + (Variable_3 * 100)

print()
# Aplicación del descuento si corresponde
if Variable_4 == "lunes"  or Variable_4 == "martes" or Variable_4 == "jueves":
    Total = Total - (Total * 0.1)
    print(f"Gracias por su visita {Variable_1} este día {Variable_4}. El costo total es de {Total:.2f}.")
else:
    print(f"Gracias por su visita {Variable_1} este día {Variable_4}.El costo total es de {Total:.2f}.")

