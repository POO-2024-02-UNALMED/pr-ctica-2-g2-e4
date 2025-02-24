
from .bebida import Bebida

class Cuenta:
    def __init__(self):
        self.pagada = False
        self.descripciones = []  # Lista de descripciones de los gastos
        self.precios = []  # Lista de precios de los gastos

    def registrar_gasto(self, descripcion: str, precio: float):
        self.descripciones.append(descripcion)
        self.precios.append(precio)

    def generar_factura_bar(self, bebida: Bebida, cliente, monto_propina: float, bartender) -> str:
        from gestorAplicacion.personal.bartender import Bartender
        from gestorAplicacion.personal.cliente import Cliente
        factura = "----- Factura Detallada -----\n"
        total = bebida.get_precio()

        # Obtener descuentos
        descuento_por_fidelidad = cliente.obtener_descuento_por_fidelidad_bar() * 100  # 5% si tiene fidelidad en el bar
        descuento_por_suscripcion = cliente.get_suscripcion().get_descuento() * 100

        # Calcular el total con descuentos
        descuento_total = descuento_por_fidelidad + descuento_por_suscripcion
        total_con_descuento = total * (1 - (descuento_total / 100))

        # Agregar los detalles de la factura
        factura += f"{bebida.get_nombre()}: ${total:.2f}\n"

        if descuento_por_fidelidad > 0:
            factura += f"Descuento por Fidelidad: -${total * (descuento_por_fidelidad / 100):.2f}\n"
        
        if descuento_por_suscripcion > 0:
            factura += f"Descuento por Suscripción: -${total * (descuento_por_suscripcion / 100):.2f}\n"
        
        factura += "-----------------------------\n"
        factura += f"Total a Pagar: ${total_con_descuento:.2f}\n"
        factura += "-----------------------------"

        self.registrar_gasto(bebida.get_nombre(), total_con_descuento)
        cliente.get_cuentas().append(self)
        cliente.set_bebida_favorita(bartender.evaluar_bebida_favorita(cliente.get_cuentas()))
        
        return factura
    
    def reiniciar_cuenta(self):
        self.descripciones.clear()
        self.precios.clear()

    def is_pagada(self) -> bool:
        return self.pagada
    
    def set_pagada(self, pagada: bool):
        self.pagada = pagada
    
    def get_descripciones(self):
        return self.descripciones
    
    def set_descripciones(self, descripciones):
        self.descripciones = descripciones
    
    def get_precios(self):
        return self.precios
    
    def set_precios(self, precios):
        self.precios = precios
