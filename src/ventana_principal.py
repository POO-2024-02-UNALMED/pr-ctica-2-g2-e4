import tkinter as tk
import ventana_inicio #NO es un error, funciona correctamente

class Ventana_Principal:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana Principal del Casino")
        self.root.geometry("800x600")

        # Menu
        menu_bar = tk.Menu(root)
        options_menu = tk.Menu(menu_bar, tearoff=0)
        options_menu.add_command(label="Volver a Inicio", command=self.return_to_inicio)
        options_menu.add_command(label="Salir", command=root.quit)
        menu_bar.add_cascade(label="Opciones", menu=options_menu)
        root.config(menu=menu_bar)

        # Welcome Label
        tk.Label(root, text="Bienvenido a la Ventana Principal del Casino", font=("Arial", 16)).pack(pady=20)

    def return_to_inicio(self):
        """Closes this window and reopens Ventana_Inicio"""
        self.root.destroy()  # Close Ventana_Principal
        root = tk.Tk()  # Create a new root window
        ventana_inicio.Ventana_Inicio(root)  # Open Ventana_Inicio
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = Ventana_Principal(root)
    root.mainloop()
