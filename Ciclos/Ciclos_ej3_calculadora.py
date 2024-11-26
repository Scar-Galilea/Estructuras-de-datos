#Galilea Peralta Contreras.
#29 de octubre de 2024.
#Descripción:
#Este programa implementa una calculadora básica con un menú para realizar operaciones matemáticas básicas.
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
#Inicializar variable para controlar el bucle.
Opcion = None

#Ciclo principal del programa.
while Opcion != 0:
    #Mostrar el menú al usuario.
    print("*** Calculadora básica. ***")
    print("0) Salir.")
    print("1) Suma.")
    print("2) Resta.")
    print("3) Multiplicación.")
    print("4) División.")
    print("5) División entera.")
    print("6) Exponenciación.")
    print()

    #Solicitar la opción al usuario.
    Opcion = int(input("Ingresa una opción: "))

    #Caso: Salir del programa.
    if Opcion == 0:
        print()
        print("Fin del programa.")

    #Caso: Suma.
    elif Opcion == 1:
        print()
        print("Suma:")
        Variable_2 = float(input("Ingrese un número: "))
        Variable_3 = float(input("Ingrese otro número: "))
        print()
        print(f"La suma entre el {Variable_2} y el {Variable_3} es: {Variable_2 + Variable_3}.")

    #Caso: Resta.
    elif Opcion == 2:
        print()
        print("Resta:")
        Variable_2 = float(input("Ingrese un número: "))
        Variable_3 = float(input("Ingrese otro número: "))
        print()
        print(f"La resta entre el {Variable_2} y el {Variable_3} es: {Variable_2 - Variable_3}.")

    #Caso: Multiplicación.
    elif Opcion == 3:
        print()
        print("Multiplicación:")
        Variable_2 = float(input("Ingrese un número: "))
        Variable_3 = float(input("Ingrese otro número: "))
        print()
        print(f"La multiplicación entre el {Variable_2} y el {Variable_3} es: {Variable_2 * Variable_3}.")

    #Caso: División.
    elif Opcion == 4:
        print()
        print("División:")
        Variable_2 = float(input("Ingrese un número: "))
        Variable_3 = float(input("Ingrese otro número: "))
        print()
        print(f"La división entre el {Variable_2} y el {Variable_3} es: {Variable_2 / Variable_3}.")

    #Caso: División entera.
    elif Opcion == 5:
        print()
        print("División entera:")
        Variable_2 = float(input("Ingrese un número: "))
        Variable_3 = float(input("Ingrese otro número: "))
        print()
        print(f"La división entera entre el {Variable_2} y el {Variable_3} es: {Variable_2 // Variable_3}.")

    #Caso: Exponenciación.
    elif Opcion == 6:
        print()
        print("Exponenciación:")
        Variable_2 = float(input("Ingrese un número: "))
        Variable_3 = float(input("Ingrese otro número: "))
        print()
        print(f"La exponenciación entre el {Variable_2} y el {Variable_3} es: {Variable_2 ** Variable_3}.")

    #Caso: Opción no válida.
    else:
        print()
        print("Opción incorrecta.")
        print()


