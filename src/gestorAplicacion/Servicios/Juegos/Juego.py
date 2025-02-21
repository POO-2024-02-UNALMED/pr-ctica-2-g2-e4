from abc import ABC, abstractmethod
import math
from gestorAplicacion.personal.cliente import Cliente    # Importación adaptada
from gestorAplicacion.personal import Animador   # desde paquete personal


class Juego(ABC):
    # Atributos
    apuesta = None
    __riesgo = None

    # Constructor
    def __init__(self, apuesta, riesgo):
        self.apuesta = apuesta
        self.__riesgo = riesgo

    # Getters y Setters (se mantienen como en Java)
    def getApuesta(self):
        return self.apuesta

    def setApuesta(self, apuesta):
        self.apuesta = apuesta

    def getRiesgo(self):
        return self.__riesgo

    def setRiesgo(self, riesgo):
        self.__riesgo = riesgo

    # Método devolverApuesta
    def devolverApuesta(self, cliente):
        fichasGenerales = cliente.getFichas()
        fichasGanadas = int(math.floor(self.apuesta * self.__riesgo))
        cliente.setFichas(fichasGenerales + fichasGanadas)

    # Método abstracto
    @abstractmethod
    def jugar(self, cliente, animador):
        pass
