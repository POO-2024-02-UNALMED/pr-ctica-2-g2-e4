import tkinter as tk
from tkinter import Menu, Frame, Label, Button, messagebox, Label, Entry, StringVar, OptionMenu
import random 
from fieldFrame import FieldFrame  # Importing FieldFrame for structured forms
import ventana_inicio  # Importing Ventana_Inicio to allow navigation
from gestorAplicacion.personal.cliente import Cliente
from gestorAplicacion.personal.recepcionista import Recepcionista
from gestorAplicacion.personal.bartender import Bartender
from gestorAplicacion.personal.valet import Valet

from gestorAplicacion.Servicios.bebida import Bebida
from gestorAplicacion.Servicios.ingrediente import Ingrediente

from gestorAplicacion.Servicios.auto import Auto
from gestorAplicacion.Servicios.casino import Casino

from gestorAplicacion.Servicios import evento, asiento
from gestorAplicacion.Servicios.evento import Evento

class Ventana_Principal:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Casino")
        self.root.geometry("1000x600")

        # 🔹 ZONE 0: Application Title
        self.title_label = Label(root, text="Sistema de Casino", font=("Arial", 16, "bold"), bg="gray", fg="white")
        self.title_label.pack(fill="x")

        # 🔹 ZONE 1: Menu Bar
        menu_bar = Menu(root)

        archivo_menu = Menu(menu_bar, tearoff=0)
        archivo_menu.add_command(label="Aplicación", command=self.show_app_info)
        archivo_menu.add_command(label="Salir", command=self.return_to_inicio)
        menu_bar.add_cascade(label="Archivo", menu=archivo_menu)

        procesos_menu = Menu(menu_bar, tearoff=0)
        procesos_menu.add_command(label="Recepción", command=self.func_recepcion)
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

        #inicializacion de objetos
        self.inicializar_obj_bar()
        self.usuarioActual = None

    def show_welcome_screen(self):
        """ Displays the welcome message on startup """
        for widget in self.frame_main.winfo_children():
            widget.destroy()

        Label(self.frame_main, text="Administrador Sistema de Casino", font=("Arial", 16, "bold"), bg="white").pack(pady=10)
        Label(self.frame_main, text="Consulta y administra información sobre el casino y sus funcionalidades.", font=("Arial", 12), bg="white").pack(pady=5)

    # 🔹 FUNCIONALIDAD 1: RECEPCIÓN
    #interaccion 1
    def func_recepcion(self):
        """ Handles Recepción functionality (Step 1: Client Identification & Parking) """
        for widget in self.frame_main.winfo_children():
            widget.destroy()

        Label(self.frame_main, text="Recepción - Identificación y Estacionamiento", font=("Arial", 14, "bold"), bg="white").pack(pady=10)

        # 🔹 Step 1: Client ID, Car Model, and Plate
        criterios = ["ID Cliente", "Modelo Auto", "Placa Auto"]
        valores = ["", "", ""]
        habilitados = [True, True, True]  # All fields editable

        self.field_identificacion = FieldFrame(self.frame_main, "Criterio", criterios, "Valor", valores, habilitados)
        self.field_identificacion.pack(pady=10)

        # Label to display parking lot visualization (added above the next input fields)
        self.label_parking_display = Label(self.frame_main, text="", font=("Courier", 12), bg="white", justify="left")
        self.label_parking_display.pack(pady=5)

        self.label_feedback = Label(self.frame_main, text="", font=("Arial", 12), bg="white")
        self.label_feedback.pack(pady=5)

        Button(self.frame_main, text="Verificar ID y Mostrar Estacionamiento", command=self.verify_id_and_show_parking).pack(pady=5)

        # Initializing objects
        self.valet = Valet("Valet", "Estacionamiento")
        self.recepcionista = Recepcionista("Recepcionista", "Recepción")
        self.bartender = Bartender("Bartender", "Barra")
        self.usuarioOld = None
        self.parked_car = None

    def verify_id_and_show_parking(self):
        """ Checks ID, registers a new user if necessary, and displays the parking lot """
        id_cliente = self.field_identificacion.obtener_valor_por_criterio("ID Cliente")
        modelo = self.field_identificacion.obtener_valor_por_criterio("Modelo Auto")
        placa = self.field_identificacion.obtener_valor_por_criterio("Placa Auto")

        if not id_cliente or not modelo or not placa:
            messagebox.showerror("Error", "Ingrese un ID, modelo de auto y placa válidos.")
            return

        self.usuarioOld = self.valet.identificar_cliente(id_cliente)

        if self.usuarioOld:
            self.label_feedback.config(text=f"Hola {self.usuarioOld.get_nombre_cliente()}! Bienvenido al casino.")
            suscripcion_cliente = self.usuarioOld.get_suscripcion()
        else:
            self.label_feedback.config(text="No hay registros. Continuando con nuevo registro...")
            suscripcion_cliente = None

        # 🔹 Step 2: Initialize and Show Parking Lot
        Casino.inicializar_estacionamiento(5, 5)  # Initializes a 5x5 parking lot
        estacionamiento_str = Casino.mostrar_espacios_estacionamiento(suscripcion_cliente)

        # 🔹 Update the GUI with the parking lot visualization
        self.label_parking_display.config(text=estacionamiento_str)

        # Move to next step: Ask for parking position
        self.ask_parking_position()

    def ask_parking_position(self):
        """ Displays fields for selecting a parking space """
        # Clear previous widgets (except parking display)
        for widget in self.frame_main.winfo_children():
            if widget not in [self.label_parking_display, self.label_feedback]:
                widget.destroy()

        Label(self.frame_main, text="Seleccione la ubicación de estacionamiento", font=("Arial", 14, "bold"), bg="white").pack(pady=10)

        criterios = ["Columna Estacionamiento", "Fila Estacionamiento"]
        valores = ["", ""]
        habilitados = [True, True]

        self.field_parking = FieldFrame(self.frame_main, "Criterio", criterios, "Valor", valores, habilitados)
        self.field_parking.pack(pady=10)

        Button(self.frame_main, text="Estacionar Auto", command=self.park_car).pack(pady=5)

    def park_car(self):
        """ Registers the car in the selected parking spot, but validation is now handled in Valet """
        columna = self.field_parking.obtener_valor_por_criterio("Columna Estacionamiento")
        fila = self.field_parking.obtener_valor_por_criterio("Fila Estacionamiento")

        if not columna or not fila:
            messagebox.showerror("Error", "Seleccione una columna y fila válidas para estacionar.")
            return

        id_cliente = self.field_identificacion.obtener_valor_por_criterio("ID Cliente")
        modelo = self.field_identificacion.obtener_valor_por_criterio("Modelo Auto")
        placa = self.field_identificacion.obtener_valor_por_criterio("Placa Auto")

        # Convert input values to integers
        columna, fila = int(columna), int(fila)

        # 🔹 Step 1: Call `estacionar_registrar_auto()`, which now handles all validation
        self.parked_car = self.valet.estacionar_registrar_auto(modelo, placa, columna, fila, id_cliente)

        if self.parked_car:
            messagebox.showinfo("Estacionamiento Exitoso", f"Auto {modelo} con placa {placa} estacionado en [{columna}, {fila}]")
            self.register_client()  # Proceed to the next step
        else:
            messagebox.showwarning("Acceso Denegado", "No se pudo estacionar el auto. Revise las restricciones y espacios disponibles.")




    #interaccion 2
    def register_client(self):
        """ Handles client registration and moves to ficha exchange """
        for widget in self.frame_main.winfo_children():
            widget.destroy()

        Label(self.frame_main, text="Registro de Cliente", font=("Arial", 14, "bold"), bg="white").pack(pady=10)

        criterios = ["Nombre", "Edad", "Saldo", "Cantidad a Convertir en Fichas"]
        valores = ["", "", "", ""]
        habilitados = [True, True, True, True]

        self.field_registro = FieldFrame(self.frame_main, "Criterio", criterios, "Valor", valores, habilitados)
        self.field_registro.pack(pady=10)

        self.label_feedback = Label(self.frame_main, text="", font=("Arial", 12), bg="white")
        self.label_feedback.pack(pady=5)

        Button(self.frame_main, text="Registrar y Convertir Fichas", command=self.process_registration).pack(pady=5)

    def process_registration(self):
        """ Processes client registration and moves to welcome drink """
        nombre = self.field_registro.obtener_valor_por_criterio("Nombre")
        edad = self.field_registro.obtener_valor_por_criterio("Edad")
        saldo = self.field_registro.obtener_valor_por_criterio("Saldo")
        fichas = self.field_registro.obtener_valor_por_criterio("Cantidad a Convertir en Fichas")
        fichasn = int(fichas) // 1000
        cambio = int(fichas) % 1000

        if not nombre or not edad or not saldo or not fichas:
            messagebox.showerror("Error", "Complete todos los campos.")
            return
        
        if int(fichas)> int(saldo) or int(fichas) < 0:
            messagebox.showerror("Error", "Cantidad de dinero no válida.")
            return

        edad, saldo, fichas = int(edad), float(saldo), float(fichas)

        if self.usuarioActual is None:
            self.usuarioActual = self.recepcionista.registrar_cliente(edad, saldo, self.field_identificacion.obtener_valor_por_criterio("ID Cliente"), nombre, self.parked_car)

        if self.usuarioActual:
            messagebox.showinfo("Registro Exitoso", f"{nombre}, has sido registrado. Has cambiado {fichas} pesos por {fichasn} fichas. Te sobraron {cambio} pesos")

        self.recepcionista.cambiar_fichas(self.usuarioActual, fichas)
        
        self.give_welcome_drink()

    # interaccion 3
    def give_welcome_drink(self):
        """ Assigns a welcome drink and completes registration """
        for widget in self.frame_main.winfo_children():
            widget.destroy()

        Label(self.frame_main, text="Bebida de Bienvenida", font=("Arial", 14, "bold"), bg="white").pack(pady=10)

        criterios = ["Bebida"]
        valores = [""]
        habilitados = [False]

        self.field_bebida = FieldFrame(self.frame_main, "Criterio", criterios, "Valor", valores, habilitados)
        self.field_bebida.pack(pady=10)

        self.label_feedback = Label(self.frame_main, text="", font=("Arial", 12), bg="white")
        self.label_feedback.pack(pady=5)

        Button(self.frame_main, text="Recibir Bebida y Completar", command=self.complete_reception).pack(pady=5)



    def complete_reception(self):
        """ Completes reception and enables functionalities """
        welcome_drinks = ["Mojito", "Piña Colada", "Martini", "Whisky Sour"]
        drink = random.choice(welcome_drinks)

        self.field_bebida.entries[0].config(state="normal")
        self.field_bebida.valores_vars[0].set(drink)
        self.field_bebida.entries[0].config(state="readonly")

        messagebox.showinfo("Recepción Completa", f"Has recibido una {drink} de bienvenida. ¡Disfruta el casino!")

        self.recepcion_completed = True  # Unlocks functionalities

    # 🔹 FUNCIONALIDAD 2: JUEGOS
    def func_juegos(self):
        """ Handles Juegos functionality with restricted text boxes until Recepción is completed """
        for widget in self.frame_main.winfo_children():
            widget.destroy()

        criterios = ["Código", "Nombre", "Descripción"]
        valores = ["", "", ""]
        habilitados = [False, self.recepcion_completed, self.recepcion_completed]  # Código never editable, rest depends on Recepción

        self.field_frame = FieldFrame(self.frame_main, "Criterio", criterios, "Valor", valores, habilitados)
        self.field_frame.pack(pady=20)

        Label(self.frame_main, text="Funcionalidad: Juegos", font=("Arial", 14, "bold"), bg="white").pack(pady=10)

    # 🔹 FUNCIONALIDAD 3: BAR
    def func_bar(self):
        """ Handles Bar functionality with restricted text boxes """
        for widget in self.frame_main.winfo_children():
            widget.destroy()

        criterios = ["Código", "Nombre", "Ubicación"]
        valores = ["", "", ""]
        habilitados = [False, self.recepcion_completed, self.recepcion_completed]  

        self.field_frame = FieldFrame(self.frame_main, "Criterio", criterios, "Valor", valores, habilitados)
        self.field_frame.pack(pady=20)

        Label(self.frame_main, text="Funcionalidad: Bar", font=("Arial", 14, "bold"), bg="white").pack(pady=10)

    # 🔹 FUNCIONALIDAD 4: HOTEL
    def func_hotel(self):
        """ Handles Hotel functionality with restricted text boxes """
        for widget in self.frame_main.winfo_children():
            widget.destroy()

        criterios = ["Código", "Tipo de Habitación", "Capacidad"]
        valores = ["", "", ""]
        habilitados = [False, self.recepcion_completed, self.recepcion_completed]  

        self.field_frame = FieldFrame(self.frame_main, "Criterio", criterios, "Valor", valores, habilitados)
        self.field_frame.pack(pady=20)

        Label(self.frame_main, text="Funcionalidad: Hotel", font=("Arial", 14, "bold"), bg="white").pack(pady=10)








    # 🔹 FUNCIONALIDAD 5: EVENTOS
    def func_eventos(self):
        """Muestra la interfaz para gestionar eventos en el casino."""
        for widget in self.frame_main.winfo_children():
            widget.destroy()

        Label(self.frame_main, text="Ingrese su ID de cliente:", font=("Arial", 12), bg="white").pack(pady=5)

        self.entry_id = Entry(self.frame_main)
        self.entry_id.pack(pady=5)

        Button(self.frame_main, text="Confirmar ID", command=self.verificar_cliente).pack(pady=5)

    def verificar_cliente(self):
        """Verifica si el cliente existe y muestra los eventos."""
        id_cliente = self.entry_id.get()
        self.cliente = Recepcionista.identificar_cliente(id_cliente)

        if not self.cliente:
            messagebox.showerror("Error", "No se encontró ningún registro para esta identificación.")
            return
        
        # Limpiar pantalla
        for widget in self.frame_main.winfo_children():
            widget.destroy()
        
        # Información del cliente
        Label(self.frame_main, text=f"Hola {self.cliente.get_nombre_cliente()}!", font=("Arial", 14, "bold"), bg="white").pack(pady=5)
        Label(self.frame_main, text=f"Suscripción: {self.cliente.get_suscripcion().get_tipo_suscripcion()}", font=("Arial", 12), bg="white").pack()
        Label(self.frame_main, text=f"Saldo: {self.cliente.get_fichas()} fichas", font=("Arial", 12), bg="white").pack()

        # Inicializar eventos
        Evento.inicializar_eventos()
        self.eventos_disponibles = Evento.mostrar_eventos()  # Lista de objetos Evento

        # Crear un Frame con fondo gris para organizar la selección
        frame_seleccion = tk.Frame(self.frame_main, bg="#d3d3d3", padx=10, pady=10)
        frame_seleccion.pack(pady=10)

        # Encabezados
        Label(frame_seleccion, text="Criterio", font=("Arial", 10, "bold"), bg="#a0a0a0", width=15).grid(row=0, column=0, padx=5, pady=5)
        Label(frame_seleccion, text="Valor", font=("Arial", 10, "bold"), bg="#a0a0a0", width=20).grid(row=0, column=1, padx=5, pady=5)

        # Selección de Evento
        Label(frame_seleccion, text="Seleccione un evento:", font=("Arial", 10), bg="#d3d3d3").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.evento_var = StringVar()
        self.evento_var.set(self.eventos_disponibles[0].nombre)
        OptionMenu(frame_seleccion, self.evento_var, *[e.nombre for e in self.eventos_disponibles]).grid(row=1, column=1, padx=5, pady=5)

        # Botón para confirmar evento y pasar a selección de asiento
        Button(frame_seleccion, text="Seleccionar Evento", command=self.seleccionar_evento).grid(row=2, column=1, pady=10, sticky="e")

    def seleccionar_evento(self):
        """Muestra el precio con descuento y permite seleccionar asiento."""
        nombre_evento = self.evento_var.get()
        self.evento_seleccionado = next(e for e in self.eventos_disponibles if e.nombre == nombre_evento)

        descuento = self.cliente.get_suscripcion().get_descuento()
        costo_original = self.evento_seleccionado.get_precio()
        self.costo_final = int(costo_original * (1 - descuento))

        for widget in self.frame_main.winfo_children():
            widget.destroy()
        
        frame_seleccion = tk.Frame(self.frame_main, bg="#d3d3d3", padx=10, pady=10)
        frame_seleccion.pack(pady=10)

        # Encabezados
        Label(frame_seleccion, text="Criterio", font=("Arial", 10, "bold"), bg="#a0a0a0", width=15).grid(row=0, column=0, padx=5, pady=5)
        Label(frame_seleccion, text="Valor", font=("Arial", 10, "bold"), bg="#a0a0a0", width=20).grid(row=0, column=1, padx=5, pady=5)

        # Evento Seleccionado
        Label(frame_seleccion, text="Evento:", font=("Arial", 10), bg="#d3d3d3").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        Label(frame_seleccion, text=self.evento_seleccionado.get_nombre(), font=("Arial", 10), bg="#d3d3d3").grid(row=1, column=1, padx=5, pady=5)

        # Precio con Descuento
        Label(frame_seleccion, text="Precio con descuento:", font=("Arial", 10), bg="#d3d3d3").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        Label(frame_seleccion, text=f"{self.costo_final} fichas", font=("Arial", 10, "bold"), bg="#d3d3d3").grid(row=2, column=1, padx=5, pady=5)

        # Selección de Asiento
        zonas = {"PALCO": asiento.ZonaAsiento.PALCO, "BALCÓN": asiento.ZonaAsiento.BALCON,
                "CENTRO": asiento.ZonaAsiento.CENTRO, "ATRÁS": asiento.ZonaAsiento.ATRAS}

        Label(frame_seleccion, text="Zona de Asiento:", font=("Arial", 10), bg="#d3d3d3").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.asiento_var = StringVar()
        self.asiento_var.set("CENTRO")
        OptionMenu(frame_seleccion, self.asiento_var, *zonas.keys()).grid(row=3, column=1, padx=5, pady=5)

        # Crear label para el resumen de la reserva
        self.label_resumen = Label(frame_seleccion, text="", justify="left", font=("Arial", 10), bg="#d3d3d3")
        self.label_resumen.grid(row=5, column=0, columnspan=2, pady=10)

        # Confirmar Compra y Asiento
        Button(frame_seleccion, text="Confirmar Reserva", command=lambda: self.confirmar_asiento(zonas)).grid(row=4, column=1, pady=10, sticky="e")

    def confirmar_asiento(self, zonas):
        """Confirma la selección de asiento y finaliza la reserva."""
        self.zona_seleccionada = zonas[self.asiento_var.get()]

        if self.cliente.get_fichas() < self.costo_final:
            messagebox.showerror("Error", "No tiene suficientes fichas para este evento.")
            return

        self.cliente.set_fichas(self.cliente.get_fichas() - self.costo_final)
        
        # Ahora pasamos `self.label_resumen` correctamente
        Recepcionista.procesar_seleccion_evento(
            self.cliente, 
            self.evento_seleccionado, 
            self.zona_seleccionada, 
            self.costo_final, 
            self.label_resumen  
        )

        messagebox.showinfo("Reserva Confirmada", f"Asiento en {self.asiento_var.get()} confirmado para {self.evento_seleccionado.get_nombre()}!\nNuevo saldo: {self.cliente.get_fichas()} fichas")













    def show_app_info(self):
        """ Displays application information """
        messagebox.showinfo("Información", "Este es un sistema de casino desarrollado para administrar información.")

    def show_authors(self):
        """ Displays application authors """
        messagebox.showinfo("Acerca de", "Desarrollado por Angie, Emanuel, Juan Diego y Juan José.")

    def return_to_inicio(self):
        """ Closes this window and reopens Ventana_Inicio """
        self.root.destroy()
        root = tk.Tk()
        ventana_inicio.Ventana_Inicio(root)
        root.mainloop()

    def inicializar_obj_bar(self):
        barra_ingredientes = [
            Ingrediente("hojas de menta"), Ingrediente("zumo de limón"), Ingrediente("jarabe de azúcar"),
            Ingrediente("ron blanco"), Ingrediente("coco rallado"), Ingrediente("whisky"),
            Ingrediente("hielo"), Ingrediente("zumo de piña"), Ingrediente("malta"),
            Ingrediente("vermut"), Ingrediente("ginebra")
        ]
    
        barra_bebidas = [
            Bebida("Mojito", 8000, True, False, False, False, 2, barra_ingredientes[:5]),
            Bebida("Piña Colada", 9000, True, True, False, True, 3, [barra_ingredientes[4], barra_ingredientes[7], barra_ingredientes[3], barra_ingredientes[6]]),
            Bebida("Whisky Sour", 10000, True, False, True, True, 4, [barra_ingredientes[5], barra_ingredientes[1], barra_ingredientes[2], barra_ingredientes[6]]),
            Bebida("Cerveza Artesanal", 6000, False, False, False, True, 1, [barra_ingredientes[8]]),
            Bebida("Martini", 12000, False, False, True, True, 5, [barra_ingredientes[10], barra_ingredientes[9], barra_ingredientes[6]])
        ]
    
        bartender = Bartender("Bartender", "Barra")
        Bartender.set_barra_de_bebidas(barra_bebidas)
        Bartender.set_barra_de_ingredientes(barra_ingredientes)

if __name__ == "__main__":
    root = tk.Tk()
    app = Ventana_Principal(root)
    root.mainloop()
