from gestorAplicacion.Servicios import Suscripcion, RegistroJuego
from gestorAplicacion.personal.empleado import Empleado
from gestorAplicacion.personal.cliente import Cliente


class Animador(Empleado):
    def __init__(self):
        super().__init__("Animador", "Juegos")  # Rol y puesto fijos

    # Generar saludo personalizado
    def generarSaludo(self, nombreCliente, Rol):
        return f"¡Hola {nombreCliente}! Soy tu {Rol}. ¡Vamos a divertirnos!"

    # Manejar la suscripción del cliente
    def manejarSuscripcion(self, cliente):
        suscripcion = cliente.getSuscripcion()
        if suscripcion is None:
            print("No tienes una suscripción activa. ¿Deseas adquirir una?")
        else:
            print(
                f"Tu suscripción actual es: {suscripcion.getTipoSuscripcion()}")

    # Entregar fichas al cliente según suscripción
    def entregarFichas(self, cliente):
        suscripcion = cliente.getSuscripcion()
        if suscripcion is not None:
            fichasCompensacion = suscripcion.getFichaCompensacion()
            cliente.setFichas(cliente.getFichas() + fichasCompensacion)
            print(f"Se han entregado {fichasCompensacion} fichas a {cliente.getNombreCliente()} "
                  f"como parte de su suscripción {suscripcion.getTipoSuscripcion()}.")
        else:
            print(
                "No se pueden entregar fichas porque el cliente no tiene una suscripción activa.")

    # Método para el final de cada partida
    def otorgarRecompensa(self, cliente, partidaGanada):
        registroJuego = cliente.getRegistroJuego()

        registroJuego.incrementarPartidasJugadas(partidaGanada)
        registroJuego.setFichasFinal(cliente.getFichas())

        racha = registroJuego.getRachaVictorias()
        partidasJugadas = registroJuego.getPartidasJugadas()
        porcentajeVictorias = registroJuego.getPorcentajeVictorias()

        # Verificar racha de 3 victorias
        if racha >= 3:
            print(
                f"¡Felicidades {cliente.getNombreCliente()}, tienes una racha de {racha} victorias!")

        # Detectar posible trampa
        if partidasJugadas > 10 and porcentajeVictorias == 1.0:
            print(f"Se sospecha trampa del cliente: {cliente.getNombreCliente()}! "
                  "Has jugado más de 10 partidas y tienes un 100% de victorias.")
            cliente.getSuscripcion().setTipoSuscripcion("Vetado")
            print("Tu suscripción ahora es 'Vetado'.")

    # Métodos comentados del original
    # def entregarPremio(self, partidaGanada, premioEspecial):
    #     pass

    # def pedirBebida(self, bebidaFavorita, suscripcion, Bebidas):
    #     pass
