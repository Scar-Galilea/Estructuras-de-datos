#Galilea Peralta Contreras.
#20 de noviembre del 2024.
#Descripción:
#Usos de los tipos básico de datos en Python

def Promedio (calificaciones):
    promedio_parcial = sum(calificaciones[0:2]) * 0.5
    promedio_final = calificaciones[3] * 0.5 + promedio_parcial

    return promedio_parcial,promedio_final

print("*** Calificaciones del parcial ***")
print()
calificaciones = (6,7,8,7)
promedio_parcial,promedio_final = Promedio(calificaciones)

print("Calificacion del parcial es: ",promedio_parcial)
print("Calificacion del promedio final es: ",promedio_final)

