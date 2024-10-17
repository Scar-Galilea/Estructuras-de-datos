#Galilea Peralta Contreras.
#16 de octubre de 2024.
#Descripción:
#Usos de los tipos básico de datos en Python.
#Se utilizan para comparar dos valores

Expresión_1= input("Ingrese un si o no: ")
Expresión_2= input("Ingrese un si o no: ")

Expresión_1 = Expresión_1.lower()=="si"
Expresión_2 = Expresión_2.lower()=="si"

print(Expresión_1)
print(Expresión_2)

#AND
print(f"¿Ambos fueron si {Expresión_1 and Expresión_2}")
#OR
print(f"¿Ambos fueron no {Expresión_1 and Expresión_2}")

#NOR de la expresion 1.
print(f"¿la expresion fue no fue si? { not Expresión_1}")
#NOR de la expresion 2.
print(f"¿la expresion fue no fue si? { not Expresión_2}")