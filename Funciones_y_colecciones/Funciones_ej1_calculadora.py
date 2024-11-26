#Galilea Peralta Contreras.
#25 de noviembre del 2024.
#Descripción:
#Este programa implementa una calculadora básica con un menú para realizar operaciones matemáticas básicas.


def Menu():
    print("*** Calculadora básica. ***")
    print("1) Suma.")
    print("2) Resta.")
    print("3) Multiplicación.")
    print("4) División.")
    print("5) División entera.")
    print("6) Módulo.")
    print("7) Potenciación.")
    print()
    Opcion = int(input("Ingrese la opción: "))
    return Opcion

def Calculadora (Opcion,Numero_1,Numero_2):
    if Opcion == 1:
        print()
        Resultado = Numero_1 + Numero_2
    elif Opcion == 2:
        print()
        Resultado = Numero_1 - Numero_2
    elif Opcion == 3:
        print()
        Resultado = Numero_1 * Numero_2
    elif Opcion == 4:
        Resultado = Numero_1 / Numero_2
        print()
    elif Opcion == 5:
        Resultado = Numero_1 // Numero_2
        print()
    elif Opcion == 6:
        Resultado = Numero_1 % Numero_2
        print()
    elif Opcion == 7:
        Resultado = Numero_1 ** Numero_2
        print()
    else:
        print()
        print("Opción incorrecta.")
        print()
    return Resultado

Opcion = None

while Opcion != 0:
    Opcion = Menu()
    if Opcion != 0:
        Numero_1 = int(input("Ingrese un número: "))
        Numero_2 = int(input("Ingrese un número: "))

        Resultado = Calculadora(Opcion,Numero_1,Numero_2)

        print(f"El resultado es: {Resultado}.")
        print()
    else:
        print("Fin del programa.")
        print("___________________________________________-")
