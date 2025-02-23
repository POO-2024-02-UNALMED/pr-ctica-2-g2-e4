import random
from ..Servicios.habitacion import Habitacion
from ..Servicios.bar import Bar


class MenuHabitaciones:
    def __init__(self, cliente, conserje, bartender):
        # 3 tipos de habitaciones, 3 habitaciones por tipo
        self.menu = [[None for _ in range(3)] for _ in range(3)]
        self.tipos = ["Estándar", "Suite", "Presidencial"]
        self.crear_habitaciones(cliente)
        self.cliente = cliente
        self.conserje = conserje
        self.bartender = bartender

    def crear_habitaciones(self, cliente):
        for i in range(len(self.menu)):
            for j in range(len(self.menu[i])):
                # Número de habitación entre 1 y 100
                numero = random.randint(1, 100)
                # Precio base por tipo de habitación
                precio_base = (i + 1) * 100
                tipo = self.tipos[i]

                # Generar características aleatorias
                vista = random.choice(["al mar", "a la ciudad"])
                # Ejemplo de capacidades
                capacidad = random.choice(["Pequeña", "Grande"])
                servicio_habitacion = random.choice(
                    [True, False])  # Servicio a la habitación
                sucia = False  # Estado de la habitación (limpia o sucia)
                suscripcion_cliente = cliente.suscripcion
                descuento = suscripcion_cliente.descuento
                ocupada = False  # Inicialmente, la habitación no está ocupada

                # Crear la habitación y agregarla a la matriz
                self.menu[i][j] = Habitacion(numero, precio_base, tipo, vista, capacidad,
                                             servicio_habitacion, sucia, descuento, ocupada)

    def mostrar_menu(self, cliente):
        print("\n--- Menú de Habitaciones ---")
        descuento = cliente.suscripcion.descuento  # Obtener el descuento del cliente
        for i in range(len(self.menu)):
            print(f"\nTipo: {self.tipos[i]}")
            for j in range(len(self.menu[i])):
                if self.menu[i][j] is not None:
                    habitacion = self.menu[i][j]
                    precio_con_descuento = habitacion.precio_base * \
                        (1 - descuento)  # Aplicar el descuento
                    print(
                        f"{cliente.suscripcion.nivel}: {habitacion}, Precio (con descuento): ${precio_con_descuento:.2f}")

    def manejar_estadia(self, habitacion, noches_reservadas):
        for i in range(1, noches_reservadas + 1):
            print(f"\n--- Día {i} de su estadía ---")

            # Incrementar el contador de noches ocupadas en la habitación
            habitacion.incrementar_noches_ocupadas()
            habitacion.verificar_estado_sucia()

            # Mostrar el menú de opciones
            print("1. Solicitar servicio a la habitación")
            print("2. Solicitar limpieza de la habitación")
            print("3. Solicitar Auto")
            print("4. Salir del menú")

            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                bar = Bar()
                bar.atender_cliente(self.cliente, self.bartender)
            elif opcion == 2:
                # Llamar al conserje para limpiar la habitación
                self.conserje.limpiar_habitacion(habitacion)
            elif opcion == 3:
                self.cliente.pagar_cuenta()
            elif opcion == 4:
                print("Saliendo del menú de opciones.")
                return  # Salir del método
            else:
                print("Opción no válida. Intente de nuevo.")

        print("Su estadía ha terminado.")
        self.cliente.pagar_cuenta()

    def reservar_habitacion(self, cliente, suscripciones):
        self.mostrar_menu(cliente)

        # Obtener el nivel de suscripción del cliente
        nivel_suscripcion_string = cliente.suscripcion.nivel
        tipo = int(input(
            "Seleccione el tipo de habitación (0 = Estándar, 1 = Suite, 2 = Presidencial): "))

        # Validar la selección
        if tipo < 0 or tipo >= len(self.menu):
            print("Tipo de habitación no válido. Intente de nuevo.")
            return

        # Mostrar habitaciones disponibles de ese tipo
        print("\n--- Habitaciones Disponibles ---")
        for j in range(len(self.menu[tipo])):
            if self.menu[tipo][j] is not None and not self.menu[tipo][j].ocupada:
                habitacion = self.menu[tipo][j]
                print(
                    f"Número de habitación: {habitacion.numero}, {habitacion}")

        # Preguntar por el número de habitación
        numero_habitacion = int(
            input("Ingrese el número de la habitación que desea reservar: "))

        # Buscar la habitación por número
        habitacion_reservada = None
        for j in range(len(self.menu[tipo])):
            if self.menu[tipo][j] is not None and self.menu[tipo][j].numero == numero_habitacion:
                habitacion_reservada = self.menu[tipo][j]
                break

        if habitacion_reservada is not None and not habitacion_reservada.ocupada:
            noches = int(input("Ingrese el número de noches a reservar: "))
            habitacion_reservada.ocupada = True
            cliente.agregar_reserva(habitacion_reservada, noches)
            print(
                f"Reserva realizada exitosamente para la habitación: {habitacion_reservada}")

            self.manejar_estadia(habitacion_reservada, noches)
        else:
            print(
                "No hay habitaciones disponibles para esta categoría o el número de habitación es incorrecto.")
