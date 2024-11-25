#Galilea Peralta Contreras.
#29 de octubre de 2024.
#Descripción:
#Usos de los tipos básico de datos en Python.
"""
Escribe un programa de nombre Ciclos_ej3_calculadora.py que realice lo siguiente:
Este programa es una calculadora básica que contenga el siguiente menú:
1) Suma.
2) Resta.
3) Multiplicación.
4) División.
5) División entera.
6) Exponenciación.
0) Salir.

Cualquier otro caso -> Mostrar un mensaje de "opción no válida".
Para ello:
a) Muestre el menú.
b) Si la opción seleccionada fue entre 1 y 6, solicite dos números al usuario.
c) Calcule el resultado de acuerdo a la opción.
d) Muestre el resultado en pantalla.
e) Repita el menú anterior.
"""
Opcion = None
while Opcion != 0:
    print("*** Calculadora básica. **+")
    print("0) Salir.")
    print("1) Suma.")
    print("2) Resta.")
    print("3) Multiplicación.")
    print("4) División.")
    print("5) División entera.")
    print("6) Exponenciación.")
    print()
    Opcion = int(input("Ingresa una opción: "))

    if Opcion == 0:
        print()
        print("Fin del programa.")
    elif Opcion == 1:
        print()
        print("Suma:")
        Variable_2 = float(input("Ingrese un número: "))
        Variable_3 = float(input("Ingrese otro número: "))
        print()
        print(f"La suma entre el {Variable_2} y el {Variable_3} es {Variable_2 + Variable_3}.")
    elif Opcion == 2:
        print()
        print("Resta:")
        Variable_2 = float(input("Ingrese un número: "))
        Variable_3 = float(input("Ingrese otro número: "))
        print()
        print(f"La resta entre el {Variable_2} y el {Variable_3} es: {Variable_2 - Variable_3}.")
    elif Opcion == 3:
        print()
        print("Multiplicación:")
        Variable_2 = float(input("Ingrese un número: "))
        Variable_3 = float(input("Ingrese otro número: "))
        print()
        print(f"La multiplicación entre el {Variable_2} y el {Variable_3} es: {Variable_2 * Variable_3}.")
    elif Opcion == 4:
        print()
        print("División:")
        Variable_2 = float(input("Ingrese un número: "))
        Variable_3 = float(input("Ingrese otro número: "))
        print()
        print(f"La división entre el {Variable_2} y el {Variable_3} es: {Variable_2 / Variable_3}.")
    elif Opcion == 5:
        print()
        print("División entera:")
        Variable_2 = float(input("Ingrese un número: "))
        Variable_3 = float(input("Ingrese otro número: "))
        print()
        print(f"La división entre el {Variable_2} y el {Variable_3} es: {Variable_2 // Variable_3}.")
    elif Opcion == 6:
        print()
        print("Exponenciacion:")
        Variable_2 = float(input("Ingrese un número: "))
        Variable_3 = float(input("Ingrese otro número: "))
        print()
        print(f"La exponenciacion entre el {Variable_2} y el {Variable_3} es: {Variable_2 ** Variable_3}.")
    else:
        print()
        print("Opción incorrecta.")
        print()



