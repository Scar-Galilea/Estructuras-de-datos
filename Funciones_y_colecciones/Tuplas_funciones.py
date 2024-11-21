#Galilea Peralta Contreras.
#20 de noviembre del 2024.
#Descripción:
#Usos de los tipos básico de datos en Python

def Promedio (calificaciones):
    promedio_parcial = (sum(calificaciones[0:3]))/3
    promedio_final = calificaciones[3] * 0.5 + promedio_parcial * 0.5

    return promedio_parcial,promedio_final

print("*** Calificaciones del parcial ***")
print()
# Se solicitan las calificaciones de los parciales y ordinario.
parcial1 = float(input("Ingresa la calificación del Parcial 1: "))
parcial2 = float(input("Ingresa la calificación del Parcial 2: "))
parcial3 = float(input("Ingresa la calificación del Parcial 3: "))
ordinario = float(input("Ingresa la calificación del Ordinario: "))
print()

# Se crea una tupla
calificaciones = (parcial1, parcial2, parcial3, ordinario)
promedio_parcial,promedio_final = Promedio(calificaciones)

print("Calificacion del parcial es: ",promedio_parcial)
print("Calificacion del promedio final es: ",promedio_final)

