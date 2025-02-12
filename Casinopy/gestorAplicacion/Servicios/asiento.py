from enum import Enum

class ZonaAsiento(Enum):
    PALCO = "Palco"
    BALCON = "Balcón"
    CENTRO = "Centro"
    ATRAS = "Atrás"

class Asiento:
    def __init__(self, zona, cantidad, precio):
        self.zona = zona
        self.cantidad = cantidad
        self.precio = precio
        self.reservado = False  # Inicialmente no está reservado
        self.numero = None  # Número del asiento (opcional)

    # Métodos para reservar y liberar asientos
    def reservar_asiento(self):
        """Reserva el asiento si está disponible."""
        if not self.reservado:
            self.reservado = True
            return True
        else:
            print("El asiento ya está reservado.")
            return False

    def liberar_asiento(self):
        """Libera el asiento si está reservado."""
        if self.reservado:
            self.reservado = False
            print("El asiento ha sido liberado.")
        else:
            print("El asiento ya se encontraba disponible.")

    def es_disponible(self):
        """Verifica si el asiento está disponible."""
        return not self.reservado

    # Getters y setters con propiedades
    @property
    def zona_asiento(self):
        return self.zona

    @zona_asiento.setter
    def zona_asiento(self, zona):
        self.zona = zona

    @property
    def cantidad_asientos(self):
        return self.cantidad

    @cantidad_asientos.setter
    def cantidad_asientos(self, cantidad):
        self.cantidad = cantidad

    @property
    def precio_asiento(self):
        return self.precio

    @precio_asiento.setter
    def precio_asiento(self, precio):
        self.precio = precio

    @property
    def numero_asiento(self):
        return self.numero

    @numero_asiento.setter
    def numero_asiento(self, numero):
        self.numero = numero

    def __str__(self):
        """Representación en string del objeto Asiento."""
        return f"Asiento(zona={self.zona.value}, cantidad={self.cantidad}, reservado={self.reservado}, precio={self.precio})"
