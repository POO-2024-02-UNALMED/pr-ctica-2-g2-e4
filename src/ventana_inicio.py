import os
import tkinter as tk
from tkinter import Menu, Label, Button, Frame, Toplevel
from PIL import Image, ImageTk
import ventana_principal #NO es un error, funciona correctamente

class Ventana_Inicio:
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

        # Main Frames
        self.frame_p1 = Frame(root, bg="lightblue", width=400)
        self.frame_p1.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

        self.frame_p2 = Frame(root, bg="lightgray", width=400)
        self.frame_p2.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

        # Subframes in P1
        self.frame_p3 = Frame(self.frame_p1, bg="blue")
        self.frame_p3.pack(expand=True, fill=tk.BOTH)

        self.frame_p4 = Frame(self.frame_p1, bg="white")
        self.frame_p4.pack(expand=True, fill=tk.BOTH)

        # Subframes in P2
        self.frame_p5 = Frame(self.frame_p2, bg="green")
        self.frame_p5.pack(expand=True, fill=tk.BOTH)

        self.frame_p6 = Frame(self.frame_p2, bg="gray")
        self.frame_p6.pack(expand=True, fill=tk.BOTH)

        self.dev_photo_labels = [[Label(self.frame_p6, bg="gray") for _ in range(2)] for _ in range(2)]

        # Developer Photos (P6)
        
        for i in range(2):
            for j in range(2):
                self.dev_photo_labels[i][j].grid(row=i, column=j, padx=5, pady=5, sticky="nsew")
                self.frame_p6.grid_columnconfigure(j, weight=1)
                self.frame_p6.grid_rowconfigure(i, weight=1)

        # Welcome Label (P3)
        self.label_welcome = Label(self.frame_p3, text="Bienvenido al Casino", bg="blue", fg="white")
        self.label_welcome.pack(pady=10, expand=True)

        # Developer Bio (P5)
        self.developers = ["Angie Melissa Montoya", "Emanuel Palacio", "Juan Diego Cardenas", "Juan Jose Gómez"]
        self.dev_ages = [18, 18, 18, 18]
        self.dev_careers = ["Ingeniería de Sistemas", "Ciencias de la Computación", "Ingeniería de Sistemas", "Ingeniería de Sistemas"]
        self.current_dev_index = 0

        self.label_bio = Label(self.frame_p5, text="", bg="green", relief=tk.SUNKEN, wraplength=300)
        self.label_bio.pack(pady=10)
        self.label_bio.bind("<Button-1>", self.cycle_bio)
        self.update_bio()

        self.base_image_path = os.path.join(os.path.dirname(__file__), "images")

        # Imagenes de P4
        self.image_files = ["system1.png", "system2.png", "system3.png", "system4.png", "system5.png"]
        self.image_paths = [os.path.join(self.base_image_path, img) for img in self.image_files]
        self.current_image_index = 0

        # Label P4 imagen    
        self.image_label = tk.Label(self.frame_p4, bg="white")
        self.image_label.pack(expand=True, fill="both")
        self.cargar_imagen()
        self.image_label.bind("<Enter>", self.cambiar_imagen)

        

        # Button to enter the main window (P4)
        self.btn_enter = Button(self.frame_p4, text="Entrar al Casino", command=self.open_main_window)
        self.btn_enter.pack(pady=20)

        # Ensure proper height after Tkinter initializes
        self.root.after(100, self.adjust_frames)


    """ def cargar_foto_desarrollador(self, img_name):
        img_path = os.path.join(self.base_image_path, img_name)
        if not os.path.exists(img_path):
            img_path = os.path.join(self.base_image_path, "default.png")
        img = Image.open(img_path).resize((150, 150))
        photo = ImageTk.PhotoImage(img)
        self.dev_image_label.config(image=photo)
        self.dev_image_label.image = photo """
    def adjust_frames(self):
        """Adjust subframe heights after root window initializes"""
        height = self.root.winfo_height()
        for frame in [self.frame_p3, self.frame_p4, self.frame_p5, self.frame_p6]:
            frame.config(height=height // 2)

    def update_bio(self):
        """Updates the bio text dynamically"""
        text = f"{self.developers[self.current_dev_index]}\nEdad: {self.dev_ages[self.current_dev_index]}\nCarrera: {self.dev_careers[self.current_dev_index]}"
        self.label_bio.config(text=text)
        self.load_dev_images()

    def cycle_bio(self, event=None):
        """Cycles developer information on click"""
        self.current_dev_index = (self.current_dev_index + 1) % len(self.developers)
        self.update_bio()

    def load_dev_images(self):
        """Loads and updates images in P6 dynamically"""
        dev_name = self.developers[self.current_dev_index].lower().replace(" ", "_")
        self.dev_photos = []  # Maintain reference list
        self.base_image_path = os.path.join(os.path.dirname(__file__), "images")
        for i in range(2):
            for j in range(2):
                img_path = os.path.join(self.base_image_path, f"{dev_name}_{i}{j}.png")

                if not os.path.exists(img_path):
                    img_path = os.path.join(self.base_image_path, "default.png")

                try:
                    img = Image.open(img_path).resize((100, 100))
                    photo = ImageTk.PhotoImage(img)
                    self.dev_photos.append(photo)  # Store reference to prevent GC
                    self.dev_photo_labels[i][j].config(image=photo)
                    self.dev_photo_labels[i][j].image = photo
                except Exception as e:
                    print(f"Error loading image {img_path}: {e}")

    def show_description(self):
        """Displays system description in a new window"""
        description_window = Toplevel(self.root)
        description_window.title("Descripción del Sistema")
        Label(description_window, text="Este sistema permite administrar un casino con varias funcionalidades.", wraplength=400, padx=20, pady=20).pack()

    def cargar_imagen(self):
        try:
            img_path = self.image_paths[self.current_image_index]
            print(img_path)
            img = Image.open(img_path)
            img = img.resize((200, 200))
            self.photo = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.photo)
            self.image_label.image = self.photo
        except Exception as e:
            print(f"Error cargando la imagen en P4: {e}")

    def cambiar_imagen(self, event=None):
        self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
        self.cargar_imagen()

    def open_main_window(self):
        """Closes the current window and opens Ventana_Principal"""
        self.root.destroy()  # Close Ventana_Inicio
        root = tk.Tk()  # Create new root
        ventana_principal.Ventana_Principal(root)  # Open Ventana_Principal
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = Ventana_Inicio(root)
    root.mainloop()