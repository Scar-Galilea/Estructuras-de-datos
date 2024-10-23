#Galilea Peralta Contreras.
#23 de octubre de 2024.
#Descripción:
#Usos de los tipos básico de datos en Python.
#Se utilizan para comparar dos valores

#Código a ejecutar si la condición es verdadera

print("*** Programa que determina si un número es par o impar +++")

Variable_1 = input("Ingresa un número: ")
Variable_1 = int(Variable_1)

if Variable_1 %2 == 0:
    print(f"El número {Variable_1} es par ")
else:
    print(f"El número {Variable_1} es impar")