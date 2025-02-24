from .auto import Auto
from .suscripcion import Suscripcion
from .habitacion import Habitacion
from .evento import Evento

class Casino:
    estacionamiento = [[]]

    def __init__(self):
        self.hotel = []
        self.teatro = []

    @staticmethod
    def mostrar_espacios_estacionamiento(suscripcion):
        if Casino.estacionamiento is None or not Casino.estacionamiento:
            return "El estacionamiento está vacío o no ha sido inicializado."

        tabla = "    " + "   ".join(str(col) for col in range(len(Casino.estacionamiento[0]))) + "\n"
        tipo_sub = suscripcion.get_tipo_suscripcion() if suscripcion else "no existe"
        
        for fila, row in enumerate(Casino.estacionamiento):
            tabla += f"{fila} | "
            for columna, espacio in enumerate(row):
                if tipo_sub.lower() != "platinum" and fila < 2:
                    tabla += "X   "  # Espacio restringido
                else:
                    tabla += "X   " if espacio else "O   "
            tabla += "\n"
        
        return tabla

    @staticmethod
    def get_estacionamiento():
        return Casino.estacionamiento

    @staticmethod
    def set_estacionamiento(estacionamiento):
        Casino.estacionamiento = estacionamiento

    def get_hotel(self):
        return self.hotel

    def set_hotel(self, hotel):
        self.hotel = hotel

    def get_teatro(self):
        return self.teatro

    def set_teatro(self, teatro):
        self.teatro = teatro

    @staticmethod
    def inicializar_estacionamiento(filas, columnas):
        Casino.estacionamiento = [[None for _ in range(columnas)] for _ in range(filas)]

        autos_ejemplo = [
            (0, 0, Auto("Toyota", "ABC123")),
            (1, 1, Auto("Honda", "DEF456")),
            (2, 2, Auto("Ford", "GHI789"))
        ]

        for fila, columna, auto in autos_ejemplo:
            Casino.estacionamiento[fila][columna] = auto
        
        print("Estacionamiento inicializado con éxito.")
