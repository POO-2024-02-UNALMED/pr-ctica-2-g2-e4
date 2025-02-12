import tkinter as tk
from tkinter import Menu, Label, Button, Frame
#from PIL import Image, ImageTk  # For handling images

class CasinoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Casino - Ventana de Inicio")
        self.root.geometry("800x600")
        
        # Menu
        menu_bar = Menu(root)
        inicio_menu = Menu(menu_bar, tearoff=0)
        inicio_menu.add_command(label="Salir", command=root.quit)
        inicio_menu.add_command(label="Descripción del sistema", command=self.show_description)
        menu_bar.add_cascade(label="Inicio", menu=inicio_menu)
        root.config(menu=menu_bar)
        
        # Main Frames (P1 and P2 as main containers)
        self.frame_p1 = Frame(root, bg="lightblue")
        self.frame_p1.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        
        self.frame_p2 = Frame(root, bg="lightgray")
        self.frame_p2.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
        
        # Subframes inside P1 (P3 and P4)
        self.frame_p3 = Frame(self.frame_p1, height=100, bg="blue")
        self.frame_p3.pack(fill=tk.X)
        
        self.frame_p4 = Frame(self.frame_p1, height=200, bg="white")
        self.frame_p4.pack(expand=True, fill=tk.BOTH)
        
        # Subframes inside P2 (P5 and P6)
        self.frame_p5 = Frame(self.frame_p2, height=100, bg="green")
        self.frame_p5.pack(fill=tk.X)
        
        self.frame_p6 = Frame(self.frame_p2, height=200, bg="gray")
        self.frame_p6.pack(expand=True, fill=tk.BOTH)
        
        # Welcome Label (P3)
        self.label_welcome = Label(self.frame_p3, text="Bienvenido al Casino", font=("Arial", 16), bg="blue", fg="white")
        self.label_welcome.pack(pady=10)
        
        # Developer Bio (P5)
        self.label_bio = Label(self.frame_p5, text="Biografía del Desarrollador", font=("Arial", 12), bg="green", relief=tk.SUNKEN)
        self.label_bio.pack(pady=10)
        
        # Developer Photos (P6) - Placeholder
        self.frame_photos = Frame(self.frame_p6, bg="gray")
        self.frame_photos.pack(expand=True, fill=tk.BOTH)
        
        # Button to enter the main window (P4)
        self.btn_enter = Button(self.frame_p4, text="Entrar al Casino", font=("Arial", 12), command=self.open_main_window)
        self.btn_enter.pack(pady=20)
        
    def show_description(self):
        # Description of the system
        description_window = tk.Toplevel(self.root)
        description_window.title("Descripción del sistema")
        description_label = Label(description_window, text="Este sistema permite administrar un casino con varias funcionalidades.", wraplength=400, padx=20, pady=20)
        description_label.pack()
        
    def open_main_window(self):
        # Placeholder for opening the main casino window
        print("Opening main window...")

if __name__ == "__main__":
    root = tk.Tk()
    app = CasinoApp(root)
    root.mainloop()
