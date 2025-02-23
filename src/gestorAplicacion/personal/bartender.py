from ..Servicios import Bebida
from ..Servicios import Cuenta
from ..Servicios import Ingrediente
from ..Servicios import Suscripcion
from ..personal.empleado import Empleado
from typing import List


class Bartender(Empleado):
    barra_de_bebidas: List[Bebida] = []
    barra_de_ingredientes: List[Ingrediente] = []

    def __init__(self, rol: str, puesto: str, barra_de_bebidas: List[Bebida] = None, barra_de_ingredientes: List[Ingrediente] = None):
        super().__init__(rol, puesto)
        if barra_de_bebidas is not None:
            Bartender.barra_de_bebidas = barra_de_bebidas
        if barra_de_ingredientes is not None:
            Bartender.barra_de_ingredientes = barra_de_ingredientes
        self.menu_actual = []

    def generar_saludo(self, nombre: str, rol: str) -> str:
        return f"Hola, {nombre}, soy un {rol}"

    def preparar_bebida_bienvenida(self, cliente):
        bebida_base = self.evaluar_bebida_favorita(cliente.get_cuentas())
        if not bebida_base:
            bebida_base = max(Bartender.barra_de_bebidas,
                              key=lambda b: b.get_favorito(), default=None)

        ingredientes_preparados = [Ingrediente(i.get_nombre(), cliente.get_suscripcion())
                                   for i in bebida_base.get_ingredientes()
                                   if any(i.get_nombre().lower() == bi.get_nombre().lower() for bi in Bartender.barra_de_ingredientes)]

        return Bebida(
            bebida_base.get_nombre(), bebida_base.get_precio(), bebida_base.is_dulce(),
            bebida_base.is_amargo(), bebida_base.is_acido(), bebida_base.is_alcoholico(),
            bebida_base.get_favorito(), ingredientes_preparados
        )

    def preparar_bebida(self, nombre_bebida: str, suscripcion: Suscripcion):
        bebida_base = next((b for b in Bartender.barra_de_bebidas if b.get_nombre(
        ).lower() == nombre_bebida.lower()), None)
        if not bebida_base:
            raise ValueError(
                "La bebida solicitada no está disponible en la barra.")

        ingredientes_preparados = []
        for ingrediente in bebida_base.get_ingredientes():
            encontrado = next((i for i in Bartender.barra_de_ingredientes if i.get_nombre(
            ).lower() == ingrediente.get_nombre().lower()), None)
            if encontrado:
                ingredientes_preparados.append(Ingrediente(
                    encontrado.get_nombre(), suscripcion))
            else:
                raise ValueError(
                    f"No se encontraron todos los ingredientes necesarios para la bebida: {ingrediente.get_nombre()}")

        return Bebida(
            bebida_base.get_nombre(), bebida_base.get_precio(), bebida_base.is_dulce(),
            bebida_base.is_amargo(), bebida_base.is_acido(), bebida_base.is_alcoholico(),
            bebida_base.get_favorito(), ingredientes_preparados
        )

    def generar_menu(self, alcoholico: bool, dulce: bool, amargo: bool, acido: bool, bebida_favorita: Bebida, suscripcion: Suscripcion) -> str:
        self.menu_actual = []
        menu = [
            f"Menú personalizado (Descuento por suscripción: {suscripcion.get_descuento() * 100}%):"]

        for bebida in Bartender.barra_de_bebidas:
            if ((not dulce or bebida.is_dulce()) and (not amargo or bebida.is_amargo()) and
                    (not acido or bebida.is_acido()) and (not alcoholico or bebida.is_alcoholico())):
                precio_descuento = int(
                    bebida.get_precio() * (1 - suscripcion.get_descuento()))
                menu.append(f"{len(self.menu_actual) + 1}. {bebida.get_nombre()}: Precio original: ${bebida.get_precio()} | Precio con descuento: ${precio_descuento} ({self.calcular_recomendacion(bebida, bebida_favorita)})")
                self.menu_actual.append(bebida)

        if not self.menu_actual:
            menu.append(
                "No hay opciones disponibles con los filtros seleccionados.")

        return "\n".join(menu)

    def calcular_recomendacion(self, bebida: Bebida, bebida_favorita: Bebida) -> str:
        if bebida_favorita and bebida.get_nombre().lower() == bebida_favorita.get_nombre().lower():
            return "bebida favorita"
        elif bebida.get_favorito() > 3:
            return "recomendada"
        elif bebida.get_favorito() >= 0:
            return "Neutral"
        return "no recomendada"

    def evaluar_bebida_favorita(self, cuentas: List[Cuenta]) -> Bebida:
        descripciones = [
            d for cuenta in cuentas for d in cuenta.get_descripciones()]
        bebida_favorita_nombre = max(
            set(descripciones), key=descripciones.count, default=None)
        return self.buscar_bebida_en_barra(bebida_favorita_nombre)

    def buscar_bebida_en_barra(self, nombre_bebida: str) -> Bebida:
        return next((b for b in Bartender.barra_de_bebidas if b.get_nombre().lower() == nombre_bebida.lower()), None)

    @staticmethod
    def get_barra_de_bebidas():
        return Bartender.barra_de_bebidas

    @staticmethod
    def set_barra_de_bebidas(barra_de_bebidas: List[Bebida]):
        Bartender.barra_de_bebidas = barra_de_bebidas

    @staticmethod
    def get_barra_de_ingredientes():
        return Bartender.barra_de_ingredientes

    @staticmethod
    def set_barra_de_ingredientes(barra_de_ingredientes: List[Ingrediente]):
        Bartender.barra_de_ingredientes = barra_de_ingredientes

    def get_menu_actual(self):
        return self.menu_actual

    def set_menu_actual(self, menu_actual: List[Bebida]):
        self.menu_actual = menu_actual
