#Galilea Peralta Contreras.
#29 de octubre de 2024.
#Descripción:
#Usos de los tipos básico de datos en Python.

Contador_1 = 1
while Contador_1 != 0:
    print("*** Calculadora básica **+")
    print("0) Salir")
    print("1) Suma")
    print("2) Resta")
    print("3) Multipicación")
    print("4) Division")
    print("5) Division entera")
    print("6) Exponenciación")
    print()
    Variable_1 = int(input("Ingresa una opción: "))
    Contador_1 = Variable_1

    if Variable_1 != 0:
        if Variable_1 == 1:
            print()
            print("Suma:")
            Variable_2 = float(input("Ingrese un número: "))
            Variable_3 = float(input("Ingrese otro número: "))
            print()
            print(f"La suma entre el {Variable_2} y el {Variable_3} es {Variable_2 + Variable_3}")
        elif Variable_1 == 2:
            print()
            print("Resta:")
            Variable_2 = float(input("Ingrese un número: "))
            Variable_3 = float(input("Ingrese otro número: "))
            print()
            print(f"La resta entre el {Variable_2} y el {Variable_3} es: {Variable_2 - Variable_3}")
        elif Variable_1 == 3:
            print()
            print("Multiplicación:")
            Variable_2 = float(input("Ingrese un número: "))
            Variable_3 = float(input("Ingrese otro número: "))
            print()
            print(f"La multiplicación entre el {Variable_2} y el {Variable_3} es: {Variable_2 * Variable_3}")
        elif Variable_1 == 4:
            print()
            print("División:")
            Variable_2 = float(input("Ingrese un número: "))
            Variable_3 = float(input("Ingrese otro número: "))
            print()
            print(f"La división entre el {Variable_2} y el {Variable_3} es: {Variable_2 / Variable_3}")
        elif Variable_1 == 5:
            print()
            print("División entera:")
            Variable_2 = float(input("Ingrese un número: "))
            Variable_3 = float(input("Ingrese otro número: "))
            print()
            print(f"La división entre el {Variable_2} y el {Variable_3} es: {Variable_2 // Variable_3}")
        elif Variable_1 == 6:
            print()
            print("Exponenciacion:")
            Variable_2 = float(input("Ingrese un número: "))
            Variable_3 = float(input("Ingrese otro número: "))
            print()
            print(f"La exponenciacion entre el {Variable_2} y el {Variable_3} es: {Variable_2 ** Variable_3}")
        else:
            print()
            print("Opción incorrecta")
            print()
print()
print("Salio del programa")


