class Suscripcion:
    def __init__(self, nivel, descuento):
        self.nivel = nivel
        self.descuento = descuento

    def __str__(self):
        return f"{self.nivel} ({self.descuento * 100}% de descuento)"