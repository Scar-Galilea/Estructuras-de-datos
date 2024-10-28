#Galilea Peralta Contreras.
#16 de octubre de 2024.
#Descripción:
#Sistema de  bonificación.

#Escribe un programa de nombre Operadores_ejercicio1.py que realice lo siguiente:

#Este programa determinará si el usuario aplica para una bonificación. Para ello:
#a) Solicite al usuario un número decimal con el valor de una compra.
#b) Pregunte al usuario si la compra fue a MSI (Si/No).
#c) El usuario aplica a la bonificación si la compra fue mayor a 5000.00 y si la compra fue a MSI.
#d) Muestre el resultado en consola como valor booleano (True/False).

print("*** Sistema de bonificación ***")
Variable_1 = input("Ingresa la cantidad de su compra: ")
Variable_2 = input("Compras a meses sin intereses: ")

Variable_1 = float(Variable_1)
#Se Converte la respuesta a booleano: será True si es "si" (sin importar mayúsculas/minúsculas) y False en otros casos.
Variable_2 =  Variable_2.lower()=="si"


print(f"¿Aplica bonificación? {Variable_1 >= 5000 and Variable_2}")
