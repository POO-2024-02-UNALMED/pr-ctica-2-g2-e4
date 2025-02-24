import tkinter as tk
from tkinter import Menu, Frame, Label, Button, messagebox
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
    def func_recepcion(self):
        """ Handles Recepción functionality and unlocks the other functionalities """
        for widget in self.frame_main.winfo_children():
            widget.destroy()

        criterios = ["ID Cliente", "Nombre", "Apellido", "Habitación"]
        valores = ["", "", "", ""]
        habilitados = [True, True, True, True]  # All fields editable

        self.field_frame = FieldFrame(self.frame_main, "Criterio", criterios, "Valor", valores, habilitados)
        self.field_frame.pack(pady=20)

        Button(self.frame_main, text="Completar Recepción", command=self.complete_recepcion).pack(pady=10)

    def complete_recepcion(self):
        """ Marks Recepción as completed and unlocks the rest """
        self.recepcion_completed = True
        messagebox.showinfo("Recepción Completada", "Recepción ha sido completada. Ahora puedes acceder a las demás funcionalidades.")

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
        """ Handles Eventos functionality with restricted text boxes """
        for widget in self.frame_main.winfo_children():
            widget.destroy()

        criterios = ["Código", "Nombre", "Fecha"]
        valores = ["", "", ""]
        habilitados = [False, self.recepcion_completed, self.recepcion_completed]  

        self.field_frame = FieldFrame(self.frame_main, "Criterio", criterios, "Valor", valores, habilitados)
        self.field_frame.pack(pady=20)

        Label(self.frame_main, text="Funcionalidad: Eventos", font=("Arial", 14, "bold"), bg="white").pack(pady=10)

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
