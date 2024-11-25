#Galilea Peralta Contreras.
#29 de octubre de 2024.
#Descripción:
#Usos de los tipos básico de datos en Python.
"""
Escribe un programa de nombre Ciclos_ej4_cuenta_bancaria.py que realice lo siguiente:
Este programa realiza las operaciones básicas de una cuenta:
1) Mostrar saldo.
2) Ingresar dinero.
3) Retirar dinero.
0) Salir.

Cualquier otro caso -> Mostrar un mensaje de "opción no válida".
Para ello:
a) Suponga un saldo inicial cualquiera.
b) Muestre el menú.
c) Si la opción seleccionada es 1 o 2, verificando la cantidad a modificar.
c) Calcule el resultado de acuerdo a la opción.
d) Muestre el saldo en pantalla.
e) Repita el menú anterior
"""
Saldo = 0
Opcion = None
while Opcion != 0:
    print("*** Bienvenido al Banco Azteca. **+")
    print("0) Salir.")
    print("1) Consulte saldo.")
    print("2) Ingresar dinero.")
    print("3) Retirar dinero.")
    print()
    Opcion = int(input("Ingresa una opción: "))

    if Opcion != 0:
        print()
        print("Fin del programa.")
    elif Opcion == 1:
        print()
        print(f"Su saldo es de: ${Saldo : .2f}.")
        print()
    elif Opcion == 2:
        Cantidad = float(input("Ingrese la cantidad: "))
        Saldo = Saldo + Cantidad
        print("Se ingreso su saldo exitosamente.")
        print()
    elif Opcion == 3:
        Cantidad = float(input("Ingrese la cantidad que se va a retirar: "))
        if Cantidad < Saldo:
            Saldo = Saldo - Cantidad
            print("Se retiro su saldo exitosamente.")
        else:
            print("No se pudo completar esta operación.")
        print()
    else:
        print()
        print("Opción incorrecta.")
        print()


