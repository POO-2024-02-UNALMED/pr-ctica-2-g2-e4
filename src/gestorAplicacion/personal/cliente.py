from ..Servicios import Auto, Cuenta, Suscripcion
from .recepcionista import Recepcionista
from typing import List


class Cliente:
    def __init__(self, nombre_cliente: str, edad_cliente: int, id: int, saldo: float,
                 auto: Auto = None, suscripcion: Suscripcion = None):
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
        self.cuentas: List[Cuenta] = []
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

    def agregar_reserva(self, habitacion, noches):
        total = habitacion.precio_base * noches * \
            (1 - self.suscripcion.descuento)
        detalle = f'Habitación {habitacion.numero} por {noches} noche(s). Total (con descuento): ${total}'
        self.historial_reservas.append(detalle)
        self.cuenta_total += total

    def mostrar_historial_reservas(self):
        print("\n--- Historial de Reservas ---")
        if not self.historial_reservas:
            print("No hay reservas registradas.")
        else:
            for reserva in self.historial_reservas:
                print(reserva)

    def pagar_cuenta(self):
        if self.cuenta_total > 0:
            print(f"El total a pagar es: ${self.cuenta_total}")
            self.cuenta_total = 0
        else:
            print("No hay saldo pendiente por pagar.")

    def __str__(self):
        return f"Cliente: {self.nombre_cliente} (ID: {self.id}, Suscripción: {self.suscripcion})"

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

    def get_suscripcion(self) -> Suscripcion:
        return self.suscripcion

    def set_suscripcion(self, suscripcion: Suscripcion):
        self.suscripcion = suscripcion
