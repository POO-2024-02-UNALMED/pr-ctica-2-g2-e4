class Suscripcion:
    def __init__(self, visitas: int = None, vetado: str = None):
        if visitas is not None:
            if visitas == 1:
                self.tipo_suscripcion = "primera vez"
                self.descuento = 0.05
                self.ficha_compensacion = 20
                self.calidad_ingredientes = "media"
            elif 1 < visitas < 4:
                self.tipo_suscripcion = "por defecto"
                self.descuento = 0.0
                self.ficha_compensacion = 10
                self.calidad_ingredientes = "baja"
            elif 3 < visitas < 6:
                self.tipo_suscripcion = "Silver"
                self.descuento = 0.15
                self.ficha_compensacion = 50
                self.calidad_ingredientes = "alta"
            elif visitas > 5:
                self.tipo_suscripcion = "Platinum"
                self.descuento = 0.25
                self.ficha_compensacion = 100
                self.calidad_ingredientes = "excelente"
        elif vetado is not None:
            self.tipo_suscripcion = "vetado"
            # Add logic to handle banning from casino

    def get_tipo_suscripcion(self) -> str:
        return self.tipo_suscripcion

    def set_tipo_suscripcion(self, tipo_suscripcion: str):
        self.tipo_suscripcion = tipo_suscripcion

    def get_descuento(self) -> float:
        return self.descuento

    def set_descuento(self, descuento: float):
        self.descuento = descuento

    def get_ficha_compensacion(self) -> int:
        return self.ficha_compensacion

    def set_ficha_compensacion(self, ficha_compensacion: int):
        self.ficha_compensacion = ficha_compensacion

    def get_calidad_ingredientes(self) -> str:
        return self.calidad_ingredientes

    def set_calidad_ingredientes(self, calidad_ingredientes: str):
        self.calidad_ingredientes = calidad_ingredientes

    def is_premio_especial(self) -> bool:
        return getattr(self, 'premio_especial', False)

    def set_premio_especial(self, premio_especial: bool):
        self.premio_especial = premio_especial
