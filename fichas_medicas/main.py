# -*- coding: utf-8 -*-

import os
import platform
import re
import time

from fichas_medicas.ficha import Ficha
from fichas_medicas.people import Acompaniante
from fichas_medicas.people import Paciente
from fichas_medicas.people import Personal

fichas = []


def run():
    clear()
    options_str = """Bienvenido al programa, optiones disponibles:

    1) Ingresar ficha del paciente
    2) Actualizar ficha por el médico
    3) Asignación de medicamentos
    4) Obtención de estadísticas
    5) Salir
    """
    print(options_str)
    option = input("Seleccione una opción: ")
    if not isint(option):
        input("No ha ingresado una opción válida, presione enter para reintentar...")
        run()
    else:
        option = int(option)

    if option == 1:
        print("Ha seleccionado ingresar los datos del paciente, a continuación se le solicitarán los datos para "
              "rellenar la ficha de forma automática.")
        paciente = Paciente(input("Nombre: "), input("Apellido: "), int(input("RUN: ")), int(input("Teléfono: ")),
                            input("Dirección: "), input("Estado civil: "))
        acompaniante = None
        if input("¿El paciente viene acompañado?: ").lower() == "si":
            print("Por favor ingrese los datos del acompañante: ")
            acompaniante = Acompaniante(input("Nombre: "), input("Apellido: "), int(input("RUN: ")),
                                        input("Parentesco con el paciente: "), int(input("Teléfono: ")))
        print("Por favor ingrese los datos del personal que realizó el ingreso de datos:")
        personal = Personal(input("Nombre: "), input("Apellido: "), int(input("RUN: ")), input("Título: "),
                            input("Institución de egreso: "), input("Fecha de titulación: "), int(input("Teléfono: ")),
                            input("Dirección: "))
        print("Por favor ingrese la fecha y hora: ")
        ficha = Ficha(paciente, acompaniante, personal, input("Fecha: "), input("Hora: "))
        fichas.append(ficha)
        print("Se han ingresado los datos de atención correctamente: ")
        print(str(ficha))
        print("Id de ficha:" + str(len(fichas)))
        input()

    elif option == 2:
        print("")
    elif option == 3:
        print("")
    elif option == 4:
        print("")
    elif option == 5:
        print("Saliendo del programa...")
        time.sleep(5)
        exit(0)
    else:
        print("Opción inválida, reintente.")


def isint(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


def clear():
    name = re.sub(r"[^\w]+", "", platform.system()).lower()
    if "windows" in name:
        os.system("cls")
    else:
        os.system("clear")


if __name__ == '__main__':
    while True:
        try:
            run()
        except KeyboardInterrupt:
            exit(0)
