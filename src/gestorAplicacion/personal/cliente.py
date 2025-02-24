from typing import List
from ..Servicios.cuenta import Cuenta
from ..Servicios.suscripcion import Suscripcion
from ..Servicios.auto import Auto
from ..Servicios.bebida import Bebida
from ..Servicios.RegistroJuego import RegistroJuego
from ..Servicios.asiento import Asiento
from ..Servicios.evento import Evento
from .recepcionista import Recepcionista


class Cliente:
    def __init__(self, nombre_cliente: str, edad_cliente: int = None, id: int = None, saldo: float = 0.0, auto: Auto = None, suscripcion: Suscripcion = None):
        self.nombre_cliente = nombre_cliente
        self.edad_cliente = edad_cliente
        self.id = id
        self.saldo = saldo
        self.auto = auto
        self.fichas = 0
        self.numero_visitas = 0
        self.suscripcion = suscripcion if suscripcion else Suscripcion(
            self.numero_visitas)
        self.fidelidad_bar = False
        self.propinas_bar = 0
        self.bebida_favorita = None
        self.fidelidad_artista = False
        self.propinas_artista = 0
        self.cuentas = []
        self.registro_juego = None
        self.asiento = None
        self.evento = None
        Recepcionista.get_clientes().append(self)

    def dar_propina_bar(self, propina: int):
        self.saldo -= propina
        self.propinas_bar += 1
        if self.propinas_bar >= 3:
            self.fidelidad_bar = True

    def obtener_descuento_por_fidelidad_bar(self) -> float:
        return 0.05 if self.fidelidad_bar else 0.0

    def pagar_cuenta(self, cuenta: Cuenta):
        if not cuenta.is_pagada():
            total_cuenta = sum(cuenta.get_precios())
            if self.saldo >= total_cuenta:
                self.saldo -= total_cuenta
                cuenta.set_pagada(True)
                print(
                    f"Cuenta pagada por el cliente {self.nombre_cliente} por un total de ${total_cuenta}")
            else:
                print("Saldo insuficiente para pagar la cuenta.")

    def pagar_cuentas(self):
        for cuenta in self.cuentas:
            self.pagar_cuenta(cuenta)

    def get_nombre_cliente(self) -> str:
        return self.nombre_cliente

    def set_nombre_cliente(self, nombre_cliente: str):
        self.nombre_cliente = nombre_cliente

    def get_edad_cliente(self) -> int:
        return self.edad_cliente

    def set_edad_cliente(self, edad_cliente: int):
        self.edad_cliente = edad_cliente

    def get_id(self) -> int:
        return self.id

    def set_id(self, id: int):
        self.id = id

    def get_saldo(self) -> float:
        return self.saldo

    def set_saldo(self, saldo: float):
        self.saldo = saldo

    def get_auto(self) -> Auto:
        return self.auto

    def set_auto(self, auto: Auto):
        self.auto = auto

    def get_fichas(self) -> int:
        return self.fichas

    def set_fichas(self, fichas: int):
        self.fichas = fichas

    def get_numero_visitas(self) -> int:
        return self.numero_visitas

    def set_numero_visitas(self, numero_visitas: int):
        self.numero_visitas = numero_visitas

    def get_suscripcion(self) -> Suscripcion:
        return self.suscripcion

    def set_suscripcion(self, suscripcion: Suscripcion):
        self.suscripcion = suscripcion

    def is_fidelidad_bar(self) -> bool:
        return self.fidelidad_bar

    def set_fidelidad_bar(self, fidelidad_bar: bool):
        self.fidelidad_bar = fidelidad_bar

    def get_propinas_bar(self) -> int:
        return self.propinas_bar

    def set_propinas_bar(self, propinas_bar: int):
        self.propinas_bar = propinas_bar

    def get_bebida_favorita(self) -> Bebida:
        return self.bebida_favorita

    def set_bebida_favorita(self, bebida_favorita: Bebida):
        self.bebida_favorita = bebida_favorita

    def is_fidelidad_artista(self) -> bool:
        return self.fidelidad_artista

    def set_fidelidad_artista(self, fidelidad_artista: bool):
        self.fidelidad_artista = fidelidad_artista

    def get_propinas_artista(self) -> int:
        return self.propinas_artista

    def set_propinas_artista(self, propinas_artista: int):
        self.propinas_artista = propinas_artista

    def get_cuentas(self) -> list:
        return self.cuentas

    def set_cuentas(self, cuentas: list):
        self.cuentas = cuentas

    def get_registro_juego(self) -> RegistroJuego:
        return self.registro_juego

    def set_registro_juego(self, registro_juego: RegistroJuego):
        self.registro_juego = registro_juego

    def get_asiento(self) -> Asiento:
        return self.asiento

    def set_asiento(self, asiento: Asiento):
        self.asiento = asiento

    def get_evento(self) -> Evento:
        return self.evento

    def set_evento(self, evento: Evento):
        self.evento = evento

    """ def agregar_reserva(self, habitacion, noches):
        total = habitacion.precio_base * noches * \
            (1 - self.suscripcion.descuento)
        detalle = f'Habitación {habitacion.numero} por {noches} noche(s). Total (con descuento): ${total}'
        self.historial_reservas.append(detalle)
        self.cuenta_total += total """

    """ def mostrar_historial_reservas(self):
        print("\n--- Historial de Reservas ---")
        if not self.historial_reservas:
            print("No hay reservas registradas.")
        else:
            for reserva in self.historial_reservas:
                print(reserva) """

    """ def pagar_cuenta(self):
        if self.cuenta_total > 0:
            print(f"El total a pagar es: ${self.cuenta_total}")
            self.cuenta_total = 0
        else:
            print("No hay saldo pendiente por pagar.") """
