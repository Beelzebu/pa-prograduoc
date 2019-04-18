# -*- coding: utf-8 -*-
# Script en python para calcular el promedio de un alumno


def is_invalid(nota):
    try:
        notaf = float(nota)
        if 1 <= notaf <= 7:
            return notaf
        else:
            return True
    except ValueError:
        return True


asignatura = input("Ingresa el nombre de la asignatura: ")
semestre = is_invalid(input("Ingresa el número de semestre: "))

if semestre is True:
    print("Semestre inválido")
    input()
    exit(1)
elif semestre == 1:
    semestre = "Primero"
elif semestre == 2:
    semestre = "Segundo"
elif semestre == 3:
    semestre = "Tercero"
elif semestre == 4:
    semestre = "Cuarto"
else:
    print("Semestre inválido")
    input()
    exit(1)

nota1 = is_invalid(input("Ingresa la primera nota: ").replace(",", "."))
if nota1 is True:
    print("No has ingresado un valor válido, saliendo...")
    input()
    exit(1)
nota2 = is_invalid(input("Ingresa la segunda nota: ").replace(",", "."))
if nota2 is True:
    print("No has ingresado un valor válido, saliendo...")
    input()
    exit(1)
nota3 = is_invalid(input("Ingresa la tercera nota: ").replace(",", "."))
if nota3 is True:
    print("No has ingresado un valor válido, saliendo...")
    input()
    exit(1)

promedio = (nota1 + nota2 + nota3) / 3
estado = "Aprobado con distinción" if promedio > 6.6 else "Aprobado" if promedio >= 4 else "Reprobado"

print("""
    Asignatura: {}
    Promedio: {}
    Semestre: {}
    Estado: {}
    """.format(asignatura, "{0:.1f}".format(promedio), semestre, estado))

input()
