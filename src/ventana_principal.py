import tkinter as tk
from tkinter import Menu, Frame, Label, Button, messagebox
import random
from fieldFrame import FieldFrame  # Importing FieldFrame for structured forms
import ventana_inicio  # Importing Ventana_Inicio to allow navigation
from gestorAplicacion.personal.cliente import Cliente
from gestorAplicacion.personal.recepcionista import Recepcionista
from gestorAplicacion.personal.bartender import Bartender
from gestorAplicacion.personal.valet import Valet
from gestorAplicacion.Servicios.suscripcion import Suscripcion
from gestorAplicacion.Servicios.bebida import Bebida
from gestorAplicacion.Servicios.ingrediente import Ingrediente
from gestorAplicacion.Servicios.auto import Auto
from gestorAplicacion.Servicios.casino import Casino


class Ventana_Principal:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Casino")
        self.root.geometry("1000x600")

        # 🔹 ZONE 0: Application Title
        self.title_label = Label(root, text="Sistema de Casino", font=(
            "Arial", 16, "bold"), bg="gray", fg="white")
        self.title_label.pack(fill="x")

        # 🔹 ZONE 1: Menu Bar
        menu_bar = Menu(root)

        archivo_menu = Menu(menu_bar, tearoff=0)
        archivo_menu.add_command(
            label="Aplicación", command=self.show_app_info)
        archivo_menu.add_command(label="Salir", command=self.return_to_inicio)
        menu_bar.add_cascade(label="Archivo", menu=archivo_menu)

        procesos_menu = Menu(menu_bar, tearoff=0)
        procesos_menu.add_command(
            label="Recepción", command=self.func_recepcion)
        procesos_menu.add_command(label="Juegos", command=self.func_juegos)
        procesos_menu.add_command(label="Bar", command=self.func_bar)
        procesos_menu.add_command(label="Hotel", command=self.func_hotel)
        procesos_menu.add_command(label="Eventos", command=self.func_eventos)
        menu_bar.add_cascade(label="Procesos y Consultas", menu=procesos_menu)

        ayuda_menu = Menu(menu_bar, tearoff=0)
        ayuda_menu.add_command(label="Acerca de", command=self.show_authors)
        menu_bar.add_cascade(label="Ayuda", menu=ayuda_menu)

        root.config(menu=menu_bar)

        # 🔹 ZONE 2: Main Interaction Area
        self.frame_main = Frame(root, bg="white")
        self.frame_main.pack(expand=True, fill="both", padx=10, pady=10)

        # State Tracking: Funcionalidades 2-5 have disabled text fields until Recepción is completed
        self.recepcion_completed = False

        # Default startup screen
        self.show_welcome_screen()

        # Inicialización de objetos
        self.inicializar_obj_bar()
        self.inicializar_clientes()
        self.usuarioActual = None

    def show_welcome_screen(self):
        """ Displays the welcome message on startup """
        for widget in self.frame_main.winfo_children():
            widget.destroy()

        Label(self.frame_main, text="Administrador Sistema de Casino",
              font=("Arial", 16, "bold"), bg="white").pack(pady=10)
        Label(self.frame_main, text="Consulta y administra información sobre el casino y sus funcionalidades.", font=(
            "Arial", 12), bg="white").pack(pady=5)

    # 🔹 FUNCIONALIDAD 1: RECEPCIÓN
    # Interacción 1
    def func_recepcion(self):
        """ Handles Recepción functionality (Step 1: Client Identification & Parking) """
        for widget in self.frame_main.winfo_children():
            widget.destroy()

        Label(self.frame_main, text="Recepción - Identificación y Estacionamiento",
              font=("Arial", 14, "bold"), bg="white").pack(pady=10)

        # 🔹 Step 1: Client ID, Car Model, and Plate
        criterios = ["ID Cliente", "Modelo Auto", "Placa Auto"]
        valores = ["", "", ""]
        habilitados = [True, True, True]  # All fields editable

        self.field_identificacion = FieldFrame(
            self.frame_main, "Criterio", criterios, "Valor", valores, habilitados)
        self.field_identificacion.pack(pady=10)

        # Label to display parking lot visualization
        self.label_parking_display = Label(self.frame_main, text="", font=(
            "Courier", 12), bg="white", justify="left")
        self.label_parking_display.pack(pady=5)

        self.label_feedback = Label(
            self.frame_main, text="", font=("Arial", 12), bg="white")
        self.label_feedback.pack(pady=5)

        Button(self.frame_main, text="Verificar ID y Mostrar Estacionamiento",
               command=self.verify_id_and_show_parking).pack(pady=5)

        # Initializing objects
        self.valet = Valet("Valet", "Estacionamiento")
        self.recepcionista = Recepcionista("Recepcionista", "Recepción")
        self.bartender = Bartender("Bartender", "Barra")
        self.usuarioOld = None
        self.parked_car = None

    def verify_id_and_show_parking(self):
        """ Checks ID, registers a new user if necessary, and displays the parking lot """
        id_cliente = self.field_identificacion.obtener_valor_por_criterio(
            "ID Cliente")
        modelo = self.field_identificacion.obtener_valor_por_criterio(
            "Modelo Auto")
        placa = self.field_identificacion.obtener_valor_por_criterio(
            "Placa Auto")

        if not id_cliente or not modelo or not placa:
            messagebox.showerror(
                "Error", "Ingrese un ID, modelo de auto y placa válidos.")
            return

        self.usuarioOld = self.valet.identificar_cliente(id_cliente)

        if self.usuarioOld:
            self.label_feedback.config(
                text=f"Hola {self.usuarioOld.get_nombre_cliente()}! Bienvenido al casino.")
            suscripcion_cliente = self.usuarioOld.get_suscripcion()
        else:
            self.label_feedback.config(
                text="No hay registros. Continuando con nuevo registro...")
            suscripcion_cliente = None

        # 🔹 Step 2: Initialize and Show Parking Lot
        # Inicializa un estacionamiento de 5x5
        Casino.inicializar_estacionamiento(5, 5)
        estacionamiento_str = Casino.mostrar_espacios_estacionamiento(
            suscripcion_cliente)

        # Actualiza la visualización en la GUI
        self.label_parking_display.config(text=estacionamiento_str)

        # Move to next step: Ask for parking position
        self.ask_parking_position()

    def ask_parking_position(self):
        """ Displays fields for selecting a parking space """
        for widget in self.frame_main.winfo_children():
            if widget not in [self.label_parking_display, self.label_feedback]:
                widget.destroy()

        Label(self.frame_main, text="Seleccione la ubicación de estacionamiento", font=(
            "Arial", 14, "bold"), bg="white").pack(pady=10)

        criterios = ["Columna Estacionamiento", "Fila Estacionamiento"]
        valores = ["", ""]
        habilitados = [True, True]

        self.field_parking = FieldFrame(
            self.frame_main, "Criterio", criterios, "Valor", valores, habilitados)
        self.field_parking.pack(pady=10)

        Button(self.frame_main, text="Estacionar Auto",
               command=self.park_car).pack(pady=5)

    def park_car(self):
        """ Registers the car in the selected parking spot, with proper exception handling """
        columna = self.field_parking.obtener_valor_por_criterio(
            "Columna Estacionamiento")
        fila = self.field_parking.obtener_valor_por_criterio(
            "Fila Estacionamiento")

        if not columna or not fila:
            messagebox.showerror(
                "Error", "Seleccione una columna y fila válidas para estacionar.")
            return

        # Se intenta convertir los valores a enteros
        try:
            columna = int(columna)
            fila = int(fila)
        except ValueError:
            messagebox.showerror(
                "Error", "La columna y la fila deben ser números enteros.")
            return

        id_cliente = self.field_identificacion.obtener_valor_por_criterio(
            "ID Cliente")
        modelo = self.field_identificacion.obtener_valor_por_criterio(
            "Modelo Auto")
        placa = self.field_identificacion.obtener_valor_por_criterio(
            "Placa Auto")

        # Se llama al método de valet para registrar el auto
        self.parked_car = self.valet.estacionar_registrar_auto(
            modelo, placa, columna, fila, id_cliente)

        if self.parked_car:
            messagebox.showinfo(
                "Estacionamiento Exitoso", f"Auto {modelo} con placa {placa} estacionado en [{columna}, {fila}]")
            self.register_client()  # Procede al siguiente paso
        else:
            messagebox.showwarning(
                "Acceso Denegado", "No se pudo estacionar el auto. Revise las restricciones y espacios disponibles.")

    # Interacción 2
    def register_client(self):
        """ Handles client registration and moves to ficha exchange """
        for widget in self.frame_main.winfo_children():
            widget.destroy()

        Label(self.frame_main, text="Registro de Cliente", font=(
            "Arial", 14, "bold"), bg="white").pack(pady=10)

        criterios = ["Nombre", "Edad", "Saldo",
                     "Cantidad a Convertir en Fichas"]
        valores = ["", "", "", ""]
        habilitados = [True, True, True, True]

        self.field_registro = FieldFrame(
            self.frame_main, "Criterio", criterios, "Valor", valores, habilitados)
        self.field_registro.pack(pady=10)

        self.label_feedback = Label(
            self.frame_main, text="", font=("Arial", 12), bg="white")
        self.label_feedback.pack(pady=5)

        Button(self.frame_main, text="Registrar y Convertir Fichas",
               command=self.process_registration).pack(pady=5)

    def process_registration(self):
        """ Processes client registration and moves to welcome drink, with exception handling """
        nombre = self.field_registro.obtener_valor_por_criterio("Nombre")
        edad = self.field_registro.obtener_valor_por_criterio("Edad")
        saldo = self.field_registro.obtener_valor_por_criterio("Saldo")
        fichas = self.field_registro.obtener_valor_por_criterio(
            "Cantidad a Convertir en Fichas")

        if not nombre or not edad or not saldo or not fichas:
            messagebox.showerror("Error", "Complete todos los campos.")
            return

        # Se intenta convertir edad, saldo y fichas a números
        try:
            edad_int = int(edad)
            saldo_float = float(saldo)
            fichas_int = int(fichas)
        except ValueError:
            messagebox.showerror(
                "Error", "Edad, Saldo y Cantidad a Convertir deben ser números válidos.")
            return

        if fichas_int > saldo_float or fichas_int < 0:
            messagebox.showerror("Error", "Cantidad de dinero no válida.")
            return

        fichasn = fichas_int // 1000
        cambio = fichas_int % 1000

        if self.usuarioActual is None:
            self.usuarioActual = self.recepcionista.registrar_cliente(
                edad_int,
                saldo_float,
                self.field_identificacion.obtener_valor_por_criterio(
                    "ID Cliente"),
                nombre,
                self.parked_car
            )

        if self.usuarioActual:
            messagebox.showinfo(
                "Registro Exitoso", f"{nombre}, has sido registrado. Has cambiado {fichas_int} pesos por {fichasn} fichas. Te sobraron {cambio} pesos")

        self.recepcionista.cambiar_fichas(self.usuarioActual, fichas_int)

        self.give_welcome_drink()

    # Interacción 3
    def give_welcome_drink(self):
        """ Handles the third interaction: Assigning the welcome drink """
        for widget in self.frame_main.winfo_children():
            widget.destroy()

        Label(self.frame_main, text="Recepción - Bebida de Bienvenida",
              font=("Arial", 14, "bold"), bg="white").pack(pady=10)

        # Verifica que haya un cliente registrado
        if not self.usuarioActual:
            messagebox.showerror(
                "Error", "No hay cliente registrado. Complete los pasos anteriores.")
            return

        self.welcome_drink = self.bartender.preparar_bebida_bienvenida(
            self.usuarioActual)

        # Muestra la descripción de la bebida
        bebida_info = str(self.welcome_drink)
        self.label_drink_info = Label(self.frame_main, text=bebida_info, font=(
            "Arial", 12), bg="white", justify="left")
        self.label_drink_info.pack(pady=10)

        # Solicita la calificación usando FieldFrame
        criterios = ["Calificación (1 = Excelente, 2 = Normal, 3 = Mala)"]
        valores = [""]
        habilitados = [True]

        self.field_feedback = FieldFrame(
            self.frame_main, "Criterio", criterios, "Valor", valores, habilitados)
        self.field_feedback.pack(pady=10)

        # Botón para enviar la calificación
        Button(self.frame_main, text="Enviar Calificación",
               command=self.process_drink_feedback).pack(pady=10)

    def process_drink_feedback(self):
        """ Processes the rating given to the welcome drink and updates its popularity """
        rating = self.field_feedback.obtener_valor_por_criterio(
            "Calificación (1 = Excelente, 2 = Normal, 3 = Mala)")

        if not rating.isdigit() or int(rating) not in [1, 2, 3]:
            messagebox.showerror(
                "Error", "Ingrese una calificación válida (1, 2 o 3).")
            return

        rating = int(rating)

        # Ajusta el atributo 'favorito' según la calificación
        if rating == 1:
            self.welcome_drink.set_favorito(
                self.welcome_drink.get_favorito() + 1)
        elif rating == 3:
            self.welcome_drink.set_favorito(
                self.welcome_drink.get_favorito() - 1)

        messagebox.showinfo("Calificación Guardada",
                            "Gracias por su opinión. Disfrute su estadía en el casino.")

        # Finaliza el proceso de recepción
        self.finalize_reception()

    def finalize_reception(self):
        """ Marks the reception process as completed and unlocks functionalities """
        self.recepcion_completed = True
        messagebox.showinfo(
            "Recepción Completa", "Recepción finalizada. Ahora puedes acceder a todas las funcionalidades.")
        self.show_welcome_screen()

    # 🔹 FUNCIONALIDAD 2: JUEGOS
    def func_juegos(self):
        """ Handles Juegos functionality with restricted text boxes until Recepción is completed """
        for widget in self.frame_main.winfo_children():
            widget.destroy()

        criterios = ["Código", "Nombre", "Descripción"]
        valores = ["", "", ""]
        # Código nunca editable, lo demás depende de la Recepción
        habilitados = [False, self.recepcion_completed,
                       self.recepcion_completed]

        self.field_frame = FieldFrame(
            self.frame_main, "Criterio", criterios, "Valor", valores, habilitados)
        self.field_frame.pack(pady=20)

        Label(self.frame_main, text="Funcionalidad: Juegos",
              font=("Arial", 14, "bold"), bg="white").pack(pady=10)

    # 🔹 FUNCIONALIDAD 3: BAR
    def func_bar(self):
        """ Handles Bar functionality with restricted text boxes """
        for widget in self.frame_main.winfo_children():
            widget.destroy()

        criterios = ["Código", "Nombre", "Ubicación"]
        valores = ["", "", ""]
        habilitados = [False, self.recepcion_completed,
                       self.recepcion_completed]

        self.field_frame = FieldFrame(
            self.frame_main, "Criterio", criterios, "Valor", valores, habilitados)
        self.field_frame.pack(pady=20)

        Label(self.frame_main, text="Funcionalidad: Bar", font=(
            "Arial", 14, "bold"), bg="white").pack(pady=10)

    # 🔹 FUNCIONALIDAD 4: HOTEL
    def func_hotel(self):
        """ Handles Hotel functionality with restricted text boxes """
        for widget in self.frame_main.winfo_children():
            widget.destroy()

        criterios = ["Código", "Tipo de Habitación", "Capacidad"]
        valores = ["", "", ""]
        habilitados = [False, self.recepcion_completed,
                       self.recepcion_completed]

        self.field_frame = FieldFrame(
            self.frame_main, "Criterio", criterios, "Valor", valores, habilitados)
        self.field_frame.pack(pady=20)

        Label(self.frame_main, text="Funcionalidad: Hotel", font=(
            "Arial", 14, "bold"), bg="white").pack(pady=10)

    # 🔹 FUNCIONALIDAD 5: EVENTOS
    def func_eventos(self):
        """ Handles Eventos functionality with restricted text boxes """
        for widget in self.frame_main.winfo_children():
            widget.destroy()

        criterios = ["Código", "Nombre", "Fecha"]
        valores = ["", "", ""]
        habilitados = [False, self.recepcion_completed,
                       self.recepcion_completed]

        self.field_frame = FieldFrame(
            self.frame_main, "Criterio", criterios, "Valor", valores, habilitados)
        self.field_frame.pack(pady=20)

        Label(self.frame_main, text="Funcionalidad: Eventos",
              font=("Arial", 14, "bold"), bg="white").pack(pady=10)

    def show_app_info(self):
        """ Displays application information """
        messagebox.showinfo(
            "Información", "Este es un sistema de casino desarrollado para administrar información.")

    def show_authors(self):
        """ Displays application authors """
        messagebox.showinfo(
            "Acerca de", "Desarrollado por Angie, Emanuel, Juan Diego y Juan José.")

    def return_to_inicio(self):
        """ Closes this window and reopens Ventana_Inicio """
        self.root.destroy()
        root = tk.Tk()
        ventana_inicio.Ventana_Inicio(root)
        root.mainloop()

    def inicializar_obj_bar(self):
        barra_ingredientes = [
            Ingrediente("hojas de menta"), Ingrediente(
                "zumo de limón"), Ingrediente("jarabe de azúcar"),
            Ingrediente("ron blanco"), Ingrediente(
                "coco rallado"), Ingrediente("whisky"),
            Ingrediente("hielo"), Ingrediente(
                "zumo de piña"), Ingrediente("malta"),
            Ingrediente("vermut"), Ingrediente("ginebra")
        ]

        barra_bebidas = [
            Bebida("Mojito", 8000, True, False, False,
                   False, 2, barra_ingredientes[:5]),
            Bebida("Piña Colada", 9000, True, True, False, True, 3, [
                   barra_ingredientes[4], barra_ingredientes[7], barra_ingredientes[3], barra_ingredientes[6]]),
            Bebida("Whisky Sour", 10000, True, False, True, True, 4, [
                   barra_ingredientes[5], barra_ingredientes[1], barra_ingredientes[2], barra_ingredientes[6]]),
            Bebida("Cerveza Artesanal", 6000, False, False,
                   False, True, 1, [barra_ingredientes[8]]),
            Bebida("Martini", 12000, False, False, True, True, 5, [
                   barra_ingredientes[10], barra_ingredientes[9], barra_ingredientes[6]])
        ]

        self.bartender = Bartender("Bartender", "Barra")
        Bartender.set_barra_de_bebidas(barra_bebidas)
        Bartender.set_barra_de_ingredientes(barra_ingredientes)

    def inicializar_clientes(self):
        """ Inicializa clientes de prueba en el sistema """
        Cliente("James", 18, 45, 1000000, None,
                Suscripcion(6))  # Cliente Platinum
        Cliente("Samanta", 18, 37, 1000000, None, Suscripcion(4)).set_fidelidad_bar(
            True)  # Cliente Silver con fidelidad al bar
        Cliente("Jose", 18, 29, 1000000, None,
                Suscripcion(2))  # Cliente por defecto


if __name__ == "__main__":
    root = tk.Tk()
    app = Ventana_Principal(root)
    root.mainloop()
