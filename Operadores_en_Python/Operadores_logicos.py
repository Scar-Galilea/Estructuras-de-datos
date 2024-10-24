#Galilea Peralta Contreras.
#16 de octubre de 2024.
#Descripción:
#Ejemplos de uso de los operadores relacionales.

"""
Los operadores lógicos permiten combinar expresiones booleanas (verdadero o falso) para crear condiciones más complejas.
Estos operadores nos permiten realizar operaciones lógicas como "y", "o" y "no", lo que nos da la capacidad de tomar
decisiones más sofisticadas dentro de nuestros programas.
"""

# Se solicita por consola que se ingresen dos valores (Si/No) para covnertirlas a expresiones booleanas.
Expresión_1= input("Ingrese un si o no: ")
Expresión_2= input("Ingrese un si o no: ")

# Las cadenas se convierten a expresiones booleanas.
Expresión_1 = Expresión_1.lower()=="si"
Expresión_2 = Expresión_2.lower()=="si"

print(Expresión_1)
print(Expresión_2)


# Se imprimen mensajes sobre operaciones lógicas.
#And
print(f"¿Ambos fueron si {Expresión_1 and Expresión_2}")
#Or
print(f"¿Ambos fueron no {Expresión_1 and Expresión_2}")

#Nor de la expresion 1.
print(f"¿la expresion fue no fue si? { not Expresión_1}")
#Nor de la expresion 2.
print(f"¿la expresion fue no fue si? { not Expresión_2}")