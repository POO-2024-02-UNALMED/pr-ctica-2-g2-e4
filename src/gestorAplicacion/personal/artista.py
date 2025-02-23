from .empleado import Empleado


class Artista(Empleado):
    
    def __init__(self, nombre: str):
        super().__init__("Artista", "Escenario")  # Default values for rol & puesto
        self.nombre = nombre
        self.tipo_espectaculo = "General"  # Default value for tipo_espectaculo
    
    def generar_saludo(self, nombre: str, rol: str) -> str:
        return f"Hola, {nombre}, soy un {rol}."
    
    def get_tipo_espectaculo(self) -> str:
        return self.tipo_espectaculo
    
    def set_tipo_espectaculo(self, tipo_espectaculo: str):
        self.tipo_espectaculo = tipo_espectaculo
    
    def get_nombre(self) -> str:
        return self.nombre
