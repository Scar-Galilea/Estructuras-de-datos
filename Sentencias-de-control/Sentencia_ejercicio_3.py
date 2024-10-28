#Galilea Peralta Contreras.
#28 de octubre de 2024.
#Descripción:
# Programa para calcular descuentos en "La Cona" basados en la membresía y monto de compra.

"""
Escribe un programa de nombre Sentencias_ejercicio3.py que realice lo siguiente:

Este programa determinará un descuento en compras en "La cona", de acuerdo a lo siguiente:

Si tiene membresía, obtiene un 5 % de descuento en todas sus compras.
Si tiene la membresía y su compra fue mayor o igual a $ 1000.00, entonces el descuento es del 8 %.
Si no tiene la membresía, no obtiene ningún descuento y se invita a ser miembro.
Para ello:

a) Solicite al usuario la cantidad comprada en la tienda.

b) Pregunte al usuario si cuenta con la membresía (Si/No).

c) Utilice la lógica adecuada para determinar el total a pagar.

d) Muestre el descuento y el total a pagar en consola utilizando dos decimales.

"""
print("*** Descuento por ser miembro de La Cona ***")
Variable_1 = input("Ingrese la cantidad de su cantidad de su compra: ")
Variable_1 = float(Variable_1)

# Verificar si el usuario tiene membresía.
Variable_2 = input("¿Cuenta con la membresía? ")
Variable_2 = Variable_2.lower() == "si"

print()
Total = Variable_1
# Calcula el descuento y el total de acuerdo a las condiciones
if Variable_2 == True and Variable_1 < 1000:
    print("Descuento es del 5%.")
    print(f"Su total es de {Variable_1 - (Variable_1 * 0.05) :.2f}.")

elif Variable_2 == True and Variable_1 >= 1000:
    print("Descuento es del 8%.")
    print(f"Su total es de {Variable_1 - (Variable_1 * 0.08) :.2f}.")

else:
    print("Se te invita a ser miembro de la tienda para obtener un descuento hasta del 8%")
    print(f"Su total es de {Variable_1 :.2f}.")