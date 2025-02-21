from .bebida import Bebida
from .cuenta import Cuenta

class Bar:
    def __init__(self):
        self.menu = [
            Bebida("Cerveza", 5.0, "neutral"),
            Bebida("Vino", 10.0, "muy recomendado"),
            Bebida("Refresco", 2.0, "poco recomendado"),
        ]

    def mostrar_menu(self):
        print("\n--- Menú de Bebidas ---")
        for bebida in self.menu:
            print(bebida)

    def atender_cliente(self, cliente, bartender):
        
        self.mostrar_menu()
        continuar = True
        cuenta = Cuenta()

        while continuar:
            pedido = input("Seleccione la bebida que desea pedir (o ingrese 'salir' para finalizar): ")
            if pedido.lower() == "salir":
                continuar = False
                break

            bebida_pedida = self.buscar_bebida(pedido)
            if bebida_pedida:
                cuenta.agregar_bebida(bebida_pedida)
                print(f"Bebida {bebida_pedida.nombre} añadida a la cuenta.")
            else:
                print("Bebida no encontrada en el menú.")
        cliente.cuenta_total += bebida_pedida.precio
        print(f"Total de la cuenta de la habitación: ${cliente.cuenta_total}")
        propina_respuesta = input("¿Desea dejar una propina? (si/no): ")
        if propina_respuesta.lower() == "si":
            print("Gracias por su propina.")
        print("Gracias por su visita al bar. ¡Que tenga un buen día!")

    def buscar_bebida(self, nombre):
        for bebida in self.menu:
            if bebida.nombre.lower() == nombre.lower():
                return bebida
        return None