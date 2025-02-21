class Cuenta:
    def __init__(self):
        self.bebidas_pedidas = []
        self.total = 0.0

    def agregar_bebida(self, bebida):
        self.bebidas_pedidas.append(bebida)
        self.total += bebida.precio

    def get_total(self):
        return self.total

    def get_bebidas_pedidas(self):
        return self.bebidas_pedidas