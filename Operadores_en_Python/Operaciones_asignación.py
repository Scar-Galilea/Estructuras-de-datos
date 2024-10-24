#Galilea Peralta Contreras.
#15 de octubre de 2024.
#Descripción:
#Ejemplos de uso de los operadores de asignación.

"""
En programación, las operaciones de asignación se utilizan para almacenar un valor en una variable.
Es decir, se establece una relación entre un nombre (la variable) y un valor en la memoria de la computadora.
"""

# Asignación multiple
print("   ***   Asignación múltiple   ***")
Variable_1,Variable_2 = 5,10 #Equivale a Variable_1 = 5 y en otra linea Variable_2 = 10 .
Variable_3,Variable_4 = 9.14,"Galilea" #Equivale a Variable_3 = 9.14 y en otra linea Variable_4 = "Galilea".
print(Variable_1)
print(Variable_2)
print(Variable_3)
print(Variable_4)
Variable_5,Variable_6 = Variable_1 + Variable_2,Variable_1 - Variable_2 #Equivale a Variable_5 = Variable_1 + Variable 2.
#En otra linea equivale igual Variable_6 = Variable_1 - Variable_2.
print(Variable_5)
print(Variable_6)

#Asignacion encadenada
print()
print("   ***   Asignación encadenada  ***")
Variable_7 = Variable_8 = Variable_9 = 10
print(Variable_7)
print(Variable_8)
print(Variable_9)

#Intercambio de variables
print()
print("   ***   Intercambio de variables  ***")
Variable_10,Variable_11 = "Scarlett" , "Ana"
print(Variable_10)
print(Variable_11)
Variable_10 , Variable_11 = Variable_11 , Variable_10 #Es una forma de intercambiar las variables.
print(Variable_10)
print(Variable_11)

#Nombre = input("Ingrese nombre: ")
#Apellido = input("Ingrese apellido: ")
Nombre , Apellido = input("Ingrese nombre") , input("Ingrese apellido") #Es otra manera de pedir datos del usuario.
print(Nombre,Apellido)






