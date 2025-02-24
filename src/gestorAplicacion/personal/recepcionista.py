from ..Servicios.asiento import Asiento
from ..Servicios.asiento import ZonaAsiento
from ..Servicios.auto import Auto
from ..Servicios.evento import Evento
from ..personal.empleado import Empleado
from ..Servicios.suscripcion import Suscripcion

from typing import List


class Recepcionista(Empleado):
    clientes = []

    def __init__(self, rol: str, puesto: str):
        super().__init__(rol, puesto)

    def registrar_cliente(self, edad: int, saldo: float, identificacion: int, nombre: str, auto: Auto):
        from gestorAplicacion.personal.cliente import Cliente
        numero_visitas = 1

        for cliente in Recepcionista.clientes:
            if cliente.get_id() == identificacion:
                cliente.set_numero_visitas(cliente.get_numero_visitas() + 1)
                cliente.set_auto(auto)
                cliente.set_saldo(saldo)
                cliente.set_suscripcion(
                    Suscripcion(cliente.get_numero_visitas()))
                return cliente

        if edad < 18:
            print("No es mayor de edad, no puede entrar al casino")
            return None

        cliente_nuevo = Cliente(
            nombre, edad, identificacion, saldo, auto, Suscripcion(numero_visitas))
        Recepcionista.clientes.append(cliente_nuevo)
        return cliente_nuevo

    def generar_saludo(self, nombre: str, rol: str) -> str:
        return f"Hola, {nombre}, soy un {rol}."

    def cambiar_fichas(self, cliente, dinero: float):
        fichas = int(dinero) // 1000
        cambio = dinero % 1000
        cliente.set_saldo(cliente.get_saldo() - dinero + cambio)
        cliente.set_fichas(cliente.get_fichas() + fichas)

    @staticmethod
    def get_clientes():
        return Recepcionista.clientes

    @staticmethod
    def identificar_cliente(identificacion: int):
        for cliente in Recepcionista.get_clientes():
            if cliente.get_id() == identificacion:
                return cliente
        return None

    @staticmethod
    def procesar_seleccion_evento(cliente, evento_seleccionado: Evento, ubicacion: ZonaAsiento, costo_con_descuento: int):
        print("\n--Resumen de la reserva--\n")
        print(f"Ha seleccionado el evento: {evento_seleccionado.get_nombre()}")
        print(
            f"Artista invitado: {evento_seleccionado.get_artista().get_nombre()}")
        print(f"En la ubicación: {ubicacion}")
        print(f"El precio del evento fue de {costo_con_descuento} fichas.")
        print("Gracias por visitar el área de eventos. ¡Disfrute del espectáculo!")

        if cliente.get_suscripcion().get_tipo_suscripcion().lower() == "platinum":
            print(
                "Como miembro Platinum, también recibirá una bebida especial durante el espectáculo.")
