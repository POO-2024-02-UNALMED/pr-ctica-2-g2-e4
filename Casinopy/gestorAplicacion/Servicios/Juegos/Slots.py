from gestorAplicacion.Servicios import RegistroJuego
from gestorAplicacion.personal import Animador, Cliente
from .juego import Juego
import random


class Slots(Juego):
    # Atributos
    SIMBOLOS = ["pica", "corazon", "trebol", "diamante"]

    # Constructor
    def __init__(self, apuesta):
        super().__init__(apuesta, 1.5)

    # Método para tirar la rueda
    def tirarRueda(self):
        return self.SIMBOLOS[random.randint(0, len(self.SIMBOLOS) - 1)]
    # Método para obtener multiplicador

    def obtenerMultiplicador(self, simbolo):
        if simbolo == "pica":
            return 1.5
        elif simbolo == "corazon":
            return 2.0
        elif simbolo == "trebol":
            return 3.0
        elif simbolo == "diamante":
            return 8.0
        else:
            return 1.0

    # Método jugar implementado
    def jugar(self, cliente, animador):
        if cliente.getRegistroJuego() is None:
            cliente.setRegistroJuego(RegistroJuego(cliente.getFichas()))

        animador.generarSaludo(cliente.getNombreCliente(), animador.getRol())
        animador.manejarSuscripcion(cliente)

        # Tirar las tres ruedas
        rueda1 = self.tirarRueda()
        rueda2 = self.tirarRueda()
        rueda3 = self.tirarRueda()

        # Mostrar resultados
        print(f"Rueda 1: {rueda1}")
        print(f"Rueda 2: {rueda2}")
        print(f"Rueda 3: {rueda3}")

        # Verificar ganador
        if rueda1 == rueda2 and rueda2 == rueda3:
            multiplicador = self.obtenerMultiplicador(rueda1)
            ganancia = self.apuesta * multiplicador
            cliente.setFichas(cliente.getFichas() + int(ganancia))
            print(
                f"¡Ganaste! Multiplicador: {multiplicador}. Ganancia: {ganancia} fichas.")

            animador.otorgarRecompensa(cliente, True)

            # Premio especial
            if rueda1 == "diamante" and rueda2 == "diamante" and rueda3 == "diamante":
                print("¡Premio especial por Diamantes! ¡Felicidades!")
                cliente.setFichas(cliente.getFichas() + int(ganancia) + 10)
        else:
            print("Lo siento, no ganaste. Mejor suerte la próxima vez.")
            cliente.setFichas(cliente.getFichas() - self.apuesta)
            animador.otorgarRecompensa(cliente, False)

        print("¡Gracias por jugar Slots!")
        print(f"Tus fichas actuales: {cliente.getFichas()}")
