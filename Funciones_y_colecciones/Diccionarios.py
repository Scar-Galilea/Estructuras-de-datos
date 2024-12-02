#Galilea Peralta Contreras.
#02 de diciembre del 2024.
#Descripción:
#Usos de los tipos básico de datos en Python.

"""
Un diccionario en Python funciona como un par clave-valor:
- Clave: Un valor único e inmutable que se utiliza para acceder a un valor específico.
  Puede ser de casi cualquier tipo de dato, como una cadena, un número o incluso una tupla.
- Valor: El dato asociado a una clave. Puede ser de cualquier tipo de dato y son mutables.

Sintaxis para crear un diccionario:
Se utilizan llaves {} para definir un diccionario. Cada par clave-valor se separa por una coma.
nombre_diccionario ={clave1: valor1, clave2: valor2, clave3: valor3, ...}

"""
"""
# Se crean dos diccionarios y se imprimen.
print("          ********  Ejemplos de uso de diccionarios  ********")

diccionario_profesor = {'nombre': 'Alberto',
                        'primer_apellido': 'Martínez',
                        'segundo_apellido': 'Barbosa',
                        'edad': 31,
                        'correo': 'alberto.mtba@unsij.edu.mx',
                        'cubo': 12}                             # No olvidar el uso de las comas

diccionario_alumno = {}

print(f"Diccionario del profesor: {diccionario_profesor}")
print(f"Diccionario del alumno (vacío): {diccionario_alumno}")
print()


# Se agregan elementos al diccionario del alumno.
print("Se agregan valores al diccionario.")

diccionario_alumno['nombre'] = "Yared"
diccionario_alumno['primer_apellido'] = "Cerqueda"
diccionario_alumno['grupo'] = "303"

print(f"Diccionario del alumno con valores agregados: {diccionario_alumno}")
print()


# Se accede a los elementos del diccionario, en donde se tienen dos formas.
print("Se acceden a los valores del diccionario.")
nombre = diccionario_profesor.get('nombre')
primer_apellido = diccionario_profesor['primer_apellido']

print(f"Nombre del profesor: {nombre}")
print(f"Primer apellido del profesor: {primer_apellido}")
print()


# Se modifican los valores del diccionario. Las claves no se pueden modificar porque son inmutables.
print("Se modifican los valores del diccionario.")
print(f"Diccionario del alumno antes de modificar los valores: {diccionario_alumno}")
diccionario_alumno['nombre'] = "Yare"
diccionario_alumno['grupo'] = "403"

print(f"Diccionario del alumno después de modificar los valores: {diccionario_alumno}")
print()


# Se elimina el par clave-valor del diccionario, en donde se tiene dos formas.
print("Se elimina el par clave-valor del diccionario.")

print(f"Diccionario (antes): {diccionario_profesor}")
del diccionario_profesor['edad']
diccionario_profesor.pop('correo')
print(f"Diccionario (después): {diccionario_profesor}")
print()


# Se muestran las claves y los valores utilizando ciclos for y diferentes funciones.
print("Se muestran las claves y los valores del diccionario del profesor.")

for clave, valor in diccionario_profesor.items():   # Devuelve en par clave-valor como una tupla.
    print(f"Par clave-valor: {clave, valor}")
print()

for valor in diccionario_profesor.values():         # Devuelve únicamente los valores.
    print(f"Valor: {valor}")
print()

for clave in diccionario_profesor.keys():           # Devuelve únicamente las claves.
    print(f"Clave: {clave}")
print()

TEMAS UN POCO MÁS AVANZADOS.
# Uso de tuplas para guardar la clave.
print("Uso de tuplas para guardar la clave.")

diccionario_egresado = { 'nombre': "Diego",
                         ('primer_apellido', 'segundo_apellido') : "Ocaña Martínez",
                         'edad': 25}

print(f"Diccionario del egresado: {diccionario_egresado}")

for clave, valor in diccionario_egresado.items():
    print(f"Par clave-valor: {clave, valor}")
print()


# Combinación de diccionarios.
print("Combinación de diccionarios.")

diccionario_informatica = {
    'grupo 303' : {'no_alumnos': 12,
                   'no_materias': 5,
                   'no_creditos': 48},

    'grupo 503' : {'no_alumnos': 7,
                   'no_materias': 5,
                   'no_creditos': 40},

    'grupo 703' : {'no_alumnos': 7,
                   'no_materias': 5,
                   'no_creditos': 42},

    'grupo 903' : {'no_alumnos': 2,
                   'no_materias': 5,
                   'no_creditos': 45},
}

print(f"Diccionario de informática: {diccionario_informatica}")

for grupo in enumerate(diccionario_informatica):
    print(f"Grupo: {grupo}")

print("No. de alumnos de cada grupo:")
print(f"Grupo 303: {diccionario_informatica['grupo 303']['no_alumnos']}")
print(f"Grupo 503: {diccionario_informatica['grupo 503']['no_alumnos']}")
print(f"Grupo 903: {diccionario_informatica['grupo 903']['no_alumnos']}")
"""

Diccionario_alumno = {}

print(f"{Diccionario_alumno}")
#Se añaden elementos

Diccionario_alumno['Nombre'] = "Galilea"
Diccionario_alumno['Prmer_apellido'] = "Peralta"

print(Diccionario_alumno)
print()

print(Diccionario_alumno.get('Nombre'))
print(Diccionario_alumno['Prmer_apellido'])

Diccionario_alumno['Nombre'] = "Scarlett"
print(Diccionario_alumno)

Diccionario_alumno['Grupo'] = 403
print(Diccionario_alumno)

#Eliminar
del Diccionario_alumno['Prmer_apellido']
print(Diccionario_alumno)
Diccionario_alumno.pop('Grupo')
print(Diccionario_alumno)

Diccionario_alumno['Prmer_apellido'] = "Peralta"
#Se accede al par clave_valor

for clave,valor in Diccionario_alumno.items():
    print(clave,valor)

#Combinación con tuplas

Diccionario_egresado = { 'Nombre': "Diego",
                         ('Primer_apellido', 'Segundo_apellido') : "Ocaña Martínez",
                         'edad': 25 }
print(Diccionario_egresado)

Diccionario_informatica = {
    'Grupo 303':{'No_alumnos' : 12,
                 'No_materias': 5,
                 'Promedio_grupal' : 7.99},
    'Grupo 503':{'No_alumnos' : 7,
                 'No_materias': 5,
                 'Promedio_grupal' : 6},
    'Grupo 903':{'No_alumnos' : 5,
                 'No_materias': 5,
                 'Promedio_grupal' : 8}
}

print(Diccionario_informatica)

for grupo in enumerate(Diccionario_informatica):
    print(f"Grupo: {grupo}")

Promedio_303 = Diccionario_informatica['Grupo 303']['Promedio_grupal']
Promedio_503 = Diccionario_informatica['Grupo 503']['Promedio_grupal']
Promedio_903 = Diccionario_informatica['Grupo 903']['Promedio_grupal']
print(Promedio_303)
print(Promedio_503)
print(Promedio_903)

