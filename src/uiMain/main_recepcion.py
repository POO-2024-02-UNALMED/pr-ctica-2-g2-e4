from src.gestorAplicacion.Servicios.bebida import Bebida
from src.gestorAplicacion.Servicios.auto import Auto
from src.gestorAplicacion.Servicios.casino import Casino
from src.gestorAplicacion.personal import Bartender, Cliente, Recepcionista
from src.gestorAplicacion.personal.valet import Valet
from uiMain import RecepcionUIConsole


def funcionalidad_recepcion():
    consola = RecepcionUIConsole()
    
    # Inicializar objetos
    valet = Valet("Valet", "Estacionamiento")
    recepcionista = Recepcionista("Recepcionista", "Recepcion")
    bartender = Bartender("Bartender", "Barra")
    
    # Interacción 1
    auto = None
    print("Bienvenido, por favor deme su identificación para ver si tiene un registro en el casino")
    id = consola.pedir_id()
    cliente_old = Valet.identificar_cliente(id)
    
    if cliente_old:
        print(f"Hola {cliente_old.get_nombre_cliente()}! Bienvenido al casino")
    else:
        print("No hay registros para esa identificación")
    
    modelo = consola.pedir_modelo()
    print(f"Modelo: {modelo}")
    placa = consola.pedir_placa()
    print(f"Placa: {placa}")
    Casino.inicializar_estacionamiento(5, 5)
    
    print(Casino.mostrar_espacios_estacionamiento(cliente_old.get_suscripcion() if cliente_old else None))
    
    columna, fila = 0, 0
    while auto is None:
        columna = consola.pedir_columna()
        fila = consola.pedir_fila()
        auto = valet.estacionar_registrar_auto(modelo, placa, columna, fila, id)
    
    print(f"Auto estacionado en [{columna},{fila}]")
    print(f"Su {modelo} con placa {placa} fue estacionado correctamente")
    
    # Interacción 2
    cliente_now = None
    nombre = cliente_old.get_nombre_cliente() if cliente_old else consola.pedir_nombre()
    saldo = consola.pedir_saldo()
    
    while cliente_now is None:
        edad = consola.pedir_edad()
        cliente_now = recepcionista.registrar_cliente(edad, saldo, id, nombre, auto)
    
    print(f"Ha sido registrado exitosamente, {cliente_now.get_nombre_cliente()}")
    dinero_a_cambiar = consola.cambiar_fichas(cliente_now)
    recepcionista.cambiar_fichas(cliente_now, dinero_a_cambiar)
    print(f"Has cambiado {dinero_a_cambiar} pesos por {cliente_now.get_fichas()} fichas.")
    
    # Interacción 3
    bebida_bienvenida = bartender.preparar_bebida_bienvenida(cliente_now)
    print(f"Por favor, reciba esta {bebida_bienvenida.get_nombre()} que le preparamos especialmente para darle la bienvenida")
    print(bebida_bienvenida)
    consola.encuesta_bebida_bienvenida(bebida_bienvenida)
    print("Ya puede acceder a las instalaciones del casino, disfrute su estadía")
    
    return cliente_now
