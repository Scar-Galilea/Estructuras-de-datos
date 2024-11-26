#Galilea Peralta Contreras.
#29 de octubre de 2024.
#Descripción:
#Este programa simula las operaciones básicas de una cuenta bancaria.
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
#Inicializar variables.
Saldo = 0  #Saldo inicial de la cuenta.
Opcion = None  #Variable para controlar el menú.

#Ciclo principal del programa.
while Opcion != 0:
    #Mostrar el menú al usuario.
    print("*** Bienvenido al Banco Azteca. ***")
    print("0) Salir.")
    print("1) Consultar saldo.")
    print("2) Ingresar dinero.")
    print("3) Retirar dinero.")
    print()

    #Solicitar opción al usuario.
    Opcion = int(input("Ingresa una opción: "))

    #Caso: Salir del programa.
    if Opcion == 0:
        print()
        print("Fin del programa.")

    #Caso: Consultar saldo.
    elif Opcion == 1:
        print()
        print(f"Su saldo actual es de: ${Saldo:.2f}.")
        print()

    #Caso: Ingresar dinero.
    elif Opcion == 2:
        Cantidad = float(input("Ingrese la cantidad: "))
        Saldo = Saldo + Cantidad
        print("Se ingreso su saldo exitosamente.")
        print()

    #Caso: Retirar dinero.
    elif Opcion == 3:
        Cantidad = float(input("Ingrese la cantidad que se va a retirar: "))
        if Cantidad < Saldo:
            Saldo = Saldo - Cantidad
            print("Se retiro su saldo exitosamente.")
        else:
            print("No se pudo completar esta operación.")
        print()

    #Caso: Opción no válida.
    else:
        print()
        print("Opción incorrecta.")
        print()

