#Galilea Peralta Contreras.
#08 de enero de 2025.
#Descripción:
#Este programa calcula la suma acumulativa desde 0 hasta un número ingresado por el usuario.


def colores_favoritos (persona:str,*vargs):
    print(f"{persona} : {vargs}")
    cadena = "Hola"
    tupla = "Hola",
    print(cadena)
    print(tupla)

def sumar(* vargs) -> int :
    resultado = 0
    for i in vargs:
         resultado += i

    return resultado

if __name__ == '__main__':
    colores_favoritos("Jenifer","Morados","Negro","BLanco","Rosa")
    colores_favoritos("Addi","Azul","Blanco","Negro")
    colores_favoritos("Galilea", "Violetta")
    res = sumar(5, 3, 4)
    print(res )





