#Galilea Peralta Contreras.
#08 de enero de 2025.
#Descripción:
#Este programa calcula la suma acumulativa desde 0 hasta un número ingresado por el usuario.

def preferencias(tema:str, ** kwargs):
    print(f"El tema es {tema}")

    for key,value in kwargs.items():
        print(f"Nombre: {key} prefiere: {value}")

if __name__ == '__main__':
    preferencias("Comida",Rebeca = "Mole",Juan = "Tacos",Bryan = "Tlayudas")
