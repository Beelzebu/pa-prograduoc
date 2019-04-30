# -*- coding: utf-8 -*-

import os
import platform
import re
from enum import Enum


class Sexo(Enum):
    MASCULINO = "M"
    FEMENINO = "F"


class Persona:

    def __init__(self, edad: int, sexo: Sexo):
        self.__edad__: int = edad
        self.__sexo__: Sexo = sexo

    def edad(self) -> int:
        return self.__edad__

    def sexo(self) -> Sexo:
        return self.__sexo__


def run() -> None:
    personas: int = toint(input("Ingrese el número de personas que serán ingresadas: "))
    if not isint(personas):
        print("No se ha ingresado un valor válido, reintente...")
        run()
    else:
        personas_ingresadas: list = []
        ingresadas: int = 0

        while ingresadas < personas:
            edad: int = toint(input("Edad: "))
            while not isint(edad):
                edad = toint(input("No se ha ingresado una edad válida, ingrese nuevamente: "))
            sexo_input: str = input("Sexo (M o F): ").lower()
            while not (sexo_input == "m" or sexo_input == "f"):
                sexo_input = input("No ha ingresado un sexo válido, ingrese nuevamente (M o F): ")
            sexo: Sexo
            if sexo_input == "m":
                sexo = Sexo.MASCULINO
            elif sexo_input == "f":
                sexo = Sexo.FEMENINO
            else:
                print("Ha ocurrido un error inesperado.")
                continue
            persona: Persona = Persona(edad, sexo)
            personas_ingresadas.append(persona)

            ingresadas += 1

            if (persona.sexo() == Sexo.MASCULINO and persona.edad() >= 65) or (
                    persona.sexo() == Sexo.FEMENINO and persona.edad() >= 60):
                print("Debe jubilar")
            else:
                print("Aún no debe jubilar")

        hombres_a_jubilar: int = 0
        mujeres_a_jubilar: int = 0
        total_a_jubilar: int = 0
        for persona in personas_ingresadas:
            persona: Persona = persona
            if persona.sexo() == Sexo.MASCULINO and persona.edad() >= 65:
                hombres_a_jubilar += 1
                total_a_jubilar += 1
            elif persona.sexo() == Sexo.FEMENINO and persona.edad() >= 60:
                mujeres_a_jubilar += 1
                total_a_jubilar += 1
        for x in range(3):
            print("")
        print("Personas ingresadas: {}".format(len(personas_ingresadas)))
        print("Total de personas que deben jubilar: {}".format(total_a_jubilar))
        print("Hombres que deben jubilar: {}".format(hombres_a_jubilar))
        print("Mujeres que deben jubilar: {}".format(mujeres_a_jubilar))
        print("Promedio de personas que deben jubilar: {}%".format((total_a_jubilar / len(personas_ingresadas)) * 100))
        input("Presione enter para continuar...")
        clear()


def isint(x: any) -> bool:
    try:
        int(x)
        return True
    except ValueError:
        return False


def toint(x: any):
    return int(x) if isint(x) else x


def is_in_range(x: any, rmin: int, rmax: int) -> bool:
    x = toint(x)
    return rmin - 1 < x < rmax + 1 if isint(x) else False


def clear() -> None:
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
