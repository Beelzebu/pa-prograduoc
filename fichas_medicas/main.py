# -*- coding: utf-8 -*-

import os
import platform
import re
import time


def run():
    clear()
    out = """Bienvenido al programa, optiones disponibles:

    1)
    2)
    3)
    4)
    5) Salir del programa
    """
    print(out)
    option = input("Seleccione una opción: ")
    if not isint(option):
        input("No ha ingresado una opción válida, presione enter para reintentar...")
        run()
    else:
        option = int(option)

    if option == 1:
        print("")
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
        print("")


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
