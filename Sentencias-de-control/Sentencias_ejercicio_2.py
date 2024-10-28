#Galilea Peralta Contreras.
#28 de octubre de 2024.
#Descripción:
#Usos de los tipos básico de datos en Python.
#Ejercicio.

"""
Este programa determinará la estación del año de acuerdo al número de mes ingresado por el usuario. Para ello:

a) Solicite al usuario un número que representa al mes.

b) Utilice la lógica adecuada para determinar la estación del año de acuerdo con:

    3, 4 y 5: Primavera.

    6, 7 y 8: Verano.

    9,10 y 11: Otoño.

    12, 1 y 2: Invierno.

    Otro caso: Mensaje de mes incorrecto.

c) Muestre la estación correspondiente en consola.
"""
print("*** Programa que determine la estacion del año ***")
Variable_1 = input("Ingresa el numero del mes: ")
Variable_1 = int(Variable_1)

print()
if Variable_1 == 3 or Variable_1 == 4 or Variable_1 == 5:
    print("La estación es: Primavera.")
elif Variable_1 == 6 or Variable_1 == 7 or Variable_1 == 8:
    print("La estación es: Primavera.")
elif Variable_1 == 9 or Variable_1 == 10 or Variable_1 == 11:
    print("La estación es: Otoño.")
elif Variable_1 == 12 or Variable_1 == 1 or Variable_1 == 2:
    print("La estación es: Invierno.")
else:
    print("Mensaje del mes incorrecto.")