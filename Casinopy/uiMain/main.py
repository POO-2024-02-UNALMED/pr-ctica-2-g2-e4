import random
from .inicio_sesion import InicioSesion
from gestorAplicacion.habitaciones.menu_habitaciones import MenuHabitaciones
from gestor_aplicacion.usuarios.suscripcion import Suscripcion
from gestor_aplicacion.usuarios.recepcionista import Recepcionista
from gestor_aplicacion.usuarios.cliente import Cliente
from gestor_aplicacion.usuarios.conserje import Conserje
from gestor_aplicacion.usuarios.bartender import Bartender


def main():
    # Datos iniciales
    NOMBRES = ["Juan", "Paulina", "Carlos", "Maria", "Luis", "Sofia"]
    IDENTIFICACIONES = ["2341", "5212", "3215", "4296", "5015", "8127"]
    SUSCRIPCIONES = [
        Suscripcion("Estándar", 0.1),
        Suscripcion("Premium", 0.2),
        Suscripcion("Primera vez", 0.05)
    ]

    # Crear un recepcionista
    recepcionista = Recepcionista("Ana", 1234)

    # Inicio de sesión
    inicio_sesion = InicioSesion(recepcionista)
    if not inicio_sesion.iniciar_sesion():
        return  # Salir si las credenciales son incorrectas

    # Crear un cliente aleatorio
    nombre = random.choice(NOMBRES)
    identificacion = random.choice(IDENTIFICACIONES)
    suscripcion = random.choice(SUSCRIPCIONES)

    cliente = Cliente(nombre, identificacion, suscripcion)
    conserje = Conserje(nombre="Alfredo", id=4231)
    bartender = Bartender(nombre="Luis", id=6432)

    print(cliente)

    # Inicializar el menú de habitaciones
    menu_habitaciones = MenuHabitaciones(cliente, conserje, bartender)

    # Mostrar el menú y permitir al cliente reservar una habitación
    menu_habitaciones.mostrar_menu(cliente)
    menu_habitaciones.reservar_habitacion(cliente, SUSCRIPCIONES)
    cliente.mostrar_historial_reservas()


if __name__ == "__main__":
    main()
