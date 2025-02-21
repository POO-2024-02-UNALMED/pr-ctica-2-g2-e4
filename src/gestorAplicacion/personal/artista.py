from gestorAplicacion.personal.empleado import Empleado

class Artista(Empleado):
    def __init__(self, nombre: str, tipo_espectaculo: str = "General", rol: str = "Artista", puesto: str = "Escenario"):
        super().__init__(rol, puesto)
        self.nombre = nombre
        self.tipo_espectaculo = tipo_espectaculo

    def generar_saludo(self, nombre: str, rol: str) -> str:
        return f"Hola, {nombre}, soy un {rol}."

    def get_tipo_espectaculo(self) -> str:
        return self.tipo_espectaculo

    def set_tipo_espectaculo(self, tipo_espectaculo: str):
        self.tipo_espectaculo = tipo_espectaculo

    def get_nombre(self) -> str:
        return self.nombre