import pickle

class Habitacion():
    def __init__(self, numero, precio_base, tipo, vista, capacidad, servicio_habitacion, sucia, descuento, ocupada):
        self.numero = numero
        self.precio_base = precio_base
        self.tipo = tipo
        self.vista = vista
        self.capacidad = capacidad
        self.servicio_habitacion = servicio_habitacion
        self.sucia = sucia
        self.descuento = descuento
        self.ocupada = ocupada
        self.noches_ocupadas = 0

    def calcular_precio_con_descuento(self):
        return self.precio_base * (1 - self.descuento)

    def limpiar(self):
        self.sucia = False

    def verificar_estado_sucia(self):
        self.sucia = (self.noches_ocupadas % 2 == 0 and self.noches_ocupadas != 0)

    def incrementar_noches_ocupadas(self):
        self.noches_ocupadas += 1

    def __str__(self):
        return f"Habitacion{{numero={self.numero}, tipo='{self.tipo}', vista='{self.vista}', capacidad='{self.capacidad}', " \
               f"servicio_habitacion={self.servicio_habitacion}, sucia={self.sucia}, precio_base={self.precio_base}, " \
               f"descuento={self.descuento}, ocupada={self.ocupada}}}"