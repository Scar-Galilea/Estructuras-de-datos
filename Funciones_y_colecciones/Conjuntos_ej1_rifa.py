#Galilea Peralta Contreras.
#28 de noviembre del 2024.
#Descripción:
#Este programa es una rifa en donde se registran correos electrónicos, y cada participante solo puede ingresar un correo.
#Permite administrar los participantes y seleccionar un ganador al azar.
"""
Escribe un programa de nombre Conjuntos_ej1_rifa.py que realice lo siguiente:
Este programa es una rifa, en donde se registra el correo electrónico y solamente permite ingresar un correo por participante.
Se debe mostrar el siguiente menú:

  ***  Rifa de una computadora  ***
1) Ver correos de participantes.
2) Agregar correo de participante.
3) Eliminar correo de participante.
4) Seleccionar ganador.
0) Salir.

Cualquier otro caso -> Opción no válida.
Para ello:
a) Utilice un conjunto para almacenar los correos de los participantes.
b) Utilice un valor aleatorio utilizando la función random.choice(lista). Notar que hay que convertir primero a una lista.
"""
from random import random, choice  #Se importa la función choice para seleccionar un ganador al azar.


#Función para mostrar el menú y devolver la opción seleccionada.
def Menu():
    print("***  Rifa de una computadora  ***")
    print()
    print("0) Salir.")
    print("1) Ver correos de participantes.")
    print("2) Agregar correo de participante.")
    print("3) Eliminar correo de participante.")
    print("4) Seleccionar ganador.")
    print()

    #Solicita la opción del usuario.
    Opcion = int(input("Ingrese la opción: "))
    return Opcion

#Declaración del conjunto para almacenar los correos electrónicos de los participantes.
Conjunto_de_correos = set()
Opcion = None

while Opcion != 0:
    Opcion = Menu() #Muestra el menú y obtiene la opción del usuario.
    if Opcion == 0: #Salir del programa.
        print()
        print("Fin del programa.")
    elif Opcion == 1: #Mostrar la lista de correos registrados.
        print()
        if len(Conjunto_de_correos) != 0: #Verifica si hay correos registrados.
            print("El conjunto de correos electrónico es:")
            for Correo in Conjunto_de_correos:#Recorre e imprime cada correo.
                print(f"-{Correo}")
        else:
            print("No hay participantes por mostrar.") #Mensaje si el conjunto está vacío.

    elif Opcion  == 2:  #Agregar un nuevo correo electrónico.
        print()
        Correo_a_añadir = input("Ingrese el correo electrónico del participante a agregar: ")
        Conjunto_de_correos.add(Correo_a_añadir)    #Añade el correo al conjunto (automáticamente evita duplicados).
        print(f"¡El correo electrónico {Correo_a_añadir} se añadió con éxito!")
    elif Opcion == 3:    #Eliminar un correo electrónico existente.
        print()
        if len(Conjunto_de_correos) != 0: #Verifica si hay correos registrados.
            for Correo in Conjunto_de_correos:  #Muestra los correos actuales.
                print(f"-{Correo}")
            print()
            Correo_a_eliminar =input("Ingrese el correo electrónico del participante a eliminar: ")
            Conjunto_de_correos.remove(Correo_a_eliminar)   #Elimina el correo del conjunto.
            print(f"¡El correo  electrónico se eliminó con éxito!")
        else:
            print("No hay participantes por eliminar.") #Mensaje si el conjunto está vacío.
    elif Opcion  == 4:  #Seleccionar un ganador al azar.
        print()
        if len(Conjunto_de_correos) != 0:
            print()
            Lista_de_correos = list(Conjunto_de_correos)  #Convierte el conjunto a una lista para usar random.choice.
            Ganador = choice(Lista_de_correos)  #Mensaje si no hay participantes.
            print(f"El correo ganador es {Ganador}")
            print("¡Muchas felicidades!")
        else:
            print("No hay correos por seleccionar.")
    else:
        print()
        print("Opción incorrecta.") #Mensaje para opciones no válidas.
    print("______________________________________________________")
    print()