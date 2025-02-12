from ..Servicios.cuenta import Cuenta


class Cliente:
    def __init__(self, nombre, identificacion, suscripcion):
        self.nombre = nombre
        self.identificacion = identificacion
        self.suscripcion = suscripcion
        self.cuenta_total = 0
        self.historial_reservas = []

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
        return f"Cliente: {self.nombre} (ID: {self.identificacion}, Suscripción: {self.suscripcion})"
