import random
from ..RegistroJuego import RegistroJuego
from .Juego import Juego


class Blackjack(Juego):
    def __init__(self, apuesta):
        super().__init__(apuesta, 2.0)
        self.baraja = []
        self.manoJugador = []
        self.manoCrupier = []
        self.inicializarBaraja()

    # Inicializa y mezcla la baraja
    def inicializarBaraja(self):
        valores = ["2", "3", "4", "5", "6", "7",
                   "8", "9", "10", "J", "Q", "K", "A"]
        palos = ["corazones", "diamantes", "treboles", "picas"]

        self.baraja = [
            f"{valor} de {palo}" for palo in palos for valor in valores]
        random.shuffle(self.baraja)

    # Extrae la última carta de la baraja
    def sacarCarta(self):
        return self.baraja.pop()

    def jugar(self, cliente, animador):
        if cliente.getRegistroJuego() is None:
            cliente.setRegistroJuego(RegistroJuego(cliente.getFichas()))

        animador.generarSaludo(cliente.getNombreCliente(), animador.getRol())
        animador.manejarSuscripcion(cliente)

        # Repartir cartas iniciales
        self.manoJugador.append(self.sacarCarta())
        self.manoJugador.append(self.sacarCarta())
        self.manoCrupier.append(self.sacarCarta())
        self.manoCrupier.append(self.sacarCarta())

        # Mostrar cartas iniciales
        print(f"Tus cartas: {self.manoJugador}")
        print(f"Carta del crupier: {self.manoCrupier[0]} (otra oculta)")

        if self.calcularPuntaje(self.manoJugador) == 21:
            print("¡Blackjack! Ganaste con las dos primeras cartas.")
            cliente.setFichas(cliente.getFichas() + int(self.apuesta * 2.5))
            animador.otorgarRecompensa(cliente, True)
            return

        jugadorContinua = True
        while jugadorContinua:
            decision = input("¿Deseas pedir otra carta (s/n)? ").lower()
            if decision == "s":
                nuevaCarta = self.sacarCarta()
                self.manoJugador.append(nuevaCarta)
                print(f"Recibiste: {nuevaCarta}")

                puntaje = self.calcularPuntaje(self.manoJugador)
                if puntaje > 21:
                    print("Te pasaste de 21. ¡Perdiste!")
                    cliente.setFichas(cliente.getFichas() - self.apuesta)
                    animador.otorgarRecompensa(cliente, False)
                    return
            else:
                jugadorContinua = False

        while self.calcularPuntaje(self.manoCrupier) < 17:
            self.manoCrupier.append(self.sacarCarta())

        self.mostrarResultados(cliente, animador)

    def mostrarResultados(self, cliente, animador):
        puntajeJugador = self.calcularPuntaje(self.manoJugador)
        puntajeCrupier = self.calcularPuntaje(self.manoCrupier)
        ganoJugador = False

        print(f"Tu puntaje: {puntajeJugador}")
        print(f"Puntaje del crupier: {puntajeCrupier}")

        if puntajeJugador > puntajeCrupier or puntajeCrupier > 21:
            print("¡Ganaste!")
            cliente.setFichas(cliente.getFichas() + (self.apuesta * 2))
            ganoJugador = True
        else:
            print("Perdiste.")
            cliente.setFichas(cliente.getFichas() - self.apuesta)

        animador.otorgarRecompensa(cliente, ganoJugador)
        print("¡Gracias por jugar a Blackjack!")
        print(f"Tus fichas actuales: {cliente.getFichas()}")

    def calcularPuntaje(self, mano):
        puntaje = 0
        ases = 0

        for carta in mano:
            valor = carta.split(" ")[0]
            if valor in ["J", "Q", "K"]:
                puntaje += 10
            elif valor == "A":
                ases += 1
                puntaje += 11
            else:
                puntaje += int(valor)

        while puntaje > 21 and ases > 0:
            puntaje -= 10
            ases -= 1

        return puntaje
