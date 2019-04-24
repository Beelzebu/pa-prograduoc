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
        self.medico = None
        self.sintomas = ""
        self.diagnostico = ""
        self.reposo = False
        self.reposo_dias = 0

    def __str__(self):
        asd = "---------------\nFicha de atención:---------------\n\n\n" \
              "{}\n" \
              "{}" \
              "{}\n" \
              "{}\n" \
              "{}\n" \
              "{}" \
              "{}\n" \
              "{}" \
              "{}".format(self.paciente, self.acompaniante if self.acompaniante is not None else "",
                          self.personal_ingreso, self.fecha, self.hora, self.medico if self.medico is not None else "")
        return str(self.paciente) + "\n" + str(self.acompaniante) if self.acompaniante is not None else "" + str(
            self.personal_ingreso) + "\nFecha: " + self.fecha + "\nHora: " + self.hora + ("\n" + str(
            self.medico)) if self.medico is not None else "" + "\nSintomas: " + self.sintomas + "\nReposo: " + "Si" if self.reposo else "No" + (
                "\nDías de reposo: " + str(self.reposo_dias)) if self.reposo else ""
