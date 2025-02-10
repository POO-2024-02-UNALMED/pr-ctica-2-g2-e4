import random
from persistencia import Persistencia # type: ignore
from ...Casinopy.gestor_aplicacion.habitaciones.habitacion import Habitacion
from ...Casinopy.gestor_aplicacion.usuarios.recepcionista import Recepcionista
from ...Casinopy.gestor_aplicacion.usuarios.cliente import Cliente

def main():
    try:
        # Crear objetos de ejemplo
        random.seed()
        hab1 = Habitacion(101, 100, "Estándar", random.choice(["al mar", "a la ciudad"]),
                          random.choice(["Pequeña", "Grande"]),
                          random.choice([True, False]), random.choice([True, False]), 0, False)

        hab2 = Habitacion(102, 200, "Suite", random.choice(["al mar", "a la ciudad"]),
                          random.choice(["Pequeña", "Grande"]),
                          random.choice([True, False]), random.choice([True, False]), 0, False)

        recepcionista = Recepcionista("Ana", 1234)
        cliente = Cliente("Carlos", "456789", "Premium")

        # Guardar objetos individuales
        Persistencia.guardar_objeto(hab1, "habitacion1.dat")
        Persistencia.guardar_objeto(recepcionista, "recepcionista.dat")
        Persistencia.guardar_objeto(cliente, "cliente.dat")

        # Guardar una lista de habitaciones
        habitaciones = [hab1, hab2]
        Persistencia.guardar_lista(habitaciones, "habitaciones.dat")

        # Cargar los objetos
        habitacion_cargada = Persistencia.cargar_objeto("habitacion1.dat")
        recepcionista_cargado = Persistencia.cargar_objeto("recepcionista.dat")
        cliente_cargado = Persistencia.cargar_objeto("cliente.dat")

        habitaciones_cargadas = Persistencia.cargar_lista("habitaciones.dat")

        # Mostrar los datos cargados
        print(f"Habitación cargada: {habitacion_cargada.numero}")
        print(f"Recepcionista cargado: {recepcionista_cargado.nombre}")
        print(f"Cliente cargado: {cliente_cargado.nombre}")
        print("Lista de habitaciones cargadas: ")
        for h in habitaciones_cargadas:
            print(h.numero)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()