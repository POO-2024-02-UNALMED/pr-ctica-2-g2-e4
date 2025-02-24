from ..Servicios.suscripcion import Suscripcion



class Empleado:
    empleados = []

    def __init__(self, rol: str, puesto: str):
        self.rol = rol
        self.puesto = puesto
        Empleado.empleados.append(self)

    def compensar_fichas(self, suscripcion: Suscripcion, cliente):
        from gestorAplicacion.personal.cliente import Cliente
        fichas_compensacion = suscripcion.get_ficha_compensacion()
        cliente.set_fichas(cliente.get_fichas() + fichas_compensacion)

    def generar_saludo(self, nombre: str, rol: str) -> str:
        return f"Hola, {nombre}, soy un {rol}."

    def get_rol(self) -> str:
        return self.rol

    def set_rol(self, rol: str):
        self.rol = rol

    def get_puesto(self) -> str:
        return self.puesto

    def set_puesto(self, puesto: str):
        self.puesto = puesto

    @staticmethod
    def get_empleados():
        return Empleado.empleados

    @staticmethod
    def set_empleados(empleados):
        Empleado.empleados = empleados
