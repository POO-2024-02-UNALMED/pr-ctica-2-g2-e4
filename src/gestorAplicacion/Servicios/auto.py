from ..personal.cliente import Cliente

from typing import List, Optional

class Auto:
    def __init__(self, modelo: Optional[str] = None, placa: Optional[str] = None, cliente: Optional[Cliente] = None):
        self.estacionado = False
        self.modelo = modelo
        self.placa = placa
        self.cliente = cliente
        self.espacio_estacionamiento = [0, 0]
    
    def is_estacionado(self) -> bool:
        return self.estacionado
    
    def get_estacionado(self) -> bool:
        return self.estacionado
    
    def set_estacionado(self, estacionado: bool):
        self.estacionado = estacionado
    
    def get_modelo(self) -> Optional[str]:
        return self.modelo
    
    def set_modelo(self, modelo: str):
        self.modelo = modelo
    
    def get_placa(self) -> Optional[str]:
        return self.placa
    
    def set_placa(self, placa: str):
        self.placa = placa
    
    def get_cliente(self) -> Optional[Cliente]:
        return self.cliente
    
    def set_cliente(self, cliente: Cliente):
        self.cliente = cliente
    
    def get_espacio_estacionamiento(self) -> List[int]:
        return self.espacio_estacionamiento
    
    def set_espacio_estacionamiento(self, espacio_estacionamiento: List[int]):
        self.espacio_estacionamiento = espacio_estacionamiento
