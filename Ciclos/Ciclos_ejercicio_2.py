#Galilea Peralta Contreras.
#28 de octubre de 2024.
#Descripción:
#Usos de los tipos básico de datos en Python.

print()
print("*** Programa que calcula la suma acumulativa entre dos números **+")
Variable_1 = input("Ingrese el número inicial: ")
Variable_2 = input("Ingrese el número final: ")

Variable_1 = int(Variable_1)
Variable_2 = int(Variable_2)

Contador_1 = Variable_1
Total = 0

while Contador_1 <= Variable_2 :
    Total += Contador_1
    Contador_1 += 1

print(f"La suma del {Variable_1} al {Variable_2} son: {Total}")


