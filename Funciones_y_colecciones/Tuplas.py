#Galilea Peralta Contreras.
#19 de noviembre del 2024.
#Descripción:
#Usos de los tipos básico de datos en Python

print("*** Ejemplo de tuplas ***")
fechas_cumple = ('12-19','12-27','01-10','10-18','11-01','09-30','08-25','01-06','10-21,04-11','03-06','08-02')

print("*** Series de pi de Leibniz")

pi_serie = (4,-4/3, 4/5, -4/7, 4/9, -4/11, 4/13 -4/15, 4/17, -4/19, 4/21, -4/23)

print(f"La suma de los 3 digitos son {sum(pi_serie[0:2]):.4f}")
print(f"La suma de los 4 digitos son {sum(pi_serie[0:3]):.4f}")
print(f"La suma de los 5 digitos son {sum(pi_serie[0:4]):.4f}")
print(f"La suma de los 8 digitos son {sum(pi_serie[0:7]):.4f}")
print(f"La suma de los 10 digitos son {sum(pi_serie[0:9]):.4f}")
print(f"La suma de los total digitos son {sum(pi_serie):.4f}")

print("*** Ejemplo con cordenadas ***")
punto_1 = (1,0)
punto_2 = (5,3)
#desempaquetado de tuplas

x1, y1 = punto_1
x2, y2 = punto_2

#Expresion de una recta y = mx + b

m = (y2 - y1) / (x2 -x1)
b = y1 - m * x1

print(f"Expresion de la recta es: y = {m}x + ({b})")
#punto_1[0] = 2

