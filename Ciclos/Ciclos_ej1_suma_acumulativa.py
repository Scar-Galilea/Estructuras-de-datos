#Galilea Peralta Contreras.
#28 de octubre de 2024.
#Descripción:
#Este programa calcula la suma acumulativa desde 0 hasta un número ingresado por el usuario.
"""
Escribe un programa de nombre Ciclos_ej1_suma_acumulativa.py que realice lo siguiente:

Este programa calculará la suma acumulativa del cero hasta un número ingresado por el usuario. Para ello:

a) Solicite al usuario un número mayor a cero que será el número hasta donde se realizará la suma.

b) Calcule la suma acumulativa.

c) Muestre el resultado de la suma.
"""
print("*** Programa que calcula la suma acumulativa. ***")
#Solicitar al usuario el número final.
Numero_final = input("Ingrese el número final: ")
Numero_final = int(Numero_final)

#Variables para el cálculo de la suma acumulativa.
Contador_1 = 0 #Contador que inicia en 0.
Total = 0  #Variable para acumular la suma.

#Ciclo que calcula la suma acumulativa desde 0 hasta el número ingresado.
while Contador_1 <= Numero_final :
    Total += Contador_1   #Sumar el contador al total
    Contador_1 += 1       #Incrementar el contador en 1

print()
#Mostrar el resultado de la suma acumulativa
print(f"La suma del 0 al {Numero_final} son: {Total}.")


