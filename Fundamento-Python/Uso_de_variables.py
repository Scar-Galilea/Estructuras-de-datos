#Galilea Peralta Contreras
# 8 de octubre de 2024
# En este archivo se ejemplifica el uso de variables en Python.

# Notas:
# En Python todo es un objeto.
# Variable - una variable es un nombre que almacena un valor guardado en la memoria temporal.

# Toda variable requiere un valor inicial.
semestre = 5        # Es una variable que apunta a un objeto de tipo int con valor de 3.
print(semestre)     # imprime el valor de la variable.
semestre = 3        # la variable ya no apunta al objeto anterior, sino a uno nuevo, por lo que se pierde la referencia.
print(semestre)

# Se crean varias variables para ejemplificar su uso.
#En Python ya no es necesario declarar su tipo de variable.
#Python reconoce el tipo de variable.
nombre = "Galilea"  # variable de tipo String.
altura = 1.60       # variable de tipo Float.
edad = 18          # variable de tipo Int

# Se imprimen las variables, añadiendo información adicional para comprender lo que se imprime.
#Al imprimir no es necesario poner que tipo de variable es, sino que es mas directo con solo poner el nombre de  la variable.
print("Nombre:", nombre)
print("Semestre:", semestre)
print("Altura: ", altura, "cm.")
print("Edad: ", edad, "años.")

# Se modifican los valores de las variables y se mandan a imprimir.
altura = 1.59
edad = 19
print()
print("Valores modificados:")
print("Nombre:", nombre)
print("Semestre:", semestre)
print("Altura: ", altura, "cm.")
print("Edad: ", edad, "años.")

# En Python, las variables son dinámicas, por lo que pueden almacenar otro tipo de dato en cualquier momento.
edad = "Dieciocho"      # edad antes tenía el valor de 18 (Int).
print() #El print si nada de elementos es un reglon.
print("Edad (con otro tipo de dato):", edad)

# Reglas para los nombres de las variables en Python:
# - Utilizar únicamente letras (mayúsculas o minúsculas), números y el guion bajo.
# - La variable no puede iniciar con números.
# - No se pueden utilizar palabras reservadas, ejemplos: if, else, True, class.
# - Es sensible a mayúsculas y minúsculas. Por ejemplo, las palabras "Hola", "hola" y "HOLA" son consideradas diferentes.

# Buenas prácticas:
# - Utilizar minúsculas para las palabras.
# - Separar las palabras con el guion bajo.
# - Utilizar nombres descriptivos de acuerdo a su uso. Por ejemplo: edad, en lugar de e.

#  Reglas para los nombres de las variables en Python:
# - Utilizar únicamente letras (mayúsculas o minúsculas), números y el guion bajo.
# - La variable no puede iniciar con números.
# - No se pueden utilizar palabras reservadas, ejemplos: if, else, True, class.
# - Es sensible a mayúsculas y minúsculas. Por ejemplo, las palabras "Hola", "hola" y "HOLA" son consideradas diferentes.

# Buenas prácticas:
# - Utilizar minúsculas para las palabras.
# - Separar las palabras con el guion bajo.
# - Utilizar nombres descriptivos de acuerdo a su uso. Por ejemplo: edad, en lugar de e.

# Ejemplos correctos y con buenas prácticas
fecha_nacimiento = "1 de noviembre del 2005"
clase = "Estructuras de Datos"
horas_estudio = 4
nombre = "Galilea"
es_estudiante = True

# Ejemplos incorrectos (líneas comentadas porque marcan error) o de malas prácticas
f = "1 de noviembre del 2005"
fechanacimiento = "1 de noviembre del 2005"
# class = "Estructuras de Datos"
#4horas_estudio = 4
Nombre = "G A L I L E A"
NOMBRE = "GALILEA"

# Notar que las variables 'nombre', 'Nombre' y 'NOMBRE', son distintas
print()
print("Las variables son sensibles a mayúsculas y minúsculas:")
print("Variable nombre:", nombre)
print("Variable Nombre:", Nombre)
print("Variable NOMBRE:", NOMBRE)
