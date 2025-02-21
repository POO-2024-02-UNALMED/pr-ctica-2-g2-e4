from gestorAplicacion.Servicios import RegistroJuego
from gestorAplicacion.Servicios.Juegos import Blackjack, Ruleta, Craps, Slots
from gestorAplicacion.personal import Animador, Cliente


class MainJuegos:
    @staticmethod
    def funcionalidadJugar(usuarioActual):
        animador = Animador()
        continuar = True

        while continuar:
            # Mostrar menú de opciones
            print("\nSeleccione un juego para jugar:")
            print("1. Blackjack")
            print("2. Ruleta")
            print("3. Craps")
            print("4. Slots")
            print("5. Mostrar estadísticas")
            print("0. Salir")

            opcion = int(input("Opción: "))

            if opcion == 0:
                print("Gracias por jugar. ¡Hasta pronto!")
                continuar = False
                continue

            if opcion == 5:
                registro = usuarioActual.getRegistroJuego()
                print(registro)
                continue

            # Validación de apuesta
            try:
                apuesta = int(
                    input("Ingrese la cantidad de fichas que desea apostar: "))
            except ValueError:
                print("Debe ingresar un número válido.")
                continue

            if apuesta <= 0:
                print("La cantidad apostada debe ser mayor a 0.")
                continue

            if apuesta > usuarioActual.getFichas():
                print("No tienes suficientes fichas para apostar esa cantidad.")
                continue

            # Lógica de selección de juego
            if opcion == 1:
                juego = Blackjack(apuesta)
            elif opcion == 2:
                juego = Ruleta(apuesta)
            elif opcion == 3:
                juego = Craps(apuesta)
            elif opcion == 4:
                juego = Slots(apuesta)
            else:
                print("Opción no válida. Intente de nuevo.")
                continue

            # Ejecutar el juego seleccionado
            juego.jugar(usuarioActual, animador)
