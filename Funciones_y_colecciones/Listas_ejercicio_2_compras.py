#Galilea Peralta Contreras.
#13 de noviembre del 2024.
#Descripción:
#Usos de los tipos básico de datos en Python
"""
Escribe un programa de nombre Listas_ej2_compras.py que realice lo siguiente:
Este programa es una lista de compras para el súper. La lista está conformado por varios productos. Cada producto tiene un nombre y cantidad, por lo que también se sugiere utilizar una lista.
Se debe mostrar el siguiente menú:
   ***  Lista de compras para el súper  ***
1) Ver lista de productos.
2) Añadir producto a la lista.
3) Eliminar producto de la lista.
0) Salir.

Cualquier otro caso -> Opción no válida.
Para ello:
a) Utilice funciones para modular el código.
b) Utilice una lista para los productos a añadir, en donde también se sugiere utilizar una lista para los productos, es decir, se va a utilizar una lista de listas.
"""
def Menu():
    print("*** Lista de compras para el súper. **+")
    print()
    print("0) Salir.")
    print("1) Ver lista.")
    print("2) Añadir producto a la lista.")
    print("3) Eliminar producto de la lista.")
    print()

    Opcion = int(input("Ingrese la opción: "))
    return Opcion


Productos = []
Cantidades = []
Opcion = None

while Opcion != 0:
    Opcion = Menu()
    if Opcion == 0:
        print("Fin del programa")
    elif Opcion == 1:
        print()
        if len(Productos) == 0:
            Numero = 0
            for Producto in Productos:
                print(f"{Cantidades[Numero]}- {Producto}")
                Numero += 1
        else:
            print("No hay compras por ver")
            print()
    elif Opcion  == 2:
        print()
        Producto_añadido = input("Ingrese el producto: ")
        Cantidad_añadida = input("Ingrese la cantidad del producto: ")
        Productos.append(Producto_añadido)
        Cantidades.append(Cantidad_añadida)
        print()
    elif Opcion  == 3:
        if len(Productos) == 0:
            Eliminar_producto = input("Ingrese el producto que desea eliminar: ")
            Numero_de_producto = 0

            while Productos[Numero_de_producto] != Eliminar_producto:
                Numero_de_producto += 1

            Productos.remove(Eliminar_producto)
            del Cantidades[Numero_de_producto]
        else:
            print("No hay compras por eliminar.")
            print()

    else:
        print()
        print("Opción incorrecta.")
        print()
