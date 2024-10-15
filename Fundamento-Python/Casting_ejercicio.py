#Galilea Peralta Contreras.
#14 de octubre de 2024.
#Descripción:
#Conversión de tipos de datos (casting) en Python.

print("Realiza un programa de nombre Casting_ejercicio.py que realice lo siguiente:")

print()
print("A)Convierta los siguientes números en cadenas: 3.14159265, 12, 0.")
#Llenar datos
Variable_1 = 3.14159265
Variable_2 = 12
Variable_3 = 0
#Imprimir datos y convertir los numeros a cadenas
print(f"El número {Variable_1} se convierten a cadena: {str(Variable_1)}.")
print(f"El número {Variable_2} se convierten a cadena: {str(Variable_2)}.")
print(f"El número {Variable_3} se convierten a cadena: {str(Variable_3)}.")

print()
print("B) De los números anteriores, indica su valor booleano.")
Es_verdadero = bool(Variable_1)
print(f"¿El valor de {Variable_1} es verdadero? {Es_verdadero}.")
Es_verdadero = bool(Variable_2)
print(f"¿El valor de {Variable_2} es verdadero? {Es_verdadero}.")
Es_verdadero = bool(Variable_3)
print(f"¿El valor de {Variable_3} es verdadero? {Es_verdadero}.")

print()
print("C) Convierta las siguientes cadenas a números: 10002, 100.02, 0.")
Variable_1 = "10002"
Variable_2 = "100.02"
Variable_3 = "0"
print(f"la cadena {Variable_1} se convierte en el  número {int(Variable_1)}.")
print(f"la cadena {Variable_2} se convierte en el número {float(Variable_2)}.")
print(f"la cadena {Variable_3} se convierte en el número{int(Variable_3)}.")

print()
print("D) De las cadenas anteriores, indica su valor booleano. Nota: especificar por qué el resultado de la cadena 0.")

Es_verdadero = bool(Variable_1)
print(f"¿El valor de {Variable_1} es verdadero? {Es_verdadero}.")
Es_verdadero = bool(Variable_2)
print(f"¿El valor de {Variable_2} es verdadero? {Es_verdadero}.")
Es_verdadero = bool(Variable_3)
print(f"¿El valor de {Variable_3} es verdadero? {Es_verdadero}.")
#El 0 representa un carácter, lo que lo hace diferente al 0 en número.
#La cadena "0" no está vacía, contiene un carácter (el dígito "0").
#Cuando la cadena está vacía es falso, pero este caso no lo está.