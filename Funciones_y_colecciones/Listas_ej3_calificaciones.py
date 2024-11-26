#Galilea Peralta Contreras.
#13 de noviembre del 2024.
#Descripción:
#Usos de los tipos básico de datos en Python
"""
Escribe un programa de nombre Listas_ej3_calificaciones.py que realice lo siguiente:
Este programa es una lista de las calificaciones de los alumnos del Parcial 1. La lista está conformada por el nombre del alumno y sus calificaciones.
Cada alumno tiene 5 calificaciones: estructuras de datos, derecho, contabilidad, álgebra y electrónica.
Se debe mostrar el siguiente menú:

  ***  Calificaciones del Parcial 1  ***
1) Ver calificaciones de todos los alumnos.
2) Ver calificaciones detalladas de un alumno.
3) Ver promedios del Parcial 1 de todos los alumnos.
4) Ver promedio grupal del Parcial 1.
5) Agregar alumno y sus calificaciones.
6) Eliminar alumno y sus calificaciones.
0) Salir.

Cualquier otro caso -> Opción no válida.
Para ello:
a) Se sugiere utilizar funciones para modular el código.
b) Se sugiere utilizar listas para las cinco calificaciones, los nombres y las calificaciones de los alumnos.
c) Todas las calificaciones y promedios se deben mostrar únicamente con un decimal.
"""
def Menu():
    print("*** Promedios del parcial 1. **+")
    print()
    print("0) Salir.")
    print("1) Ver calificaciones de alumno.")
    print("2) Ver calificaciones de los alumnos.")
    print("3) Ver promedios del Parcial 1 de todos los alumnos.")
    print("4) Añadir alumno.")
    print("5) Eliminar alumno.")
    print("6) Ver promedio grupal.")
    print()
    Opcion = int(input("Ingresa una opción: "))
    return Opcion

Estructura_de_datos = []
Derecho = []
Contabilidad = []
Algebra = []
Electronica = []
Ingles = []
Calificaciones = [Estructura_de_datos, Derecho, Contabilidad, Algebra, Electronica,Ingles]
Posicion = 0
Opcion = None

while Opcion != 0:
    Opcion = Menu()
    if Opcion  == 0:
        print("Fin de programa.")
    elif Opcion  == 1:
        print()
        if len(Estructura_de_datos) != 0:
             Numero_de_alumno = int(input("Ingrese el numero del alumno que deseas ver: "))
             print("Calificacion del alumno ",Numero_de_alumno)
             print(f" Estructura de datos: {Estructura_de_datos[Numero_de_alumno]: .1f}.")
             print(f" Derecho: {Derecho[Numero_de_alumno]: .1f}.")
             print(f" Contabilidad: {Contabilidad[Numero_de_alumno]: .1f}.")
             print(f" Electronica: {Electronica[Numero_de_alumno]: .1f}.")
             print(f" Ingles: {Ingles[Numero_de_alumno]: .1f}.")
             print()
        else:
            print("No hay alumnos por ver.")
    elif Opcion == 2:
        print()
        if len(Estructura_de_datos) != 0:
            for Calificacion in Calificaciones:
                print(f" {Calificacion}")
        else:
            print("No hay alumnos por ver.")
        print()
    elif Opcion == 3:
        if len(Estructura_de_datos) != 0:
            # Con una materia ya se sabe cuantos alumnos hay
            Numero_de_alumnos = len(Estructura_de_datos)
            Contador = 0
            Promedio_de_un_alumno = 0
            Total = 0
            while Contador < Numero_de_alumnos:
                # Si fuera la otra forma de lista , se podria utilizar la funcion sum
                Promedio_de_un_alumno = (Estructura_de_datos[Contador] + Derecho[Contador] + Contabilidad[Contador] +
                                         Algebra[Contador] + Electronica[Contador] + Ingles[Contador]) / 6
                print(f"El promedio del alumno {Contador} es: {Promedio_de_un_alumno:.1f}.")
                Contador += 1
        else:
            print("No hay alumnos.")


    elif Opcion  == 4:
        print()
        print("Ingrese las calificaciones del alumno")
        Estructura_añadido = float(input("Estructuras de datos: "))
        Derecho_añadido = float(input("Derecho: "))
        Contabilidad_añadido = float(input("Contabilidad: "))
        Algebra_añadido = float(input("Algebra: "))
        Electronica_añadido = float(input("Electronica: "))
        Ingles_añadido = float(input("Ingles: "))

        Calificaciones[0].append(Estructura_añadido)
        Calificaciones[1].append(Derecho_añadido)
        Calificaciones[2].append(Contabilidad_añadido)
        Calificaciones[3].append(Algebra_añadido)
        Calificaciones[4].append(Electronica_añadido)
        Calificaciones[5].append(Ingles_añadido)

        print()
    elif Opcion  == 5:
        Eliminar_de_alumno = int(input("Ingrese el numero del alumno que deseas eliminar: "))
        del Estructura_de_datos[Eliminar_de_alumno]
        del Derecho[Eliminar_de_alumno]
        del Contabilidad[Eliminar_de_alumno]
        del Algebra[Eliminar_de_alumno]
        del Electronica [Eliminar_de_alumno]
        del Ingles[Eliminar_de_alumno]

    elif Opcion == 6:
        if len(Estructura_de_datos) != 0:
            #Con una materia ya se sabe cuantos alumnos hay
            Numero_de_alumnos = len(Estructura_de_datos)
            Contador = 0
            Promedio_de_un_alumno = 0
            Total = 0
            while Contador < Numero_de_alumnos:
                #Si fuera la otra forma de lista , se podria utilizar la funcion sum
                Promedio_de_un_alumno = (Estructura_de_datos[Contador] + Derecho[Contador] + Contabilidad[Contador] + Algebra[Contador] + Electronica[Contador] + Ingles[Contador])/6
                Total = Total + Promedio_de_un_alumno
                Contador += 1
            Total = Total / Numero_de_alumnos
            print(f"El promedio grupal es: {Total: .1f}.")
        else :
            print()
            print("No hay alumnos que promediar.")
        print()
    else:
        print()
        print("Opción incorrecta.")
        print()
