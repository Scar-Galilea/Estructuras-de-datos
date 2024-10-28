#Galilea Peralta Contreras.
#28 de octubre de 2024.
#Descripción:
#Expresión booleana (exp1) o (exp2) y (exp3) o (exp4).

#Escribe un programa de nombre Operadores_ejercicio4.py que realice lo siguiente:
#Este programa determinará True o False de acuerdo a la expresión (exp1 O exp2) Y (exp3 O exp4). Para ello:
#a) Pida al usuario cuatro valores booleanos (V/F).
#a) Pida al usuario cuatro valores booleanos (V/F).
#b) Obtenga el resultado de la expresión booleana de acuerdo con los valores ingresados.
#c) Muestre el resultado en consola como valor booleano (True/False).

print("*** Expresión booleana (exp1) o (exp2) y (exp3) o (exp4) ***")

Expresión_1 = input("Ingrese valor booleano (V/F): ")
Expresión_2 = input("Ingrese valor booleano (V/F): ")
Expresión_3 = input("Ingrese valor booleano (V/F): ")
Expresión_4 = input("Ingrese valor booleano (V/F): ")

Expresión_1 = Expresión_1.lower() == "v"
Expresión_2 = Expresión_2.lower() == "v"
Expresión_3 = Expresión_3.lower() == "v"
Expresión_4 = Expresión_4.lower() == "v"

print(f"El resultado de la expresión booleana es: {(Expresión_1 or Expresión_2) and (Expresión_3 or Expresión_4) }")