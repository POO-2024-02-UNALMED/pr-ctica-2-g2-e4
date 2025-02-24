from ..personal.empleado import Empleado

class Conserje(Empleado):
    def __init__(self, rol, puesto):
        super().__init__(rol, puesto)

    def get_rol(self):
        return "Conserje"

    def limpiar_habitacion(self, habitacion):
        if habitacion.ocupada:
            if not habitacion.sucia:
                print(f"La habitación {habitacion.numero} está limpia. No se requiere limpieza.")
            else:
                habitacion.limpiar()
                print(f"La habitación {habitacion.numero} ha sido limpiada.")
        else:
            print(f"La habitación {habitacion.numero} no está ocupada. No se puede limpiar.")