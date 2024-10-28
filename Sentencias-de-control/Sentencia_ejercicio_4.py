#Galilea Peralta Contreras.
#28 de octubre de 2024.
#Descripción:
# Programa para verificar el acceso al bar "La Negra" según la edad y el presupuesto del usuario.

"""
Escribe un programa de nombre Sentencias_ejercicio4.py que realice lo siguiente:

Este programa determinará si te permiten el acceso al bar "La Negra", por lo que se debe cumplir lo siguiente:

Tener al menos 18 años.
Tener al menos $ 250.00 para gastar.
Si ambas condiciones se cumplen, se imprime el mensaje en consola: "¡Bienvenido a tu mejor bar!". En caso contrario, se imprime: "Lo sentimos, ya estamos por cerrar!"

Para ello:

a) Solicite al usuario su edad.

b) Solicite al usuario el dinero con el que cuenta.

c) Utilice la lógica adecuada para determinar el mensaje.

d) Muestre el mensaje adecuado en consola.

"""
print("*** Acceso al bar 'La Negra' ***")
Variable_1 = input("Ingresa su edad: ")
Variable_2 = input("Ingresa su prosupuesto: ")

Variable_1 = int(Variable_1)
Variable_2 = float(Variable_2)

print()
# Verificación de las condiciones de acceso
if Variable_1 >= 18 and Variable_2 >= 300:
    print("¡Bienvenido a tu mejor bar!")
else:
    print("Lo sentimos, ya estamos por cerrar!")
