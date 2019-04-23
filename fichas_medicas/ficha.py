# -*- coding: utf-8 -*-
from fichas_medicas.people import Acompaniante
from fichas_medicas.people import Paciente
from fichas_medicas.people import Personal


class Ficha:
    def __init__(self, paciente: Paciente, acompaniante: Acompaniante, personal_ingreso: Personal, fecha: str,
                 hora: str):
        self.id = -1
        if not isinstance(paciente, Paciente):
            raise ValueError("paciente is not an instance of Persona")
        self.paciente = paciente
        if not isinstance(personal_ingreso, Personal):
            raise ValueError("personal_ingreso is not an instance of Persona")
        if not isinstance(acompaniante, Acompaniante) and acompaniante is not None:
            raise ValueError("acompaniante is not an instance of Acompaniante")
        self.acompaniante = acompaniante
        self.personal_ingreso = personal_ingreso
        self.fecha = fecha
        self.hora = hora

    def __str__(self):
        return str(self.paciente) + "\n" + str(self.acompaniante) if self.acompaniante is not None else "" + str(
            self.personal_ingreso) + "\nFecha: " + self.fecha + "\nHora: " + self.hora
