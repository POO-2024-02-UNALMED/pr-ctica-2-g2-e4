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
        self.numero = None 

    @staticmethod
    def seleccionar_asiento(cliente, evento_seleccionado):
        """
        Método para seleccionar el asiento del cliente según su suscripción.
        """
        tipo_suscripcion = cliente.get_suscripcion().get_tipo_suscripcion().lower()

        if tipo_suscripcion == "platinum":
            print("Como miembro Platinum, se le ha asignado automáticamente un asiento en Primera Fila.")
            print("Además, recibirá una bebida especial gratuita durante el espectáculo.")
            return Asiento.ZonaAsiento.PALCO

        print("\nAquí tienes los asientos disponibles:\n")
        evento_seleccionado.mostrar_zonas_asientos()

        print("Seleccione una zona de asiento: ")
        print("1. PALCO\n2. BALCÓN\n3. CENTRO\n4. ATRÁS")

        zonas = {
            1: Asiento.ZonaAsiento.PALCO,
            2: Asiento.ZonaAsiento.BALCON,
            3: Asiento.ZonaAsiento.CENTRO,
            4: Asiento.ZonaAsiento.ATRAS
        }

        while True:
            try:
                opcion = int(input("Ingrese el número de la zona deseada: "))
                if opcion in zonas:
                    return zonas[opcion]
                else:
                    print("Opción inválida. Intente nuevamente.")
            except ValueError:
                print("Por favor, ingrese un número válido.")


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
