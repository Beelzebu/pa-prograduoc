import sqlite3


class Database:
    def __init__(self):
        self.connection = None

    def connect(self):
        pass

    def save(self, ficha):
        pass

    def find_one(self, ficha_id):
        pass

    def find_all(self):
        pass


class Serializable:

    def query(self):
        pass

    def values(self):
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

    def save(self, object):
        if not isinstance(object, Serializable):
            raise ValueError("object is not an instance of Serializable")
        self.connection.execute(object.query(), object.values())
