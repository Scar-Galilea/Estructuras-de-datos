#Galilea Peralta Contreras.
#15 de octubre de 2024.
#Descripción:
#Usos de los tipos básico de datos en Python. Corregir

Variable_1,Variable_2=5,10
Variable_3,Variable_4=9.14,"Galilea"
#asignación multiple

print(Variable_1)
print(Variable_2)
print(Variable_3)
print(Variable_4)

Variable_5,Variable_6 = Variable_1 + Variable_2,Variable_1 - Variable_2
print(Variable_5)
print(Variable_6)

#Asignacion encadenada
print()
Variable_7 = Variable_8 = Variable_9 = 10
print(Variable_7)
print(Variable_8)
print(Variable_9)

#Intercambio de variables
print()
Variable_10,Variable_11 = "Scarlett" , "Ana"
print(Variable_10)
print(Variable_11)
Variable_10 , Variable_11 = Variable_11 , Variable_10
print(Variable_10)
print(Variable_11)

Nombre = input("Ingrese nombre: ")
Apellido = input("Ingrese apellido: ")

Nombre , Apellido = input("Ingrese nombre") , input("Ingrese apellido")
print(Nombre,Apellido)




