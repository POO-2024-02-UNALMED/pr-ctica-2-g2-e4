from typing import List, Optional
from gestorAplicacion.Servicios import Ingrediente

class Bebida:
    def __init__(self, nombre: str = "", precio: int = 0, dulce: bool = False, amargo: bool = False, 
                 acido: bool = False, alcoholico: bool = False, favorito: int = 0, 
                 ingredientes: Optional[List[Ingrediente]] = None):
        self.nombre = nombre
        self.precio = precio
        self.dulce = dulce
        self.amargo = amargo
        self.acido = acido
        self.alcoholico = alcoholico
        self.favorito = favorito
        self.ingredientes = ingredientes if ingredientes is not None else []

    def __str__(self) -> str:
        descripcion = f"Bebida: {self.nombre}\nSabores: "
        if self.dulce:
            descripcion += "Dulce "
        if self.amargo:
            descripcion += "Amargo "
        if self.acido:
            descripcion += "Acido "
        if self.alcoholico:
            descripcion += "Alcoholico "
        descripcion += "\nIngredientes: "
        descripcion += ", ".join([f"{ing.get_nombre()} ({ing.get_calidad()})" for ing in self.ingredientes])
        return descripcion

    def get_nombre(self) -> str:
        return self.nombre

    def set_nombre(self, nombre: str):
        self.nombre = nombre

    def get_precio(self) -> int:
        return self.precio

    def set_precio(self, precio: int):
        self.precio = precio

    def is_dulce(self) -> bool:
        return self.dulce

    def set_dulce(self, dulce: bool):
        self.dulce = dulce

    def is_amargo(self) -> bool:
        return self.amargo

    def set_amargo(self, amargo: bool):
        self.amargo = amargo

    def is_acido(self) -> bool:
        return self.acido

    def set_acido(self, acido: bool):
        self.acido = acido

    def is_alcoholico(self) -> bool:
        return self.alcoholico

    def set_alcoholico(self, alcoholico: bool):
        self.alcoholico = alcoholico

    def get_favorito(self) -> int:
        return self.favorito

    def set_favorito(self, favorito: int):
        self.favorito = favorito

    def get_ingredientes(self) -> List[Ingrediente]:
        return self.ingredientes

    def set_ingredientes(self, ingredientes: List[Ingrediente]):
        self.ingredientes = ingredientes
