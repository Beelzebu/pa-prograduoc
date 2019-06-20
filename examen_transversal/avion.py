# -*- coding: utf-8 -*-
import os
import platform
import re

letra_asientos = ["A", "B", "C", "D", "E", "F"]
asientos = []
asientos_espacio_adicional = [0, 1, 2, 3, 4, 17]
asientos_no_reclinables = [9, 10, 11, 12, 13, 14, 15, 16]


def init() -> None:
    """
    Función principal del programa, debe ser ejecutada al iniciarse el programa para preparar las variables
    requeridas por otras funciones para ser ejecutadas
    """
    for i in range(6):  # rellenar la matriz de asientos con 198 valores (6*33)
        fila = []
        for j in range(33):
            fila.append(None)
        asientos.append(fila)
    menu()


def menu() -> None:
    while True:
        clear()
        print("[1] Compra de pasaje")
        print("[2] Listado de pasajeros")
        print("[3] Mostrar ubicaciones disponibles")
        print("[4] Buscar pasajero")
        print("[5] Reasignar asiento")
        print("[6] Mostrar ganancias totales")
        print("[7] Salir del programa")
        opcion = int_in_range(x=input("Ingrese una opción: "), min_n=1, max_n=7)
        if opcion == 1:
            comprar_asientos()
        elif opcion == 2:
            for pasajero in lista_pasajeros():
                print(prettify_run(pasajero))
            input("Presione enter para volver al menú principal.")
        elif opcion == 3:
            print_asientos()
            input("Presione enter para volver al menú principal.")
        elif opcion == 4:
            run = request_run()
            ubicacion = buscar_pasajero(run)
            if ubicacion is None:
                print("El pasajero solicitado no tiene asientos comprados.")
            else:
                print("El pasajero tiene comprado el asiento " + asiento_to_str(ubicacion[0]) + " en la fila " + str(
                    ubicacion[1] + 1))
            input("Presione enter para volver al menú principal.")
        elif opcion == 5:
            reasignar_asiento(request_run())
            input("Presione enter para volver al menú principal.")
        elif opcion == 6:
            print("Ganancias totales hasta el momento: $" + str(ganancias()))
            input("Presione enter para volver al menú principal.")
        elif opcion == 7:
            exit(0)


def clear() -> None:
    """Clear console, should work on Windows and *nix"""
    name = re.sub(r"[^\w]+", "", platform.system()).lower()
    if "windows" in name:
        os.system("cls")
    else:
        os.system("clear")


def lista_pasajeros() -> list:
    pasajeros = []
    for fila in asientos:
        for run in fila:
            if run is not None:
                pasajeros.append(run)
    pasajeros.sort()
    return pasajeros


def buscar_pasajero(run: str) -> tuple:
    for n_fila in range(6):
        for n_asiento in range(33):
            if asientos[n_fila][n_asiento] == run:
                return n_fila, n_asiento
    return None


def reasignar_asiento(run: str) -> None:
    print_asientos()
    ubicacion_anterior = buscar_pasajero(run)
    if ubicacion_anterior is None:
        print("El pasajero no ha comprado ningún asiento.")
    else:
        asientos[ubicacion_anterior[0]][ubicacion_anterior[1]] = None
        fila = request_fila()
        asiento = request_asiento()
        while not is_empty(fila, asiento):
            print("La ubicación solicitada está ocupada, intente nuevamente...")
            fila = request_fila()
            asiento = request_asiento()
        asientos[asiento][fila] = run


def is_run(run: str) -> bool:
    """
    Verifica si el string pasado es un RUN válido o no, la forma de validarlo es dividir el string en 2, obtener la
    primera parte, eliminar lo que no sea un número y verificar si el largo del resultado es 7 u 8, un RUN de menos de
    10 millones tiene un largo de 7 sin puntos ni dígito verificador y uno de 10 millones o más, un largo de 8.

    :param run: String para validar como RUN.
    :return: True si el argumento pasado es un RUN, Falso de otra forma.
    """
    return re.fullmatch(r"\d{7,8}", normalize_run(run)) is not None


