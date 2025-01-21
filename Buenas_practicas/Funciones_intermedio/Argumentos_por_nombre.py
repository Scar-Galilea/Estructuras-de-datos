#Galilea Peralta Contreras.
#08 de enero de 2025.
#Descripción:
#Este programa calcula la suma acumulativa desde 0 hasta un número ingresado por el usuario.


def imprimir_alumno(nombre:str="hola",edad:int=64,matricula:int=6464646,grupo:int=303,*,semestre:int = 3) -> None:
    print("Datos personales")
    print(f"Nombre: {nombre}.")
    print(f"Edad: {edad}.")
    print(f"Matricula: {matricula}.")
    print(f"Grupo: {grupo}")
    print(f"Semestre: {semestre}")

def main() -> None:
    if __name__ == '__main__':
        nombre = "Galilea"
        edad = 17
        matricula = 1635674
        grupo = 303
        semestre = 3
        #imprimir_alumno(nombre,edad,matricula,grupo)
        #imprimir_alumno("g",5,775,7)
        print()
        #imprimir_alumno(nombre = "Scarlett",matricula=1233,edad=19,grupo=202,semestre=300)
        print()

main()
