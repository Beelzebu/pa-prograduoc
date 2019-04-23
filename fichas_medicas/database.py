# -*- coding: utf-8 -*-
import sqlite3


class Database:
    def __init__(self):
        self.connection = None

    def connect(self):
        """Function to create connection to database and create default tables"""
        pass

    def save(self, ficha):
        """Function to save `fichas` on the database"""
        pass

    def find_one(self, ficha_id: int):
        """Fetch the document that matches with the provided id or None if not found"""
        pass

    def find_all(self) -> []:
        """Fetch all documents from the database and return them as a list"""
        pass


class Serializable:

    def query(self) -> str:
        """Query to insert this object to the database"""
        pass

    def values(self) -> str:
        """Values from this object to replace in the query"""
        pass

    def save(self) -> None:  # TODO: get database instance and execute query
        pass


class SQLiteDatabase(Database):

    def __init__(self):
        super().__init__()

    def connect(self):
        self.connection = sqlite3.connect('local.db').cursor()
        self.connection.execute('''CREATE TABLE IF NOT EXISTS `mydb`.`ficha` (
        `id` INT NOT NULL,
        `fecha` DATE NOT NULL,
        `hora` TIME NOT NULL,
        PRIMARY KEY (`id`),
        UNIQUE INDEX `id_UNIQUE` (`id` ASC))
        ENGINE = InnoDB''')
        self.connection.execute('''CREATE TABLE IF NOT EXISTS `mydb`.`paciente` (
        `run` INT NOT NULL,
        `nombre` VARCHAR(45) NOT NULL,
        `telefono` INT NOT NULL,
        `direccion` VARCHAR(100) NOT NULL,
        `ficha_id` INT NOT NULL,
        PRIMARY KEY (`run`, `ficha_id`),
        INDEX `fk_paciente_ficha_idx` (`ficha_id` ASC),
        CONSTRAINT `fk_paciente_ficha`
        FOREIGN KEY (`ficha_id`)
        REFERENCES `mydb`.`ficha` (`id`)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION)
        ENGINE = InnoDB''')

    def save(self, entity: Serializable):
        if not isinstance(entity, Serializable):
            raise ValueError("object is not an instance of Serializable")
        self.connection.execute(entity.query(), entity.values())
