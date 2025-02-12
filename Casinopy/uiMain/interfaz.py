import tkinter as tk
from tkinter import Menu, Label, Button, Frame
#from PIL import Image, ImageTk  # For handling images

class CasinoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Casino - Ventana de Inicio")
        self.root.geometry("800x600")
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        
        # Menu
        menu_bar = Menu(root)
        inicio_menu = Menu(menu_bar, tearoff=0)
        inicio_menu.add_command(label="Salir", command=root.quit)
        inicio_menu.add_command(label="Descripción del sistema", command=self.show_description)
        menu_bar.add_cascade(label="Inicio", menu=inicio_menu)
        root.config(menu=menu_bar)
        
        # Main Frames (P1 and P2 as main containers)
        self.frame_p1 = Frame(root, bg="lightblue", width=400)
        self.frame_p1.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
        
        self.frame_p2 = Frame(root, bg="lightgray", width=400)
        self.frame_p2.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')
        
        # Subframes inside P1 (P3 and P4)
        self.frame_p3 = Frame(self.frame_p1, height=int(self.root.winfo_height()*0.5), bg="blue")
        self.frame_p3.pack(expand=True, fill=tk.BOTH)
        
        self.frame_p4 = Frame(self.frame_p1, height=int(self.root.winfo_height()*0.5), bg="white")
        self.frame_p4.pack(expand=True, fill=tk.BOTH)
        
        # Subframes inside P2 (P5 and P6)
        self.frame_p5 = Frame(self.frame_p2, height=int(self.root.winfo_height()*0.5), bg="green")
        self.frame_p5.pack(expand=True, fill=tk.BOTH)
        
        self.frame_p6 = Frame(self.frame_p2, height=int(self.root.winfo_height()*0.5), bg="gray")
        self.frame_p6.pack(expand=True, fill=tk.BOTH)
        
        # Welcome Label (P3)
        self.label_welcome = Label(self.frame_p3, text="Bienvenido al Casino Diamond, \n disfrute su estadia", bg="blue", fg="white")
        self.label_welcome.pack(pady=5, expand=True)
        
        # Developer Bio (P5)
        self.label_bio = Label(self.frame_p5, text="Biografía del Desarrollador", bg="green")
        self.label_bio.pack(pady=5, anchor='center')
        
        # Developer Photos (P6) - Placeholder
        self.frame_photos = Frame(self.frame_p6, bg="gray")
        self.frame_photos.pack(expand=True, fill=tk.BOTH)
        
        # Button to enter the main window (P4)
        self.btn_enter = Button(self.frame_p4, text="Entrar al Casino", command=self.open_main_window)
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
