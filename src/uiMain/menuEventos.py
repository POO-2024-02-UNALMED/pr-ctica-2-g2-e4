from ..gestorAplicacion.Servicios import evento
from ..gestorAplicacion.Servicios import asiento
from ..gestorAplicacion.personal import Cliente, Recepcionista


class EventoMain:
    @staticmethod
    def funcionalidad_evento():
        print("\n=== ¡Bienvenido al área de eventos del casino! ===\n")
        print("Por favor, deme su identificación nuevamente para confirmar su registro.")

        id_cliente = input("Ingrese su ID de cliente: ")
        cliente = Recepcionista.identificar_cliente(id_cliente)

        if cliente:
            print("\n--------------------- DATOS USUARIO ---------------------")
            print(f"Hola {cliente.get_nombre_cliente()}!")

            tipo_suscripcion = cliente.get_suscripcion().get_tipo_suscripcion().lower()
            print(f"Su suscripción actual es: {tipo_suscripcion.capitalize()}")
            print(f"Su saldo actual es: {cliente.get_fichas()}")

            evento.inicializar_eventos()
            print("\n------------------------------- EVENTOS -------------------------------")
            evento.mostrar_eventos()
            print("-----------------------------------------------------------------------")

            while True:
                try:
                    opcion_evento = int(input("\nSeleccione un evento ingresando el número correspondiente: "))
                    evento_seleccionado = evento.get_evento_por_indice(opcion_evento)
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido.")

            # Aplicar descuento
            descuento = cliente.get_suscripcion().get_descuento()
            costo_original = evento_seleccionado.get_precio()
            costo_con_descuento = int(costo_original * (1 - descuento))

            print("-------- Descuento por suscripción --------")
            print(f"El costo original del evento \"{evento_seleccionado.get_nombre()}\" es de {costo_original} fichas.")
            print(f"Como miembro \"{tipo_suscripcion.capitalize()}\", recibe un descuento del {descuento * 100}%.")
            print(f"El costo final con descuento es de {costo_con_descuento} fichas.")
            print("----------------------------------")

            # Verificar si el cliente tiene suficientes fichas
            if cliente.get_fichas() < costo_con_descuento:
                print("No tiene suficientes fichas para pagar este evento.")
                print("Por favor, recargue su saldo antes de intentar comprar un boleto.")
                return  

            # Restar fichas si tiene saldo suficiente
            cliente.set_fichas(cliente.get_fichas() - costo_con_descuento)
            print(f"Pago exitoso. Su nuevo saldo es: {cliente.get_fichas()} fichas.\n")

            # Seleccionar asiento (asiento)
            zona_seleccionada = asiento.seleccionar_asiento(cliente, evento_seleccionado)

            # Procesar evento
            Recepcionista.procesar_seleccion_evento(cliente, evento_seleccionado, zona_seleccionada, costo_con_descuento)

        else:
            print("No se encontró ningún registro para esta identificación. Por favor, regístrese primero o ingrese un ID válido.")
