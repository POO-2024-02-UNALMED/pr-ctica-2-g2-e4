class Bartender:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id

    def dar_bienvenida(self, cliente):
        print(f"¡Bienvenido, {cliente.nombre}!")
        print(f"Su nivel de suscripción es: {cliente.suscripcion.nivel}")

        if cliente.suscripcion.nivel == "Premium":
            print("¡Disfrute de un aperitivo extra y su primera bebida gratis!")
        elif cliente.suscripcion.nivel == "Estándar":
            print("¡Disfrute de un aperitivo extra!")
        else:
            print("¡Gracias por ser nuestro cliente! Pregunte por nuestras ofertas.")