#Galilea Peralta Contreras.
#19 de noviembre del 2024.
#Descripción:
#Usos de los tipos básico de datos en Python

"""
Este programa muestra el valor máximo y mínimo de una lista de números. En este caso, la tupla se utiliza para devolver los valores máximo y mínimo de la función.
Se debe mostrar el siguiente menú:
  ***  Valor máximo y mínimo de una lista de números del usuario  ***
1) Ver lista de números.
2) Añadir número a la lista.
3) Determinar el valor máximo y mínimo de la lista de números.
0) Salir.
Cualquier otro caso -> Opción no válida.
Para ello:
a) Se sugiere utilizar una función para mostrar el menú.
b) Se debe utilizar una única función para devolver el valor máximo y mínimo en una tupla.
"""
def Menu():
    print("*** Listas de compras**+")
    print()
    print("0) Salir")
    print("1) Ver lista de números")
    print("2) Añadir un número a la lista")
    print("3) Determinar el valor máximo y mínimo de la lista de números")
    print()

    Opcion = int(input("Ingrese la opcion: "))
    return Opcion

def Maximos_y_minimos(Tupla_de_numeros):
    contador = 1
    Numero_de_elementos = len(Tupla_de_numeros)
    Tupla_de_maximo_y_minimo = ()
    Maximo,Minimo = Tupla_de_numeros[0],Tupla_de_numeros[0]
    while contador < Numero_de_elementos:
        if Tupla_de_numeros[contador] > Maximo:
            Maximo = Tupla_de_numeros[contador]
        else:
            if Tupla_de_numeros[contador] < Minimo:
                Minimo = Tupla_de_numeros[contador]
        contador += 1
    Tupla_de_maximo_y_minimo = Maximo,Minimo
    return Tupla_de_maximo_y_minimo


Opcion = None
Tupla_de_numeros = ()
Numero_guardados = []
while Opcion != 0:
    Opcion = Menu()
    if Opcion == 0:
        print("Fin del programa")
    elif Opcion == 1:
        if len(Tupla_de_numeros) != 0:
            print(f"La lista de número es: {Tupla_de_numeros},")
        else:
            print("No hay números para mostrar")
        print()
    elif Opcion  == 2:
        print()
        Numero_añadido = float(input("Ingrese el número a la lista: "))
        Numero_guardados.append(Numero_añadido)
        Tupla_de_numeros = (Numero_guardados)
        print(f"¡El número {Numero_añadido} se agrego con exito!")
        print()

    elif Opcion  == 3:
        print()
        if len(Tupla_de_numeros) != 0:
            Numero_maximo,Numero_minimo = Maximos_y_minimos(Tupla_de_numeros)
            print("El número maximo de la lista es: ", Numero_maximo)
            print("El número minimo de la lista es: ", Numero_minimo)
        else:
            print("No hay números")
        print()
    else:
        print()
        print("Opción incorrecta")
        print()
print()
print("Salio del programa")