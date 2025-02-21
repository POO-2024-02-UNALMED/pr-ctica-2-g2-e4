# Ensure the correct import path
from .suscripcion import Suscripcion


class Ingrediente():
    def __init__(self, nombre: str, suscrip: Suscripcion = None):
        self.nombre = nombre
        self.calidad = suscrip.get_calidad_ingredientes() if suscrip else "alta"

    def get_nombre(self) -> str:
        return self.nombre

    def set_nombre(self, nombre: str):
        self.nombre = nombre

    def get_calidad(self) -> str:
        return self.calidad

    def set_calidad(self, calidad: str):
        self.calidad = calidad
