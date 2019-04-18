from .people import Paciente
from .people import Personal


class Ficha:
    def __init__(self, paciente, fecha, hora, personal_ingreso):
        self.id = -1
        if not isinstance(paciente, Paciente):
            raise ValueError("paciente is not an instance of Persona")
        self.paciente = paciente
        self.fecha = fecha
        self.hora = hora
        if not isinstance(personal_ingreso, Personal):
            raise ValueError("personal_ingreso is not an instance of Persona")
        self.personal_ingreso = personal_ingreso
