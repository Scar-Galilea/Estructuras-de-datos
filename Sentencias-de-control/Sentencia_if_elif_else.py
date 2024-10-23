#Galilea Peralta Contreras.
#23 de octubre de 2024.
#Descripción:
#Usos de los tipos básico de datos en Python.
#Se utilizan para comparar dos valores

#Código a ejecutar si la condición es verdadera

print("*** Programa que grupo de edad pertenece ***")

Variable_1 = input("Ingresa su edad: ")
Variable_1 = int(Variable_1)

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

