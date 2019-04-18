from .people import Persona


class Ficha:
    def __init__(self, paciente, fecha, hora, personal_ingreso):
        self.id = -1
        if not isinstance(paciente, Persona):
            raise ValueError("paciente is not an instance of Persona")
        self.paciente = paciente
        self.fecha = fecha
        self.hora = hora
        if not isinstance(personal_ingreso, Persona):
            raise ValueError("personal_ingreso is not an instance of Persona")
        self.personal_ingreso = personal_ingreso
