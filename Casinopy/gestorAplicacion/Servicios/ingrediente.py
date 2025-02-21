# Ensure the correct import path
from ..Servicios.suscripcion import suscripcion

class Ingrediente:
    def __init__(self, nombre: str, suscripcion: Suscripcion = None):
        self.nombre = nombre
        self.calidad = suscripcion.get_calidad_ingredientes() if suscripcion else "alta"

    def get_nombre(self) -> str:
        return self.nombre

    def set_nombre(self, nombre: str):
        self.nombre = nombre

    def get_calidad(self) -> str:
        return self.calidad

    def set_calidad(self, calidad: str):
        self.calidad = calidad
