import random
from ..gestorAplicacion.habitaciones.menu_habitaciones import MenuHabitaciones
from ..gestorAplicacion.Servicios.habitacion import Habitacion
from ..gestorAplicacion.habitaciones.menu_habitaciones import MenuHabitaciones
from ..gestorAplicacion.Servicios.suscripcion import Suscripcion
from ..gestorAplicacion.personal.recepcionista import Recepcionista
from ..gestorAplicacion.personal.cliente import Cliente


def main():
    # Simulación de datos iniciales
    menu_habitaciones = MenuHabitaciones()

    # Creación de habitaciones de ejemplo
    random.seed()
    habitacion1 = Habitacion(101, 100, "Estándar", random.choice(["al mar", "a la ciudad"]),
                             random.choice(["Pequeña", "Grande"]),
                             random.choice([True, False]), random.choice([True, False]), 0, False)
    habitacion2 = Habitacion(102, 200, "Suite", random.choice(["al mar", "a la ciudad"]),
                             random.choice(["Pequeña", "Grande"]),
                             random.choice([True, False]), random.choice([True, False]), 0, False)
    habitacion3 = Habitacion(103, 500, "Presidencial", random.choice(["al mar", "a la ciudad"]),
                             random.choice(["Pequeña", "Grande"]),
                             random.choice([True, False]), random.choice([True, False]), 0, False)

    # Agregar habitaciones al menú
    menu_habitaciones.agregar_habitacion(habitacion1, 0, 0)  # Estándar
    menu_habitaciones.agregar_habitacion(habitacion2, 1, 0)  # Suite
    menu_habitaciones.agregar_habitacion(habitacion3, 2, 0)  # Presidencial

    # Recepcionista para iniciar sesión
    recepcionista = Recepcionista("Carlos", "admin123")

    # Inicio de sesión
    print("Bienvenido al sistema de gestión del hotel.")
    id_recepcionista = input(
        "Por favor, inicie sesión.\nIngrese su ID de recepcionista: ")

    if id_recepcionista != recepcionista.id:
        print("ID incorrecto. Acceso denegado.")
        return

    print(f"¡Bienvenido, {recepcionista.nombre}!")

    cliente = None  # Cliente inicializado como None

    # Menú principal
    while True:
        print("\nSeleccione una opción:")
        print("1. Crear cliente")
        print("2. Ver habitaciones")
        print("3. Reservar habitación")
        print("4. Ver historial del cliente")
        print("5. Pagar cuenta del cliente")
        print("6. Salir")

        opcion = int(input())

        if opcion == 1:  # Crear cliente
            nombre = input("Ingrese el nombre del cliente: ")
            identificacion = input("Ingrese la identificación del cliente: ")

            print("Seleccione el nivel de suscripción del cliente:")
            print("1. Estándar (10% descuento)")
            print("2. Premium (20% descuento)")
            print("3. Primera vez (5% descuento)")
            nivel_suscripcion = int(input())

            if nivel_suscripcion == 1:
                suscripcion = Suscripcion("Estándar", 0.1)
            elif nivel_suscripcion == 2:
                suscripcion = Suscripcion("Premium", 0.2)
            elif nivel_suscripcion == 3:
                suscripcion = Suscripcion("Primera vez", 0.05)
            else:
                print("Opción no válida. Se asignará la suscripción estándar.")
                suscripcion = Suscripcion("Estándar", 0.1)

            cliente = Cliente(nombre, identificacion, suscripcion)
            print(f"Cliente creado exitosamente: {cliente}")

        elif opcion == 2:  # Ver habitaciones
            print("\n--- Menú de Habitaciones ---")
            menu_habitaciones.mostrar_menu(cliente)

        elif opcion == 3:  # Reservar habitación
            if cliente is None:
                print("No hay un cliente registrado. Cree un cliente primero.")
                continue

            tipo = int(input(
                "Seleccione el tipo de habitación: 0 = Estándar, 1 = Suite, 2 = Presidencial: "))
            habitacion_reservada = menu_habitaciones.buscar_disponible(tipo, 0)
            if habitacion_reservada:
                habitacion_reservada.ocupada = True
                noches = int(input("Ingrese el número de noches a reservar: "))
                cliente.agregar_reserva(habitacion_reservada, noches)
                print("Reserva realizada exitosamente:")
                print(habitacion_reservada)
            else:
                print("No hay habitaciones disponibles para esta categoría.")

        elif opcion == 4:  # Ver historial del cliente
            if cliente is None:
                print("No hay un cliente registrado. Cree un cliente primero.")
                continue
            print("\n--- Historial del Cliente ---")
            cliente.mostrar_historial_reservas()

        elif opcion == 5:  # Pagar cuenta del cliente
            if cliente is None:
                print("No hay un cliente registrado. Cree un cliente primero.")
                continue
            print("\n--- Pagar Cuenta del Cliente ---")
            cliente.pagar_cuenta()

        elif opcion == 6:  # Salir
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
