#Galilea Peralta Contreras.
#16 de octubre de 2024.
#Descripción:
#Ejemplos de uso de los operadores de asignación compuestos.

"""
Los operadores de asignación compuestos son una forma abreviada de realizar una operación aritmética y una asignación
en una sola línea de código. Combinan un operador aritmético (como suma, resta, multiplicación, división, etc.)
con el operador de asignación (=).
"""
# Se solicita un número para realizar diferentes operaciones de asignación compuestas.
Variable_1= input("Ingrese un número: ")
Variable_1=int(Variable_1)

Variable_2= input("Ingrese un número: ")
Variable_2=int(Variable_2)

Variable_1 += 3 #Equivale a Variable_1 = Variable_1 + 3.
Variable_2 -= 5 #Equivale a Variable_1 = Variable_2 - 5.
Variable_1 *= 2 #Equivale a Variable_1 = Variable_1 * 2.
Variable_2 /= 4 #Equivale a Variable_1 = Variable_2 / 3.

print(f"El resultado del número 1 es: {Variable_1} y del número 2 es {Variable_2}.")

print()
Variable_1= input("Ingrese un número: ")
Variable_1=int(Variable_1)

Variable_2= input("Ingrese un número: ")
Variable_2=int(Variable_2)

Variable_1 += Variable_2 #Equivale a Variable_1 = Variable_1 + Variable_2.
Variable_1 *= Variable_1 #Equivale a Variable_1 = Variable_1 * Variable_1.
Variable_1 -= Variable_2 #Equivale a Variable_1 = Variable_1 - Variable_2.
Variable_1 += 3 #Equivale a Variable_1 = Variable_1 + 3.
Variable_1 /= 2 #Equivale a Variable_1 = Variable_1 / 2.

print(f"El resultado del número 1 es: {Variable_1} y del número 2 es {Variable_2}.")















