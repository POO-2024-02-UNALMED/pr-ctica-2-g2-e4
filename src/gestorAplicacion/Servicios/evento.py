from ..Servicios.asiento import Asiento
from ..Servicios.asiento import ZonaAsiento

from ..personal.cliente import Cliente
from ..personal.artista import Artista


class Evento():
    eventos_disponibles = []  # Lista estática de eventos disponibles

    def __init__(self, nombre, descripcion, artista, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.artista = artista
        self.precio = precio
        self.consumo_minimo = False
        self.asientos = []

    def inicializar_asientos(self):
        """Inicializa los asientos en las distintas zonas."""
        self.asientos.append(Asiento(ZonaAsiento.PALCO, 25, 50))
        self.asientos.append(Asiento(ZonaAsiento.BALCON, 20, 40))
        self.asientos.append(Asiento(ZonaAsiento.CENTRO, 15, 25))
        self.asientos.append(Asiento(ZonaAsiento.ATRAS, 10, 20))

    @classmethod
    def inicializar_eventos(cls):
        """Inicializa eventos por defecto."""
        cls.eventos_disponibles.clear()

        artista1 = Artista("Lisa S.")
        artista2 = Artista("Merrit McKinney")
        artista3 = Artista("Franco Escamilla")

        cls.eventos_disponibles.append(Evento("Concierto de Jazz", "Jazz relajante.", artista1, 25))
        cls.eventos_disponibles.append(Evento("Show de Magia", "Acto de Ilusionismo.", artista2, 35))
        cls.eventos_disponibles.append(Evento("Comedia Stand-Up", "Una noche llena de risas.", artista3, 30))

    @classmethod
    def mostrar_eventos(cls):
        """Muestra los eventos disponibles."""
        if not cls.eventos_disponibles:
            print("No hay eventos disponibles en este momento")
            return
        
        for i, evento in enumerate(cls.eventos_disponibles, start=1):
            nombre_artista = evento.artista.nombre if evento.artista else "Artista no disponible"
            print(f"{i}. {evento.nombre} - {evento.descripcion} | Artista: {nombre_artista} (${evento.precio})")

    def mostrar_zonas_asientos(self):
        """Muestra las zonas de asientos disponibles en el evento."""
        print("-- Zonas de asientos disponibles para el evento --\n")
        for asiento in self.asientos:
            print(f"{asiento.zona}: {asiento.cantidad} asientos disponibles")

    @classmethod
    def get_evento_por_indice(cls, indice):
        """Devuelve un evento según el índice dado."""
        if 0 < indice <= len(cls.eventos_disponibles):
            return cls.eventos_disponibles[indice - 1]
        else:
            print("Opción inválida. Seleccionando el primer evento por defecto.")
            return cls.eventos_disponibles[0]

    @staticmethod
    def calcular_precio_con_descuento(cliente, evento):
        """Calcula el precio con descuento según la suscripción del cliente."""
        descuento = cliente.suscripcion.descuento
        precio_original = evento.precio
        precio_con_descuento = precio_original - (precio_original * descuento)
        print(f"\nPrecio original: {precio_original:.2f}")
        print(f"Descuento aplicado: {descuento * 100:.2f}%")
        print(f"Precio final: {precio_con_descuento:.2f}")
        return precio_con_descuento

    @staticmethod
    def verificar_consumo_obligatorio(cliente):
        """Verifica si el cliente debe hacer un consumo mínimo antes del evento."""
        if cliente.suscripcion.tipo_suscripcion.lower() == "primera vez":
            print("\nComo cliente 'Primera vez', deberá realizar un consumo mínimo en el bar antes del evento.")

    def calcular_precio_zona(self, zona):
        """Calcula el precio del evento dependiendo de la zona del asiento."""
        precios_zonas = {
            ZonaAsiento.PALCO: 200.0,
            ZonaAsiento.BALCON: 150.0,
            ZonaAsiento.CENTRO: 100.0,
            ZonaAsiento.ATRAS: 50.0
        }
        precio = precios_zonas.get(zona, 0.0)
        print(f"El precio para la zona {zona} es: {precio}")
        return precio

    def calcular_descuento(self, suscripcion):
        """Aplica descuento según la suscripción del cliente."""
        return self.precio * (1 - suscripcion.descuento)

    def verificar_consumo_minimo(self, monto):
        """Verifica si el evento requiere un consumo mínimo."""
        return not self.consumo_minimo or monto >= 0.0

    # Getters y setters
    @property
    def nombre_evento(self):
        return self.nombre

    @nombre_evento.setter
    def nombre_evento(self, nombre):
        self.nombre = nombre

    @property
    def precio_evento(self):
        return self.precio

    @property
    def descripcion_evento(self):
        return self.descripcion

    @property
    def asientos_evento(self):
        return self.asientos

    @property
    def artista_evento(self):
        return self.artista

    @artista_evento.setter
    def artista_evento(self, artista):
        self.artista = artista

    @property
    def consumo_minimo_evento(self):
        return self.consumo_minimo

    @consumo_minimo_evento.setter
    def consumo_minimo_evento(self, consumo_minimo):
        self.consumo_minimo = consumo_minimo

    @asientos_evento.setter
    def asientos_evento(self, asientos):
        self.asientos = asientos
