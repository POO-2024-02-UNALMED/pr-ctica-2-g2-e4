from ..RegistroJuego import RegistroJuego
from .Juego import Juego
import random


class Ruleta(Juego):
    # Constantes de clase
    RIESGO_COLOR = 2.0  # 2.0f en Java
    RIESGO_NUMERO = 35.0  # 35.0f en Java

    def __init__(self, apuesta):
        super().__init__(apuesta, 0)  # Llamada al constructor de Juego

    def jugar(self, cliente, animador):
        if cliente.getRegistroJuego() is None:
            cliente.setRegistroJuego(RegistroJuego(cliente.getFichas()))

        # Inicio del juego
        print(animador.generarSaludo(
            cliente.getNombreCliente(), animador.getRol()))
        animador.manejarSuscripcion(cliente)

        print("¡Bienvenido a la Ruleta!")
        print("Opciones de apuesta:")
        print(
            f"1. Apostar por color (rojo o negro) - Riesgo: x{self.RIESGO_COLOR}")
        print(f"2. Apostar por número (0-36) - Riesgo: x{self.RIESGO_NUMERO}")

        eleccion = 0

        # Lógica de elección del jugador
        while True:
            try:
                eleccion = int(
                    input("Elige tu tipo de apuesta (1 para color, 2 para número): "))
                if eleccion in [1, 2]:
                    break
            except ValueError:
                continue

        if eleccion == 1:
            self.setRiesgo(self.RIESGO_COLOR)
            color_elegido = int(
                input("Elige un color (1 para rojo, 2 para negro): "))
            es_rojo = random.choice([True, False])  # Simula color aleatorio

            print("Girando la ruleta...")
            print(f"El color que salió es: {'Rojo' if es_rojo else 'Negro'}")

            if (color_elegido == 1 and es_rojo) or (color_elegido == 2 and not es_rojo):
                print("¡Felicidades! Ganaste apostando al color.")
                cliente.setFichas(cliente.getFichas() +
                                  int(self.apuesta * self.getRiesgo()))
                animador.otorgarRecompensa(cliente, True)
            else:
                print("Lo siento, perdiste.")
                cliente.setFichas(cliente.getFichas() - self.apuesta)
                animador.otorgarRecompensa(cliente, False)

        elif eleccion == 2:
            self.setRiesgo(self.RIESGO_NUMERO)
            numero_elegido = int(input("Elige un número entre 0 y 36: "))
            numero_ganador = random.randint(0, 36)  # Genera número ganador

            print("Girando la ruleta...")
            print(f"El número que salió es: {numero_ganador}")

            if numero_elegido == numero_ganador:
                print("¡Increíble! Ganaste apostando al número.")
                cliente.setFichas(cliente.getFichas() +
                                  int(self.apuesta * self.getRiesgo()))
                animador.otorgarRecompensa(cliente, True)
            else:
                print("Lo siento, perdiste.")
                cliente.setFichas(cliente.getFichas() - self.apuesta)
                animador.otorgarRecompensa(cliente, False)

        # Fin del juego
        print("¡Gracias por jugar a la Ruleta!")
        print(f"Tus fichas actuales: {cliente.getFichas()}")
