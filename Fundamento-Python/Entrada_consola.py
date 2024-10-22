#Galilea Peralta Contreras.
#14 de octubre de 2024.
#Descripción:
#Entrada de datos por consola para interacturar con el usuario con valores dinámicos.

# La función input se utiliza para recibir datos del usuario desde la consola.
# Por defecto, los datos recibidos con input se almacenan como cadenas de texto .
numero1_cadena = input("Introduce un número decimal: ")
numero2_cadena = input("Introduce otro número decimal: ")

# En esta línea, se está concatenando las dos cadenas,es decir se juntan las dos cadenas.
resultado_cadena = numero1_cadena + numero2_cadena # Verificar qué es lo que realiza esta instrucción (ver el print).
print()
print(" ****  Recibir número sin un casting de varibles  ****")
print(f"El resultado de {numero1_cadena} y {numero2_cadena} es: {resultado_cadena}")

# Para realizar operaciones matemáticas, es necesario convertir las cadenas a un tipo de dato numérico.
# Esto es lo que se conoce como casting, que en este caso será de cadena a float.
numero2_float = float(numero2_cadena)
resultado_float = numero1_float + numero2_float # Verificar qué es lo que realiza de esta manera y compáralo.
print()
print(" ****  Casting de varibles  ****")
print(f"El resultado de {numero1_float} y {numero2_float} es: {resultado_float}")
# Ahora que ambos valores son de tipo float, podemos sumarlos correctamente como números.

#Notas:
#Los datos que nos dé el usuario siempre serán cadenas.
#Si queremos recibir otro tipo de datos que no sean cadenas, debemos de convertirlo primero antes de utilizarlos.


