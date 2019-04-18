from database.database import Serializable


class Persona(Serializable):
    def __init__(self, nombre, run, telefono, direccion):
        self.nombre = nombre
        self.run = run
        self.telefono = telefono
        self.direccion = direccion


class Paciente(Persona):

    def __init__(self, nombre, run):
        super().__init__(nombre, run)

    def query(self):
        return "INSERT INTO 'mydb'.'paciente' VALUES (?, ?, ?, ?)"

    def values(self):
        return self.run, self.nombre, self.telefono, self.direccion
