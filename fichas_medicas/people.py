# -*- coding: utf-8 -*-
from fichas_medicas.database import Serializable


class Humano(Serializable):
    def __init__(self, nombre: str, apellido: str, run: int):
        self.nombre = nombre
        self.apellido = apellido
        self.run = run

    def query(self) -> str:
        raise NotImplementedError

    def values(self) -> str:
        raise NotImplementedError


class Paciente(Humano):

    def __init__(self, nombre: str, apellido: str, run: int, telefono: int, direccion: str, estado_civil: str):
        super().__init__(nombre, apellido, run)
        self.telefono = telefono
        self.direccion = direccion
        self.estado_civil = estado_civil

    def query(self) -> str:
        return "INSERT INTO 'mydb'.'paciente' VALUES (?, ?, ?, ?, ?, ?)"

    def values(self) -> str:
        return self.run, self.nombre, self.apellido, self.telefono, self.direccion, self.estado_civil

    def __str__(self):
        return "Nombre paciente: " + self.nombre + "\nApellido paciente: " + self.apellido + "\nRUN paciente: " + str(
            self.run) + "\nTeléfono paciente: " + str(self.telefono) + "\nEstado civil paciente: " + self.estado_civil


class Acompaniante(Humano):

    def __init__(self, nombre: str, apellido: str, run: int, parentesco: str, telefono: int):
        super().__init__(nombre, apellido, run)
        self.parentesco = parentesco
        self.telefono = telefono

    def query(self) -> str:
        raise NotImplementedError

    def values(self) -> str:
        raise NotImplementedError

    def __str__(self):
        return "Nombre acompañante: " + self.nombre + "\nApellido acompañante: " + self.apellido + \
               "\nRUN acompáñante: " + str(self.run) + "\nTeléfono acompañante: " + \
               str(self.telefono) + "\nParentesco con paciente: " + self.parentesco


class Personal(Humano):

    def __init__(self, nombre: str, apellido: str, run: int, titulo: str, institucion_egreso: str,
                 fecha_titulacion: str, telefono: int, direccion: str):
        super().__init__(nombre, apellido, run)
        self.titulo = titulo
        self.institucion_egreso = institucion_egreso
        self.fecha_titulacion = fecha_titulacion
        self.telefono = telefono
        self.direccion = direccion

    def query(self) -> str:
        raise NotImplementedError

    def values(self) -> str:
        raise NotImplementedError


class Medico(Personal):

    def __init__(self, nombre, apellido, run, titulo, institucion_egreso, fecha_titulacion, telefono, direccion,
                 especialidad):
        super().__init__(nombre, apellido, run, titulo, institucion_egreso, fecha_titulacion, telefono, direccion)
        self.especialidad = especialidad

    def query(self) -> str:
        return "INSERT INTO 'mydb'.'medico' VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"

    def values(self) -> str:
        return self.nombre, self.apellido, self.run, self.titulo, self.institucion_egreso, self.fecha_titulacion, self.telefono, self.direccion, self.especialidad
