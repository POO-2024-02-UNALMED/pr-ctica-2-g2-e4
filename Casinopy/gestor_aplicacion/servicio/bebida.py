class Bebida:
    def __init__(self, nombre, precio, recomendacion):
        self.nombre = nombre
        self.precio = precio
        self.recomendacion = recomendacion

    def __str__(self):
        return f"{self.nombre} - ${self.precio} ({self.recomendacion})"