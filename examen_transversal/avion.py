import re

"""
TODO:
- Cada asiento está asociado al rut de la persona que lo usará
"""

letra_asientos = ["A", "B", "C", "D", "E", "F"]
asientos = []


def init():
    for i in range(6):
        fila = []
        for j in range(33):
            fila.append(None)
        asientos.append(fila)
    print_asientos()
    while True:
        asignar_asiento()
        print_asientos()


def is_run(run: str) -> bool:
    return re.fullmatch(r"\d{7,8}", normalize_run(run)) is not None


def normalize_run(run: str) -> str:
    return run.replace(".", "").split("-")[0][0:8]


def prettify_run(run: str) -> str:
    dv = calc_dv_run(run)
    if len(run) == 8:
        return run[0:2] + "." + run[2:5] + "." + run[5:8] + "-" + dv
    else:
        return run[0:1] + "." + run[1:4] + "." + run[4:7] + "-" + dv


def calc_dv_run(run: str) -> str:
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
            linea += "[" + ("-" if asientos[n_fila][n_asiento] is None else "X") + ("] " if n_asiento < 9 else "]  ")
        print(linea)
        if n_fila == 2:
            print("   |1| |2| |3| |4| |5| |6| |7| |8| |9| |10| |11| |12| |13| |14| |15| |16| |17| |18| |19| |20| |21| |"
                  "22| |23| |24| |25| |26| |27| |28| |29| |30| |31| |32| |33|")


def is_empty(fila: int, asiento: int) -> bool:
    return asientos[fila - 1][asiento * fila - 1] is None


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
    right = validate_y_or_n(input("Es correcto: "))
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
    return int(fila)


def request_asiento(failed: bool = False) -> int:
    if failed:
        print("No ha ingresado un asiento válido.")
    asiento = input("Ingrese asiento: ").upper()
    if asiento in letra_asientos:
        asiento = asiento_to_int(asiento)
    else:
        return request_asiento(failed=True)
    return asiento


def asignar_asiento() -> None:
    run = request_run()
    fila = request_fila()
    asiento = request_asiento()
    asientos[asiento][fila - 1] = run


def is_int(x: str) -> bool:
    try:
        int(x)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    init()
