# -*- coding: utf-8 -*-

import os
import platform
import re
import sys
import time

from fichas_medicas.ficha import Ficha
from fichas_medicas.medicine import (Lidocaina, Omeprazol, Paracetamol, Penicilina, Salbutamol)
from fichas_medicas.people import (Acompaniante, Medico, Paciente, Personal)

this = sys.modules[__name__]
this.ficha_actual = None
this.fichas = {}


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
                            input("Dirección: "), input("Estado civil: "), input("Sexo: "), int(input("Edad: ")))
        while 0 < paciente.edad > 120:
            paciente.edad = int(input("Ha ingresado una edad inválida, ingrese nuevamente: "))
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
        ficha.id = len(fichas) + 1
        this.fichas[ficha.id] = ficha
        this.ficha_actual = ficha
        print("Se han ingresado los siguientes datos de atención correctamente: ")
        print(str(ficha))
        print("Id de ficha: " + str(ficha.id))
        input()

    elif option == 2:
        if this.ficha_actual is None:
            print("Aún no se ha ingresado ninguna ficha, por favor ingrese los datos del paciente.")
            time.sleep(5)
            run()
        else:
            print("Ingrese los datos del médico: \n")
            this.ficha_actual.medico = Medico(input("Nombre: "), input("Apellido: "), int(input("RUN: ")),
                                              input("Titulo: "),
                                              input("Institución egreso: "), input("Fecha de titulación: "),
                                              int(input("Teléfono: ")), input("Dirección: "), input("Especialidad: "))
            this.fichas[this.ficha_actual.id] = this.ficha_actual
            print(this.ficha_actual)
            input()
    elif option == 3:
        medicamentos_str = """Seleccione el tipo de medicamento:

                1) Parcetamol
                2) Lidocaína
                3) Omeprazol
                4) Penicilina
                5) Salbutamol
                """
        medicamento_opt = input(medicamentos_str)
        while not isint(medicamento_opt) or 1 > medicamento_opt > 5:
            medicamento_opt = input(medicamentos_str)
            if not isint(option):
                input("No ha ingresado una opción válida, reintente...")
                continue
            else:
                medicamento_opt = int(medicamento_opt)
        medicamento = None
        if medicamento_opt == 1:
            medicamento = Paracetamol(int(input("Ha seleccionado paracetamol, ingrese la cantidad")))
        elif medicamento_opt == 2:
            medicamento = Lidocaina(int(input("Ha seleccionado lidocaína, ingrese la cantidad")))
        elif medicamento_opt == 3:
            medicamento = Omeprazol(int(input("Ha seleccionado omeprazol, ingrese la cantidad")))
        elif medicamento_opt == 4:
            medicamento = Penicilina(int(input("Ha seleccionado penicilina, ingrese la cantidad")))
        elif medicamento_opt == 5:
            medicamento = Salbutamol(int(input("Ha seleccionado salbutamol, ingrese la cantidad")))
        this.ficha_actual.paciente.add_medicine(medicamento)
        this.fichas[this.ficha_actual.id] = this.ficha_actual
        print(this.ficha_actual)
        input()
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
