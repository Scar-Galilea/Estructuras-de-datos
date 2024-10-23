#Galilea Peralta Contreras.
#14 de octubre de 2024.
#Descripción:
#Ejercicios.

#Escribe un programa de nombre Entrada_conversiones_ejercicio.py que realice lo siguiente:
#a) Pida los datos de los profesores utilizando nombres de variables adecuadas, la función input y el casting:

#Nombre (cadena).
Variable_1 = input("Ingrese nombre: ")

#No. de cubículo (int).
Variable_2 = input(" Ingrese el No. de cubículo: ")
# Primero se captura como cadena y luego se convierte a entero usando int().
Variable_2 = int(Variable_2)

#Horas en que imparte clase a la semana (float con 3 decimales).
Variable_3 = input("Ingrese las horas de que imparte clases a la semana: ")
# El casting convierte la entrada a float para permitir decimales.
Variable_3 = float(Variable_2)

#¿Tiene más de 5 años en la UNSIJ? (booleno).
Variable_4 = input("¿Tiene más de 5 años en la UNSIJ? ")
Variable_4 = Variable_4.lower() == "Si"


#b) Muestre los datos en consola de forma adecuada.
print()
print("Nombre: ", Variable_1)
print("No. de cubículo: ", Variable_2)
print("Horas de que imparte clases a la semana: ", Variable_3)
print("¿Tiene más de 5 años en la UNSIJ? ", Variable_4)