def normalize_run(run: str) -> str:
    """
    Normalización de un texto normal que debería representar un RUN, a un RUN sin puntos, guión ni dígito verificador.

    :param run: String para transformar a RUN sin puntos, guión ni dígito verificador.
    :return: String de un máximo de 8 caracteres que representa un RUN sin puntos, guiones ni dígito verificador.
    """
    return re.sub(pattern=r"[^\d]", repl="", string=run.split(sep="-", maxsplit=2)[0])[0:8]


def prettify_run(run: str) -> str:
    """
    Decoración de RUN sin puntos, guión ni dígito verificador, esta función agrega puntos, guión y agrega el dígito
    verificador calculado en base al RUN.

    :param run: RUN para decorar, se espera un str de 7 u 8 caracteres compuesto únicamente de números.
    :return: RUN decorado.
    """
    dv = calc_dv_run(run)
    if len(run) == 8:
        return run[0:2] + "." + run[2:5] + "." + run[5:8] + "-" + dv
    else:
        return run[0:1] + "." + run[1:4] + "." + run[4:7] + "-" + dv


def calc_dv_run(run: str) -> str:
    """
    Función para calcular el dígito verificador de un RUN.

    :param run: RUN sin puntos ni guión (ni dígito verificador), para calcular el dígito verificador.
    :return: Dígito verificador del RUN, número entre 0 y 9 o K.
    """
    numeros = []
    for i in run[::-1]:
        numeros.append(int(i))
    multiplicador = 2
    for i in range(len(numeros)):
        if multiplicador > 7:
            multiplicador = 2
        numeros[i] = numeros[i] * multiplicador
        multiplicador += 1
    suma = 0
    for i in numeros:
        suma += i
    resto = suma % 11
    dv = 11 - resto
    if dv == 11:
        return "0"
    elif dv == 10:
        return "K"
    else:
        return str(dv)


def asiento_to_str(fila: int) -> str:
    if fila == 0:
        return "F"
    elif fila == 1:
        return "E"
    elif fila == 2:
        return "D"
    elif fila == 3:
        return "C"
    elif fila == 4:
        return "B"
    elif fila == 5:
        return "A"


def asiento_to_int(fila: str) -> int:
    fila = fila.upper()
    if fila == "A":
        return 5
    elif fila == "B":
        return 4
    elif fila == "C":
        return 3
    elif fila == "D":
        return 2
    elif fila == "E":
        return 1
    elif fila == "F":
        return 0


def print_asientos() -> None:
    for n_fila in range(len(asientos)):
        linea = asiento_to_str(n_fila) + ": "
        for n_asiento in range(len(asientos[n_fila])):
            linea += "[" + ("-" if asientos[n_fila][n_asiento] is None or asientos[n_fila][n_asiento] is 0 else "X") + (
                "] " if n_asiento < 9 else "]  ")
        print(linea)
        if n_fila == 2:
            print("   |1| |2| |3| |4| |5| |6| |7| |8| |9| |10| |11| |12| |13| |14| |15| |16| |17| |18| |19| |20| |21| |"
                  "22| |23| |24| |25| |26| |27| |28| |29| |30| |31| |32| |33|")


def is_empty(fila: int, asiento: int) -> bool:
    return asientos[asiento][fila] is None or asientos[asiento][fila] is 0


def validate_y_or_n(input_to_validate: str):
    if len(input_to_validate) != 0:
        input_to_validate = input_to_validate.upper()[0]
    if input_to_validate == "Y" or input_to_validate == "S":
        return True
    elif input_to_validate == "N":
        return False
    else:
        print("No ha ingresado una opción válida (S o N)")
        return validate_y_or_n(input("Ingrese una opción (S o N): "))


