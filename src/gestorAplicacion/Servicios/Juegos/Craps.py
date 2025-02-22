from gestorAplicacion.Servicios.RegistroJuego import RegistroJuego
from gestorAplicacion.personal.animador import Animador
from gestorAplicacion.personal.cliente import Cliente
from gestorAplicacion.Servicios.Juegos import Juego
import random


class Craps(Juego):
    def __init__(self, apuesta):
        super().__init__(apuesta, 2.0)  # Riesgo inicial 2.0

    def jugar(self, cliente, animador):
        # Verificar y crear registro de juego
        if cliente.getRegistroJuego() is None:
            cliente.setRegistroJuego(RegistroJuego(cliente.getFichas()))

        # Inicio del juego
        print(animador.generarSaludo(
            cliente.getNombreCliente(), animador.getRol()))
        animador.manejarSuscripcion(cliente)

        print("¡Comienza el juego de Craps!")
        riesgo_actual = self.getRiesgo()  # Riesgo dinámico

        # Lógica del primer tiro
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        primer_tiro = dado1 + dado2
        print(f"Primer tiro: {primer_tiro}")

        if primer_tiro == 7:
            print("¡Felicidades! Premio especial por sacar un 7 en el primer tiro.")
            cliente.setFichas(cliente.getFichas() +
                              int(round((self.apuesta + 10) * riesgo_actual)))
            animador.otorgarRecompensa(cliente, True)
            return
        elif primer_tiro == 11:
            print("¡Felicidades! Ganaste en el primer tiro.")
            cliente.setFichas(cliente.getFichas() +
                              int(round(self.apuesta * riesgo_actual)))
            animador.otorgarRecompensa(cliente, True)
            return
        elif primer_tiro in [2, 3, 12]:
            print("Craps. Perdiste en el primer tiro.")
            cliente.setFichas(cliente.getFichas() - self.apuesta)
            animador.otorgarRecompensa(cliente, False)
            return

        # Lógica después del primer tiro
        punto = primer_tiro
        print(
            f"Tu punto es: {punto}. Debes volver a sacar {punto} antes de que salga un 7.")

        while True:
            dado1 = random.randint(1, 6)
            dado2 = random.randint(1, 6)
            nuevo_tiro = dado1 + dado2
            print(f"Nuevo tiro: {nuevo_tiro}")

            if nuevo_tiro == punto:
                print("¡Felicidades! Ganaste al volver a sacar tu punto.")
                cliente.setFichas(cliente.getFichas() +
                                  int(round(self.apuesta * riesgo_actual)))
                animador.otorgarRecompensa(cliente, True)
                return
            elif nuevo_tiro == 7:
                print("Salió un 7. Perdiste.")
                cliente.setFichas(cliente.getFichas() - self.apuesta)
                animador.otorgarRecompensa(cliente, False)
                return

            # Aumentar riesgo
            riesgo_actual += 0.5
            self.setRiesgo(riesgo_actual)
            print(f"El riesgo actual ha aumentado a: {riesgo_actual}x")
