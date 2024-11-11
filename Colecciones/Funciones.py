#Galilea Peralta Contreras.
#11 de noviembre del 2024.
#Descripción:
#Usos de los tipos básico de datos en Python.
"""
def hola( nombre ):
    print(f"Hola {Nombre}")
Nombre = input("Ingrese tu nombre: ")
hola(Nombre)
print("Adios")
"""

def Menu():
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicación")
    print("4) División")
    print("5) División entera")
    print()
    Opcion = int(input("Ingrese la opcion: "))
    return Opcion

def Calculadora (Opcion,Numero_1,Numero_2):
    if Opcion == 1:
        print()
        print("Suma:")
        Resultado = Numero_1 + Numero_2
    elif Opcion == 2:
        print()
        print("Resta:")
        Resultado = Numero_1 - Numero_2
    elif Opcion == 3:
        print()
        print("Multiplicación:")
        Resultado = Numero_1 * Numero_2
    elif Opcion == 4:
        print("División:")
        Resultado = Numero_1 / Numero_2
    elif Opcion == 5:
        print("División entera:")
        Resultado = Numero_1 // Numero_2
    else:
        print()
        print("Opción incorrecta")
        print()
    return Resultado

Opcion = Menu()

Numero_1 = int(input("Ingrese número: "))
Numero_2 = int(input("Ingrese número: "))

Resultado = Calculadora(Opcion,Numero_1,Numero_2)

print(f"El resultado es: {Resultado}")




