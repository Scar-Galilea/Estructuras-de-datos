#Galilea Peralta Contreras.
#11 de octubre de 2024.
#Descripción:
#Usos de los tipos básico de datos en Python.

# Notas:
"""
En Python, no se requiere indicar el tipo de la variable en su declaración.
Los valores básicos que pueden almacenar las variables son:
- Int
- Float
- String (str)
- Boolean. True o False (con inicial mayúscula).
- None. Tipo especial que representa una ausencia de valor.
"""

# Ejemplos de tipos de datos.
# Número entero:
mi_variable_entera = -777
print("Tipo de dato entero:",mi_variable_entera)
#Almacena números positivos o negativos, sin parte decimal.

# Número decimal:
mi_variable_decimal = 43
print("Tipo de dato decimal:", mi_variable_decimal)

# Cadena de texto:
mi_variable_texto_nombre = "Galilea"
mi_variable_texto_apellido = 'Peralta'
print("Cadena de texto:", mi_variable_texto_nombre, mi_variable_texto_apellido)

# Booleno:
mi_variable_booleana = True
print('Tipo booleano:', mi_variable_booleana)

# None:
mi_variable_none = None
print("Tipo none:",mi_variable_none)
#Tipo especial para representar una variable que aún no tiene valor asignado.

# Uso de constantes.
'''
En Python, a diferencia de otros lenguajes de programación, no existe un tipo específico para definir constantes.
Se utiliza una convención de colocar las variables en mayúsculas y no modificarlas.
'''
VARIABLE_CONSTANTE = 3.1416
print("Ejemplo de convención de una constante:", VARIABLE_CONSTANTE)

#Notas:
#Para poder identificar el tipo de mis variables  el nombre de la variable debe de usar nombres de variables descriptivos y claros.
#En Python en mi opinión, se facilita el uso de variables.
#La variable None es refencia a NULL de C++.