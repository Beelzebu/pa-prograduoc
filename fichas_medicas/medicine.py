# -*- coding: utf-8 -*-


class Medicamento:

    def __init__(self, nombre: str, descripcion: str, cantidad: int):
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad


class Paracetamol(Medicamento):

    def __init__(self, cantidad: int):
        super().__init__("Paracetamol", "Fármaco con propiedades analgésicas y antipiréticas", cantidad)


class Lidocaina(Medicamento):

    def __init__(self, cantidad: int):
        super().__init__("Lidocaína", "Fármaco perteneciente a la familia de los anestésicos locales, concretamente "
                                      "del tipo de las amino amidas", cantidad)


class Omeprazol(Medicamento):

    def __init__(self, cantidad: int):
        super().__init__("Omeprazol", "Fármaco utilizado para tratar el reflujo gastroesofágico", cantidad)


class Penicilina(Medicamento):
    def __init__(self, cantidad: int):
        super().__init__("Penicilina", "Antibióticos del grupo de los betalactámicos empleados profusamente en el "
                                       "tratamiento de infecciones provocadas por bacterias sensibles", cantidad)


class Salbutamol(Medicamento):

    def __init__(self, cantidad: int):
        super().__init__("Salbutamol", "Agonista β2 adrenérgico de efecto rápido utilizado para el alivio del "
                                       "broncoespasmo en padecimientos como el asma y la enfermedad pulmonar "
                                       "obstructiva crónica", cantidad)
