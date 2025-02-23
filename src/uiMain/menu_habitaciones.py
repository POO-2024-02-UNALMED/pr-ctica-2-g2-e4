from ..gestorAplicacion.Servicios.habitacion import Habitacion


class MenuHabitaciones:
    def __init__(self, cliente):
        # Inicialización de la matriz: Tipos de habitación (3 tipos) × Niveles de suscripción (3 niveles)
        self.menu = [[None for _ in range(3)] for _ in range(3)]
        self.crear_habitaciones()

    def crear_habitaciones(self):
        # Crear habitaciones de ejemplo
        self.menu[0][0] = Habitacion(
            101, 100, "Estándar", "al mar", "Pequeña", True, False, 0.1, False)
        self.menu[1][0] = Habitacion(
            102, 200, "Suite", "a la ciudad", "Grande", True, False, 0.2, False)
        self.menu[2][0] = Habitacion(
            103, 500, "Presidencial", "al mar", "Grande", True, False, 0.3, False)

    def mostrar_menu(self, cliente):
        tipos = ["Estándar", "Suite", "Presidencial"]
        print("\n--- Menú de Habitaciones ---")
        for i in range(len(self.menu)):
            print(f"\nTipo: {tipos[i]}")
            for j in range(len(self.menu[i])):
                if self.menu[i][j] is not None:
                    habitacion = self.menu[i][j]
                    precio_con_descuento = habitacion.calcular_precio_con_descuento()
                    print(
                        f"{cliente.suscripcion.nivel}: {habitacion}, Precio (con descuento): ${precio_con_descuento}")

    def reservar_habitacion(self, cliente, suscripciones):
        tipo = int(input(
            "Seleccione el tipo de habitación (0 = Estándar, 1 = Suite, 2 = Presidencial): "))
        habitacion_reservada = self.buscar_disponible(tipo, 0)
        if habitacion_reservada:
            habitacion_reservada.ocupada = True
            noches = int(input("Ingrese el número de noches a reservar: "))
            cliente.agregar_reserva(habitacion_reservada, noches)
            print("Reserva realizada exitosamente:")
            print(habitacion_reservada)
        else:
            print("No hay habitaciones disponibles para esta categoría.")

    def buscar_disponible(self, tipo_indice, suscripcion_indice):
        if tipo_indice >= 0 and tipo_indice < len(self.menu):
            habitacion = self.menu[tipo_indice][suscripcion_indice]
            if habitacion is not None and not habitacion.ocupada:
                return habitacion
        return None  # No disponible
