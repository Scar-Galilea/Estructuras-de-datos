#Galilea Peralta Contreras.
#16 de octubre de 2024.
#Descripción:
#Usos de los tipos básico de datos en Python.

Variable_1 = input("Ingresa la cantidad de su compra: ")
Variable_2 = input("Compras a meses sin intereses: ")

Variable_1 = float(Variable_1)
Variable_2 =  Variable_2.lower()=="no"


print(f"¿Aplica bonificación? {Variable_1 >= 5000 and Variable_2}")
