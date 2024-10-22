#Galilea Peralta Contreras.
#14 de octubre de 2024.
#Descripción:
#Conversión de cadenas a int, float y boolean mediante la interacción con consola.

# Las funciones anidadas son aquellas que se encuentran dentro de otras funciones.
# En este caso, dentro de las funciones `int()`, `float()` y `input()`, se están realizando conversiones de tipo
# directamente sobre el valor ingresado por el usuario, lo que permite convertir datos en el mismo paso en que se ingresan.
print("****   Datos de los alumnos    *****")
nombre = input("Ingresa el nombre: ")
semestre = int(input("Ingresa el no. de semestre: "))
promedio = float(input("Ingresa el promedio: "))
es_mujer = input("¿Es mujer (Si/No)?: ")

# No es posible convertir directamente una cadena a un valor booleano.
# Por ello, utilizamos la misma variable, convertimos a  minúsculas y lo comparamos con la cadena "si".
es_mujer = es_mujer.lower() == "si"
#Cuando comparamos con el ==, hacemos que lo que está en comillas sea verdadero.

# Se imprimen los datos del alumno.
# En este caso, el formato {promedio:.2f} significa que se mostrarán solo 2 cifras decimales del promedio.
# Este formato es útil para representar decimales de manera controlada.
print()
print(f"El alumno {nombre} cursa el {semestre} semestre con un promedio de {promedio:.2f}. Además, es mujer: {es_mujer}.")
