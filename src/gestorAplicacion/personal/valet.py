from ..Servicios.auto import Auto
from ..personal.empleado import Empleado
from ..personal.recepcionista import Recepcionista
from ..Servicios.casino import Casino


class Valet(Empleado):
    def __init__(self, rol: str, puesto: str):
        super().__init__(rol, puesto)

    def generar_saludo(self, nombre: str, rol: str) -> str:
        return f"Hola, {nombre}, soy un {rol}"

    @staticmethod
    def identificar_cliente(identificacion: int):
        for cliente in Recepcionista.get_clientes():
            print(cliente.get_id())
            if cliente.get_id() == identificacion:
                return cliente
        return None

    def estacionar_registrar_auto(self, modelo: str, placa: str, columna: int, fila: int, identificacion: int):
        auto = Auto()
        cliente = self.identificar_cliente(identificacion)
        auto.set_cliente(cliente)

        estacionamiento = Casino.get_estacionamiento()

        if columna < 0 or fila < 0 or columna >= len(estacionamiento) or fila >= len(estacionamiento[0]):
            print("La posición indicada está fuera de los límites del estacionamiento.")
            return None

        if estacionamiento[fila][columna] is not None:
            print(
                "El espacio seleccionado ya está ocupado o es restringido. Por favor, elija otro.")
            return None

        auto.set_modelo(modelo)
        auto.set_placa(placa)
        estacionamiento[fila][columna] = auto
        auto.set_espacio_estacionamiento((fila, columna))

        if auto.get_cliente() is not None:
            if auto.get_cliente().get_suscripcion().get_tipo_suscripcion().lower() == "platinum" and fila > 2:
                self.compensar_fichas(
                    auto.get_cliente().get_suscripcion(), auto.get_cliente())
                print(
                    f"El cliente ha recibido {auto.get_cliente().get_suscripcion().get_ficha_compensacion()} fichas de compensación por escoger un espacio menor al de su suscripción.")

        return auto
