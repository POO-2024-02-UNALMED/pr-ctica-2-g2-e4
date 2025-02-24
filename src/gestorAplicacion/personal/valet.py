from ..Servicios.auto import Auto
from ..personal.empleado import Empleado
from ..personal.recepcionista import Recepcionista
from ..Servicios.casino import Casino


class Valet(Empleado):
    def __init__(self, rol: str, puesto: str):
        super().__init__(rol, puesto)

    def generar_saludo(self, nombre: str, rol: str) -> str:
        return f"Hola, {nombre}, soy un {rol}"

    @staticmethod
    def identificar_cliente(identificacion: int):
        for cliente in Recepcionista.get_clientes():
            print(cliente.get_id())
            if cliente.get_id() == identificacion:
                return cliente
        return None


    def estacionar_registrar_auto(self, modelo: str, placa: str, columna: int, fila: int, identificacion: int):
        """ Handles parking logic, ensuring restricted areas for non-Platinum users """

        auto = Auto()
        cliente = self.identificar_cliente(identificacion)
        auto.set_cliente(cliente)

        estacionamiento = Casino.get_estacionamiento()

        # 🔹 Step 1: Validate if the selected parking spot is within allowed range
        if cliente:
            suscripcion_cliente = cliente.get_suscripcion()
            tipo_suscripcion = suscripcion_cliente.get_tipo_suscripcion().lower() if suscripcion_cliente else "no existe"

            if tipo_suscripcion != "platinum" and fila < 2:
                print("Solo clientes con suscripción Platinum pueden estacionar en las primeras dos filas.")
                return None  # ❌ Reject invalid parking request

        # 🔹 Step 2: Check if the selected space is within the parking lot limits
        if columna < 0 or fila < 0 or columna >= len(estacionamiento) or fila >= len(estacionamiento[0]):
            print("La posición indicada está fuera de los límites del estacionamiento.")
            return None

        # 🔹 Step 3: Check if the selected space is already occupied
        if estacionamiento[fila][columna] is not None:
            print("El espacio seleccionado ya está ocupado. Por favor, elija otro.")
            return None

        # 🔹 Step 4: Assign the car to the parking space
        auto.set_modelo(modelo)
        auto.set_placa(placa)
        estacionamiento[fila][columna] = auto
        auto.set_espacio_estacionamiento((fila, columna))

        # 🔹 Step 5: If a Platinum user parked outside their zone, compensate with extra tokens
        if auto.get_cliente() is not None:
            if auto.get_cliente().get_suscripcion().get_tipo_suscripcion().lower() == "platinum" and fila > 2:
                self.compensar_fichas(
                    auto.get_cliente().get_suscripcion(), auto.get_cliente()
                )
                print(
                    f"El cliente ha recibido {auto.get_cliente().get_suscripcion().get_ficha_compensacion()} fichas de compensación por escoger un espacio menor al de su suscripción."
                )

        return auto
