#Galilea Peralta Contreras.
#28 de octubre de 2024.
#Descripción:
#Este programa calcula la suma acumulativa entre dos números ingresados por el usuario.

"""
Escribe un programa de nombre Ciclos_ej2_suma_acumulativa_v2.py que realice lo siguiente:

Este programa calculará la suma acumulativa de dos números ingresados por el usuario.

A diferencia del programa anterior, ahora el usuario también definirá el número inicial. Para ello:
a) Solicite al usuario los números inicial y final de la suma acumulativa.
b) Calcule la suma acumulativa entre ambos números.
c) Muestre el resultado de la suma.
"""

print("*** Programa que calcula la suma acumulativa entre dos números. ***")

#Solicitar al usuario los números inicial y final.
Numero_inicial = input("Ingrese el número inicial de la cuenta: ")
Numero_final = input("Ingrese el número final de la cuenta: ")

Numero_inicial = int(Numero_inicial)
Numero_final = int(Numero_final)

#Inicializar el contador y la variable para acumular la suma.
Contador_1 = Numero_inicial  #Inicia en el número definido por el usuario.
Total = 0  #Variable para almacenar la suma acumulativa.

#Ciclo que calcula la suma acumulativa entre los números ingresados.
while Contador_1 <= Numero_final:
    Total += Contador_1  #Agregar el valor actual del contador al total.
    Contador_1 += 1      #Incrementar el contador.

# Mostrar el resultado de la suma acumulativa
print()
print(f"La suma del {Numero_inicial} al {Numero_final} es: {Total}.")

