# -*- coding: utf-8 -*-
from fichas_medicas.database import Serializable
from fichas_medicas.medicine import Medicamento


class Humano(Serializable):
    def __init__(self, nombre: str, apellido: str, run: int):
        self.nombre = nombre
        self.apellido = apellido
        self.run = run

    def query(self) -> str:
        raise NotImplementedError

    def values(self) -> tuple:
        raise NotImplementedError


class Paciente(Humano):

    def __init__(self, nombre: str, apellido: str, run: int, telefono: int, direccion: str, estado_civil: str,
                 sexo: str, edad: int):
        super().__init__(nombre, apellido, run)
        self.telefono = telefono
        self.direccion = direccion
        self.estado_civil = estado_civil
        self.sexo = sexo
        self.edad = edad
        self.medicamentos = {}

    def query(self) -> str:
        return "INSERT INTO 'mydb'.'paciente' VALUES (?, ?, ?, ?, ?, ?)"

    def values(self) -> tuple:
        return self.run, self.nombre, self.apellido, self.telefono, self.direccion, self.estado_civil

    def add_medicine(self, medicamento: Medicamento):
        self.medicamentos[medicamento.nombre] = medicamento.cantidad

    def __str__(self):
        return "Datos paciente:\nNombre: " + self.nombre + "\nApellido: " + self.apellido + "\nRUN: " + \
               str(self.run) + "\nTeléfono: " + str(self.telefono) + "\nEstado civil: " + \
               self.estado_civil + "\nSexo: " + self.sexo + "\nEdad: " + str(self.edad) + "\nMedicamentos recetados: " + \
               str(self.medicamentos)


class Acompaniante(Humano):

    def __init__(self, nombre: str, apellido: str, run: int, parentesco: str, telefono: int):
        super().__init__(nombre, apellido, run)
        self.parentesco = parentesco
        self.telefono = telefono

    def query(self) -> str:
        raise NotImplementedError

    def values(self) -> tuple:
        raise NotImplementedError

    def __str__(self):
        return "Datos acompañante:\nNombre: " + self.nombre + "\nApellido: " + self.apellido + \
               "\nRUN: " + str(self.run) + "\nTeléfono: " + str(self.telefono) + \
               "\nParentesco con paciente: " + self.parentesco


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

    def values(self) -> tuple:
        raise NotImplementedError

    def __str__(self):
        return "Datos personal:\nNombre: " + self.nombre + "\nApellido: " + self.apellido + \
               "\nRUN: " + str(self.run) + "\nTeléfono: " + str(self.telefono) + "\nTitulo: " + \
               self.titulo + "\nInstitución egreso: " + self.institucion_egreso + "\nFecha titulación: " + \
               self.fecha_titulacion + "\nDirección: " + self.direccion


class Medico(Personal):

    def __init__(self, nombre: str, apellido: str, run: int, titulo: str, institucion_egreso: str,
                 fecha_titulacion: str, telefono: int, direccion: str, especialidad: str):
        super().__init__(nombre, apellido, run, titulo, institucion_egreso, fecha_titulacion, telefono, direccion)
        self.especialidad = especialidad

    def query(self) -> str:
        return "INSERT INTO 'mydb'.'medico' VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"

    def values(self) -> tuple:
        return self.nombre, self.apellido, self.run, self.titulo, self.institucion_egreso, self.fecha_titulacion, \
               self.telefono, self.direccion, self.especialidad

    def __str__(self):
        return "Datos médico:\nNombre: " + self.nombre + "\nApellido: " + self.apellido + \
               "\nRUN: " + str(self.run) + "\nTeléfono: " \
               + str(self.telefono) + "\nTitulo: " + self.titulo + "\nInstitución: " + \
               self.institucion_egreso + "\nFecha titulación: " + self.fecha_titulacion + "\nEspecialidad: " + \
               self.especialidad + "\nDirección: " + self.direccion
