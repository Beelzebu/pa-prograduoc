from ..database.database import Serializable


class Humano(Serializable):
    def __init__(self, nombre, apellido, run):
        self.nombre = nombre
        self.apellido = apellido
        self.run = run

    def query(self):
        raise NotImplementedError

    def values(self):
        raise NotImplementedError


class Paciente(Humano):

    def __init__(self, nombre, apellido, run, telefono, direccion, estado_civil):
        super().__init__(nombre, apellido, run)
        self.telefono = telefono
        self.direccion = direccion
        self.estado_civil = estado_civil

    def query(self):
        return "INSERT INTO 'mydb'.'paciente' VALUES (?, ?, ?, ?, ?, ?)"

    def values(self):
        return self.run, self.nombre, self.apellido, self.telefono, self.direccion, self.estado_civil


class Personal(Humano):

    def __init__(self, nombre, apellido, run, titulo, institucion_egreso, fecha_titulacion, telefono, direccion):
        super().__init__(nombre, apellido, run)
        self.titulo = titulo
        self.institucion_egreso = institucion_egreso
        self.fecha_titulacion = fecha_titulacion
        self.telefono = telefono
        self.direccion = direccion

    def query(self):
        raise NotImplementedError

    def values(self):
        raise NotImplementedError


class Medico(Personal):

    def query(self):
        return "INSERT INTO 'mydb'.'medico' VALUES ()"

    def values(self):
        return self.nombre, self.apellido, self.run

    def __init__(self, nombre, apellido, run, titulo, institucion_egreso, fecha_titulacion, telefono, direccion,
                 especialidad):
        super().__init__(nombre, apellido, run, titulo, institucion_egreso, fecha_titulacion, telefono, direccion)
        self.especialidad = especialidad
