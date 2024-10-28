#Galilea Peralta Contreras.
#28 de octubre de 2024.
#Descripción:
#Sistema de autentificación.

#Escribe un programa de nombre Operadores_ejercicio3.py que realice lo siguiente:
#Este programa determinará si un usuario se autentifica correctamente con su usuario y contraseña. Para ello:
#a) Internamente declare dos cadenas constantes, una para el usuario y otra para la contraseña.
#b) Pida al usuario una cadena con el usuario.
#c) Pida al usuario una cadena con la contraseña.
#d) Si ambas cadenas son iguales a las cadenas declaradas internamente, entonces el usario se autenticó correctamente.
#e) Muestre el resultado en consola como valor booleano (True/False).

#Nota: Las cadenas no tienen que ser convertidas a minúsculas.

print("*** Sistema de autentificación ***")
Variable_1 = input("Ingresa tu usuario: ")
Variable_2 = input("Ingresa tu contraseña: ")

# Declaración de usuario y contraseña válidos.
Variable_1 = Variable_1 == "Alumnos"
Variable_2 = Variable_2 == "Python"

# Verificar si el usuario y la contraseña ingresados coinciden con los valores correctos
print(f"El acceso es correcto? {Variable_1 and Variable_2}")