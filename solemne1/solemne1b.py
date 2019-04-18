#!/bin/python
# -*- coding: utf-8 -*-

import platform
import os
import re


def run():
    patient_name = input("Ingrese el nombre del paciente: ")
    while patient_name == "":
        print("No ha ingresado un nombre válido, intente nuevamente.")
        patient_name = input("Ingrese el nombre del paciente: ")
    rut = input("Ingrese el rut del paciente: ")
    while rut == "":  # TODO: posiblemente revisar rut con regex para validarlo
        print("No ha ingresado un rut válido, intente nuevamente.")
        rut = input("Ingrese el rut del paciente: ")
    age = -1
    while not isint(age) or age <= 0:
        if not isint(age) and age != -1:
            print("No ha ingresado una edad válida, intente nuevamente.")
        age = input("Ingrese la edad del paciente: ")
        if isint(age):
            age = int(age)
    genres = ["Masculino", "Femenino", "Otro"]
    genre = input("Ingrese el sexo del paciente: ")
    while genre not in genres:
        print("No ha ingresado un sexo válido, intente nuevamente. Valores permitidos:")
        for g in genres:
            print(" - " + g)
        genre = input("Ingrese el sexo del paciente: ")
    paid_amount = -1
    while not isint(paid_amount) or paid_amount <= 0:
        if not isint(paid_amount)and paid_amount != -1:
            print("No ha ingresado un monto válido a pagar, intente nuevamente.")
        paid_amount = input("Ingrese el monto a pagar: ")
        if isint(paid_amount):
            paid_amount = int(paid_amount)

    out = """
    Información consulta:
    
        Información Paciente:
          Nombre Paciente: {}
          Rut Paciente: {}
          Edad Paciente: {}
          Sexo Paciente: {}
        Información Finanzas:
          Monto Pagado: {}
          Comisión Centro Médico: {}
          Comisión Doctor(a): {}
          Gastos Arriendo: {}
          Gastos Estudios Estadísticos: {}
    """.format(patient_name, rut, age, genre, paid_amount, percent(paid_amount, 40), percent(paid_amount, 30),
               percent(paid_amount, 20), percent(paid_amount, 10))
    print(out)


def isint(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


def percent(i, p):
    return (i * p) / 100


def clear():
    name = re.sub(r"[^\w]+", "", platform.system())
    if "Windows" in name:
        os.system("cls")
    else:
        os.system("clear")


if __name__ == '__main__':
    try:
        while True:
            clear()
            run()
            input("Presione cualquier tecla para continuar...")
    except KeyboardInterrupt:
        print("Saliendo del programa.")
        exit(0)