def request_run(failed: bool = False) -> str:
    if failed:
        print("No ha ingresado un run válido.")
    run = input("Ingrese run: ")
    if not is_run(run):
        return request_run(failed=True)
    run = normalize_run(run=run)
    print("Usando run: " + prettify_run(run=run))
    right = validate_y_or_n(input("¿Es correcto?: "))
    if not right:
        return request_run()
    else:
        return run


def request_fila(failed: bool = False) -> int:
    if failed:
        print("No ha ingresado una fila válida.")
    fila = input("Ingrese fila: ")
    if not is_int(fila):
        return request_fila(failed=True)
    return int(fila) - 1


def request_asiento(failed: bool = False) -> int:
    if failed:
        print("No ha ingresado un asiento válido.")
    asiento = input("Ingrese asiento: ").upper()
    if asiento in letra_asientos:
        asiento = asiento_to_int(asiento)
    else:
        return request_asiento(failed=True)
    return asiento


def price_for(fila: int) -> int:
    if fila in asientos_espacio_adicional:
        return 80000
    elif fila in asientos_no_reclinables:
        return 50000
    else:
        return 60000


def ganancias() -> int:
    total = 0
    for n_fila in range(6):
        for n_asiento in range(33):
            run = asientos[n_fila][n_asiento]
            if run is not None:
                total += price_for(fila=n_fila)
    return total


def asignar_asiento() -> tuple:
    run = request_run()
    fila = request_fila()
    asiento = request_asiento()
    while not is_empty(fila, asiento):
        print("El asiento solicitado ya está ocupado, intente nuevamente.")
        fila = request_fila()
        asiento = request_asiento()
    asientos[asiento][fila] = run
    return run, fila, asiento, price_for(fila=fila)


def is_int(x: str) -> bool:
    try:
        int(x)
        return True
    except ValueError:
        return False


def int_in_range(x: str, min_n: int, max_n: int, err_msg="No ha ingresado una opción válida, reintente: ") -> int:
    """Transform x to int if is in the requested range or force the user to input until provide a valid number"""
    while not is_int(x) or (int(x) < min_n or int(x) > max_n):
        x = input(err_msg)
        if is_int(x):
            x = int(x)
            if x < min_n or x > max_n:
                x = ""
    return int(x)


def asientos_libres() -> int:
    i = 0
    for fila in asientos:
        for asiento in fila:
            if asiento is None or asiento is 0:
                i += 1
    return i


def comprar_asientos() -> None:
    print_asientos()
    asientos_reservados = []
    disponibles = asientos_libres()
    if disponibles < 1:
        print("No quedan asientos disponibles en este vuelo.")
        return None
    cantidad = int_in_range(x=input("Ingrese la cantidad de asientos a comprar: "), min_n=1, max_n=disponibles,
                            err_msg="No ha ingresado una cantidad válida, reintente: ")
    deuda = 0
    comprados = 0
    while cantidad > comprados:
        print("Comprando asiento: " + str(comprados + 1))
        comprados += 1
        asientos_reservados.append(asignar_asiento())
    for asiento_reservado in asientos_reservados:
        deuda += asiento_reservado[3]
    print_asientos()
    print("Valor a pagar: $" + str(deuda))
    pago = int_in_range(x=input("Ingrese monto a pagar: "), min_n=1, max_n=999999999999999,
                        err_msg="Ha ingresado un valor invalido, reintente: ")
    if pago < deuda:
        print("El dinero no es suficiente para pagar los asientos, eliminando reserva temporal de asientos.")
        for asiento_reservado in asientos_reservados:
            fila = asiento_reservado[2]
            asiento = asiento_reservado[1]
            asientos[fila][asiento] = None
    else:
        if pago > deuda:
            print("Vuelto: $" + str(pago - deuda))
    input("Presione enter para continuar...")


# Inicio del programa, si el archivo se ejecuta de forma independiente python asigna el valor "__main__" a la
# variable "__name__"
if __name__ == '__main__':
    # Función principal del programa que ejecuta el resto del código
    init()
