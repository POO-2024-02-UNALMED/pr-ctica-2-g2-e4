class Empleado:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id

    def get_nombre(self):
        return self.nombre

    def get_id(self):
        return self.id

    def get_rol(self):
        raise NotImplementedError("Subclasses must implement this method")