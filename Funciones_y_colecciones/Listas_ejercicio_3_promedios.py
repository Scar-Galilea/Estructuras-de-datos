#Galilea Peralta Contreras.
#13 de noviembre del 2024.
#Descripción:
#Usos de los tipos básico de datos en Python
Calificaciones =
while Contador_1 != 0:
    print("*** Promedios del Parcial 1**+")
    print()
    print("0) Salir")
    print("1) Ver calificaciones de alumno")
    print("2) Ver calificaciones de los alumnos")
    print("3) Añadir alumno")
    print("4) Eliminar alumno")
    print("5) Ver promedio grupal")
    print()
    Contador_1 = int(input("Ingresa una opción: "))
    if Contador_1  != 0:
        if Contador_1  == 1:
            Numero = 0
            for Producto in Productos:
                print(f"{Cantidades[Numero]}- {Producto}")
                Numero += 1
        elif Contador_1 == 2:
            Numero = 0
            for Producto in Productos:
                print(f"{Cantidades[Numero]}- {Producto}")
                Numero += 1
        elif Contador_1  == 3:
            print()
            Producto_añadido = input("Ingrese el producto: ")
            Cantidad_añadida = input("Ingrese la cantidad del producto: ")
            Productos.append(Producto_añadido)
            Cantidades.append(Cantidad_añadida)
            Contador_2 += 1
            print()
        elif Contador_1  == 4:
            Eliminar_producto = input("Ingrese el producto que desea eliminar: ")
            Numero_de_producto = 0

            while Productos[Numero_de_producto] != Eliminar_producto:
                Numero_de_producto += 1

            Productos.remove(Eliminar_producto)
            del Cantidades[Numero_de_producto]
        elif Contador_1 == 5:
            Numero = 0
            for Producto in Productos:
                print(f"{Cantidades[Numero]}- {Producto}")
                Numero += 1

        else:
            print()
            print("Opción incorrecta")
            print()
print()
print("Salio del programa")