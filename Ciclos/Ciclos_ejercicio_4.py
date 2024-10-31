#Galilea Peralta Contreras.
#29 de octubre de 2024.
#Descripción:
#Usos de los tipos básico de datos en Python.

Saldo = 0
Contador_1 = 1
while Contador_1 != 0:
    print("*** Bienvenido al Banco Azteca **+")
    print("0) Salir")
    print("1) Consulte saldo")
    print("2) Ingresar dinero")
    print("3) Retirar dinero")
    print()
    Variable_1 = int(input("Ingresa una opción: "))
    Contador_1 = Variable_1

    if Variable_1 != 0:
        if Variable_1 == 1:
            print()
            print(f"Su saldo es de: ${Saldo : .2f}")
            print()
        elif Variable_1 == 2:
            Variable_2 = float(input("Ingrese la cantidad: "))
            Saldo =  Saldo + Variable_2
            print("Se ingreso su saldo exitosamente")
            print()
        elif Variable_1 == 3:
            Variable_2 = float(input("Ingrese la cantidad que se va a retirar: "))
            if Variable_2 < Saldo:
                Saldo = Saldo - Variable_2
                print("Se retiro su saldo exitosamente")
            else:
                print("No se pudo completar esta operación")
            print()
        else:
            print()
            print("Opción incorrecta")
            print()
print()
print("Salio del programa")

