import re

"""
TODO:
- Cada asiento está asociado al rut de la persona que lo usará
"""

asientos = []


def init():
    for i in range(6):
        fila = []
        for j in range(33):
            fila.append(None)
        asientos.append(fila)
    print_asientos()


def is_run(run: str) -> bool:
    return re.fullmatch(r"\d{7,8}", normalize_run(run)) is not None


def normalize_run(run: str) -> str:
    return run.replace(".", "").split("-")[0][0:8]


def print_asientos():
    for n_fila in range(len(asientos)):
        linea = ""
        if n_fila == 0:
            linea += "F: "
        elif n_fila == 1:
            linea += "E: "
        elif n_fila == 2:
            linea += "D: "
        elif n_fila == 3:
            linea += "C: "
        elif n_fila == 4:
            linea += "B: "
        elif n_fila == 5:
            linea += "A: "
        for n_asiento in range(len(asientos[n_fila])):
            linea += "[" + ("-" if asientos[n_fila][n_asiento] is None else "X") + ("] " if n_asiento < 9 else "]  ")
        print(linea)
        if n_fila == 2:
            print("   |1| |2| |3| |4| |5| |6| |7| |8| |9| |10| |11| |12| |13| |14| |15| |16| |17| |18| |19| |20| |21| |"
                  "22| |23| |24| |25| |26| |27| |28| |29| |30| |31| |32| |33|")


def comprar_asiento(fila, linea, run):
    if is_run(run):
        print("Es válido")
        print(normalize_run(run))
        asientos[fila - 1][linea - 1] = normalize_run(run)
    else:
        print("Es inválido")


if __name__ == '__main__':
    init()
    while True:
        fila = input("Ingrese fila: ").upper()
        if fila == "A":
            fila = 6
        elif fila == "B":
            fila = 5
        elif fila == "C":
            fila = 4
        elif fila == "D":
            fila = 3
        elif fila == "E":
            fila = 2
        elif fila == "F":
            fila = 1
        comprar_asiento(fila, int(input("Ingrese asiento: ")), input("Ingrese run: "))
        print_asientos()
