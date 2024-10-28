#Galilea Peralta Contreras.
#28 de octubre de 2024.
#Descripción:
# Programa para calcular el promedio de una materia y determinar si el alumno aprobó.

"""
Escribe un programa de nombre Sentencias_ejercicio5.py que realice lo siguiente:

Este programa determinará el promedio de una materia e indicará si el alumno aprobó o no la materia.

Si ambas condiciones se cumplen, se imprime el mensaje en consola: "¡Bienvenido a tu mejor bar!". En caso contrario, se imprime: "Lo sentimos, ya estamos por cerrar!"

Para ello:

a) Solicite al usuario sus tres calificaciones parciales y la calificación del ordinario.

b) Calcule el promedio y determine si aprobó (calificación mínima de 6.0).

d) Muestre el promedio (utilizando un decimal) y el mensaje: "¡Felicidades! Aprobaste.", o el mensaje: "Lo siento, no aprobaste.", según sea el caso.



"""
print("*** Programa para calcular el promedio  de una materia ***")
Variable_1 = input("Ingresa su calificación del parcial 1: ")
Variable_2 = input("Ingresa su calificación del parcial 2: ")
Variable_3 = input("Ingresa su calificación del parcial 3: ")
Variable_4 = input("Ingresa su calificación del Ordinario: ")

Variable_1 = float(Variable_1)
Variable_2 = float(Variable_2)
Variable_3 = float(Variable_3)
Variable_4 = float(Variable_4)

# Cálculo del promedio.
Promedio = (((Variable_1 + Variable_2 + Variable_3) / 3) * 0.5) + (Variable_4 * 0.5)

print()
# Verificación de aprobación
if Promedio >= 6.0:
    print(f"La calificación final es de: {Promedio :.1f}. ¡Felicidades! Aprobaste.")
else:
    print(f"La calificación final es de: {Promedio :.1f}. Lo siento, no aprobaste.")

