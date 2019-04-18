# -*- coding: utf-8 -*-
# Script en python para calcular el crédito de un grupo de casas en base al pie ingresado

class Main:
    def __init__(self):
        super().__init__()

    def run(self):
        self.calc_credit()

    def calc_credit(self):
        try:
            pie = int(input("Ingrese el valor del pie: "))
            casas = []
            casas.append(Casa("A", 80000000, 20, pie))
            casas.append(Casa("B", 75000000, 18, pie))
            casas.append(Casa("C", 70000000, 15, pie))
            for casa in casas:
                print(casa)
        except ValueError:
            print("Debes ingresar un número.")
            self.calc_credit()


class Casa:
    def __init__(self, name, price, credit, pie):
        super().__init__()
        self.name = name
        self.price = price
        self.credit = credit
        self.pie = pie

    def __str__(self):
        total = self.price - self.pie * (self.credit / 1000)
        return "\nTipo Casa " + self.name + "\nValor: $" + str(self.price) + "\nPie: $" + str(
            self.pie) + "\nSaldo: $" + str(self.price - self.pie) + "\nCredito " + str(self.credit) + "%: " + str(
            self.price - self.pie * (self.credit / 100)) + "\nTotal a pagar: $" + str(total)


if __name__ == "__main__":
    main = Main()
    try:
        main.run()
    except KeyboardInterrupt:
        print("Saliendo del programa.")
        exit(0)
