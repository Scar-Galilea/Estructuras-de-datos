#Galilea Peralta Contreras.
#12 de noviembre del 2024.
#Descripción:
#Usos de los tipos básico de datos en Python

Videos_de_YT = []

Contador_1 = 1
while Contador_1 != 0:
    print("*** Videos de YT **+")
    print()
    print("0) Salir")
    print("1) Ver listas de videos por añadido")
    print("2) Ver listas de videos por orden A-Z")
    print("3) Ver listas de videos por orden Z-A")
    print("4) Añadir videos")
    print("5) Añadir varios videos")
    print("6) Eliminar videos")
    print()
    Contador_1 = int(input("Ingresa una opción: "))
    if Contador_1  != 0:
        print()
        if Contador_1  == 1:
            Numero = 1
            for Video_de_YT in Videos_de_YT:
                print(f"{Numero}._ {Video_de_YT}")
                Numero += 1
        elif Contador_1  == 2:
            print()
            Videos_de_YT.sort()
            for Video_de_YT in Videos_de_YT:
                print(Video_de_YT, end=",")
                print()
        elif Contador_1  == 3:
            print()
            Videos_de_YT.sort(reverse = True)
            for Video_de_YT in Videos_de_YT:
                print(Video_de_YT, end=",")
                print()
        elif Contador_1  == 4:
            print()
            Videos = input("Ingrese el video: ")
            Videos_de_YT.append(Videos)
            print()
        elif Contador_1  == 5:
            print()
            Añadidos = int(input("Cuantos videos desea añadir "))
            Contador_2 = 0
            while Contador_2 <= Añadidos:
                Videos = input("Ingrese el video")
                Videos_de_YT.append(Videos)
                Contador_2 += 1
            print()
        elif Contador_1  == 6:
            Eliminar_video = input("Ingrese el video que desea eliminar: ")
            Videos_de_YT.remove(Eliminar_video)
        else:
            print()
            print("Opción incorrecta")
            print()
print()
print("Salio del programa")