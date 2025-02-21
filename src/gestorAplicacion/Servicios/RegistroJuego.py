class RegistroJuego:
    def __init__(self, fichasInicio=None):
        # Constructor sin parámetros
        if fichasInicio is None:
            self._fichasInicio = 0
            self.fichasFinal = 0
            self.partidasGanadas = 0
            self.partidasJugadas = 0
            self.rachaVictorias = 0
            self.porcentajeVictorias = 0.0
        # Constructor con parámetro
        else:
            self._fichasInicio = fichasInicio
            self.fichasFinal = 0
            self.partidasGanadas = 0
            self.partidasJugadas = 0
            self.rachaVictorias = 0
            self.porcentajeVictorias = 0.0

    # Getters y Setters (se mantienen como métodos explícitos)
    def getFichasInicio(self):
        return self._fichasInicio

    def getFichasFinal(self):
        return self.fichasFinal

    def setFichasFinal(self, fichasFinal):
        self.fichasFinal = fichasFinal

    def getPartidasGanadas(self):
        return self.partidasGanadas

    def setPartidasGanadas(self, partidasGanadas):
        self.partidasGanadas = partidasGanadas

    def getPorcentajeVictorias(self):
        return self.porcentajeVictorias

    def getPartidasJugadas(self):
        return self.partidasJugadas

    def setPartidasJugadas(self, partidasJugadas):
        self.partidasJugadas = partidasJugadas

    # Métodos de lógica de negocio
    def calcularPorcentajeVictorias(self):
        if self.partidasJugadas != 0:
            self.porcentajeVictorias = self.partidasGanadas / self.partidasJugadas

    def incrementarPartidasJugadas(self, ganada):
        self.partidasJugadas += 1
        if ganada:
            self.partidasGanadas += 1
            self.rachaVictorias += 1
        else:
            self.rachaVictorias = 0
        self.calcularPorcentajeVictorias()

    def incrementarRacha(self):
        self.rachaVictorias += 1

    def reiniciarRacha(self):
        self.rachaVictorias = 0

    # Método toString
    def __str__(self):
        return (
            "Estadísticas del Jugador:\n"
            "--------------------------\n"
            f"Fichas al inicio: {self._fichasInicio}\n"
            f"Fichas al final: {self.fichasFinal}\n"
            f"Partidas jugadas: {self.partidasJugadas}\n"
            f"Partidas ganadas: {self.partidasGanadas}\n"
            f"Porcentaje de victorias: {self.porcentajeVictorias * 100:.2f}%\n"
            f"Racha de victorias: {self.rachaVictorias}\n"
        )

    # Getter para racha de victorias
    def getRachaVictorias(self):
        return self.rachaVictorias
