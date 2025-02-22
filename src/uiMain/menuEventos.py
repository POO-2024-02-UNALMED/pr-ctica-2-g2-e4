from ..gestorAplicacion.Servicios import evento
from ..gestorAplicacion.Servicios import asiento
from ..gestorAplicacion.personal import Cliente, Recepcionista
from ui_main import EventosUIConsole

class EventoMain:
    @staticmethod
    def funcionalidad_evento():
        print("\n=== ¡Bienvenido al área de eventos del casino! ===\n")
        print("Por favor, deme su identificación nuevamente para confirmar su registro.")

        consola = EventosUIConsole()
        id_cliente = consola.pedir_id()
        cliente = Recepcionista.identificar_cliente(id_cliente)

        if cliente:
            print("\n--------------------- DATOS USUARIO ---------------------")
            print(f"Hola {cliente.get_nombre_cliente()}!")
            print(f"Su suscripción actual es: {cliente.get_suscripcion().get_tipo_suscripcion()}")
            print(f"Su saldo actual es: {cliente.get_fichas()}")

            if cliente.get_suscripcion().get_tipo_suscripcion().lower() == "platinum":
                print("Como miembro Platinum, se le ha asignado automáticamente un asiento en Primera Fila.")
                print("Además, recibirá una bebida especial gratuita durante el espectáculo.")

            evento.inicializar_eventos()
            print("\n------------------------------- EVENTOS -------------------------------")
            evento.mostrar_eventos()
            print("-----------------------------------------------------------------------")

            print("\nSeleccione un evento ingresando el número correspondiente:")
            opcion_evento = consola.pedir_evento()
            evento_seleccionado = evento.get_evento_por_indice(opcion_evento)

            # Aplicar descuento
            descuento = cliente.get_suscripcion().get_descuento()
            costo_original = evento_seleccionado.get_precio()
            costo_con_descuento = int(costo_original * (1 - descuento))

            print("-------- Descuento por suscripción --------")
            print(f"El costo original del evento \"{evento_seleccionado.get_nombre()}\" es de {costo_original} fichas.")
            print(f"Como miembro \"{cliente.get_suscripcion().get_tipo_suscripcion()}\", recibe un descuento del {descuento * 100}%.")
            print(f"El costo final con descuento es de {costo_con_descuento} fichas.")
            cliente.set_fichas(cliente.get_fichas() - costo_con_descuento)
            print(f"Su nuevo saldo es: {cliente.get_fichas()}\n")
            print("----------------------------------")

            # Inicialización de asientos
            evento_seleccionado.inicializar_asientos()

            if cliente.get_suscripcion().get_tipo_suscripcion().lower() == "platinum":
                zona_seleccionada = asiento.ZonaAsiento.PALCO
            else:
                print("\nAquí tienes los asientos disponibles:\n")
                evento_seleccionado.mostrar_zonas_asientos()
                zona_seleccionada = consola.pedir_zona_asiento()

            Recepcionista.procesar_seleccion_evento(cliente, evento_seleccionado, zona_seleccionada, costo_con_descuento)

        else:
            print("No se encontró ningún registro para esta identificación. Por favor, regístrese primero o ingrese un ID válido.")