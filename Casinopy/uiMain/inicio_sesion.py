class InicioSesion:
    def __init__(self, recepcionista):
        self.recepcionista = recepcionista

    def iniciar_sesion(self):
        nombre_ingresado = input("Ingrese su nombre: ")
        id_ingresado = int(input("Ingrese su ID: "))

        if self.recepcionista.nombre == nombre_ingresado and self.recepcionista.id == id_ingresado:
            print(f"Inicio de sesión exitoso. ¡Bienvenido, {self.recepcionista.nombre}!")
            return True
        else:
            print("Credenciales incorrectas. Acceso denegado.")
            return False