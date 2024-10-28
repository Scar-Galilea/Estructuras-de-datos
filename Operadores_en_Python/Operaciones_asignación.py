#Galilea Peralta Contreras.
#15 de octubre de 2024.
#Descripción:
#Ejemplos de uso de los operadores de asignación.

"""
En programación, las operaciones de asignación se utilizan para almacenar un valor en una variable.
Es decir, se establece una relación entre un nombre (la variable) y un valor en la memoria de la computadora.
"""

# Asignación múltiple:
print("   ***   Asignación múltiple   ***")
# Aquí se asignan valores a dos variables en una sola línea.
Variable_1,Variable_2 = 5,10 #Equivale a Variable_1 = 5 y en otra línea Variable_2 = 10 .
Variable_3,Variable_4 = 9.14,"Galilea" #Equivale a Variable_3 = 9.14 y en otra línea Variable_4 = "Galilea".
print(Variable_1) #Imprime 5.
print(Variable_2) #Imprime 10.
print(Variable_3) #Imprime 9.14.
print(Variable_4) # Imprime "Galilea"

# Calcula el valor de la suma y resta y lo asigna a dos variables en una sola línea.
Variable_5,Variable_6 = Variable_1 + Variable_2,Variable_1 - Variable_2 #Equivale a Variable_5 = Variable_1 + Variable 2.
print(Variable_5)
print(Variable_6)

#Asignacion encadenada:
print()
print("   ***   Asignación encadenada  ***")
# Asigna el mismo valor (10) a tres variables en una sola línea.
# Es una forma eficiente de inicializar múltiples variables con el mismo valor.
Variable_7 = Variable_8 = Variable_9 = 10
print(Variable_7)
print(Variable_8)
print(Variable_9)

#Intercambio de variables:
print()
print("   ***   Intercambio de variables  ***")
Variable_10,Variable_11 = "Scarlett" , "Ana"
print(Variable_10)
print(Variable_11)
# Intercambia los valores de las variables en una sola línea.
# Esta técnica es útil para reorganizar datos sin una variable temporal.
Variable_10 , Variable_11 = Variable_11 , Variable_10
print(Variable_10)
print(Variable_11)

#Nombre = input("Ingrese nombre: ")
#Apellido = input("Ingrese apellido: ")
Nombre , Apellido = input("Ingrese nombre") , input("Ingrese apellido") #Es otra manera de pedir datos del usuario.
print(Nombre,Apellido)






