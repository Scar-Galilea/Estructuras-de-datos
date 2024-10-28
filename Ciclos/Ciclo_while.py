#Galilea Peralta Contreras.
#28 de octubre de 2024.
#Descripción:
#Usos de los tipos básico de datos en Python.
#Para poder usar el ciclo while se utiliza de la siguiente manera (falta mas)

#Ejemplo 1.
print("*** Programa que imprime los numeros 1 al número que indica el usuario")
Variable_1 = input("Ingrese número: ")
Variable_1 = int(Variable_1)

Contador_1 = 1
print(f"Los números de 1 al {Variable_1} son: ")

while Contador_1 <= Variable_1:
    print(Contador_1)
    Contador_1 += 1


#Ejemplo 2
print()
print("*** Programa que imprime los numeros 1 al número que indica el usuario")
Variable_1 = input("Ingrese número: ")
Variable_1 = int(Variable_1)

Contador_1 = 1
print(f"Los números de 1 al {Variable_1} son: ")

while Contador_1 <= Variable_1:
    print(Contador_1 ,end = " ")
    Contador_1 += 1
print("Fin de cuenta")

#Ejemplo 3
print()
print("*** Programa que imprime los numeros pares al número que indica el usuario")
Variable_1 = input("Ingrese número: ")
Variable_1 = int(Variable_1)

Contador_1 = 0
print(f"Los números de 1 al {Variable_1} son: ")

while Contador_1 <= Variable_1 :
    print(Contador_1 ,end = " ")
    Contador_1 += 2
print("Fin de cuenta")
