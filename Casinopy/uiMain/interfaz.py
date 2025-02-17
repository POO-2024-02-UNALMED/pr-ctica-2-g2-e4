import tkinter as tk
from tkinter import Menu, Label, Button, Frame, Toplevel
from PIL import Image, ImageTk
import os

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

        # Developer Photos (P6)
        self.dev_photo_labels = [[Label(self.frame_p6, bg="gray") for _ in range(2)] for _ in range(2)]
        for i in range(2):
            for j in range(2):
                self.dev_photo_labels[i][j].grid(row=i, column=j, padx=5, pady=5, sticky="nsew")
                self.frame_p6.grid_columnconfigure(j, weight=1)
                self.frame_p6.grid_rowconfigure(i, weight=1)

        # Images in P4 (cycling on hover)
        self.p4_images = ["system1.png", "system2.png", "system3.png", "system4.png", "system5.png"]
        self.current_p4_image_index = 0
        self.p4_label = Label(self.frame_p4, bg="white")
        self.p4_label.pack(expand=True, fill=tk.BOTH)
        self.p4_label.bind("<Enter>", self.cycle_p4_image)
        self.p4_photo = None  # Store reference
        self.load_p4_image()

        # Button to enter the main window (P4)
        self.btn_enter = Button(self.frame_p4, text="Entrar al Casino", command=self.open_main_window)
        self.btn_enter.pack(pady=20)

        # Ensure proper height after Tkinter initializes
        self.root.after(100, self.adjust_frames)

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
        for i in range(2):
            for j in range(2):
                img_path = f"images/{dev_name}_{i}{j}.png"
                if os.path.exists(img_path):
                    img = Image.open(img_path).resize((100, 100))
                    photo = ImageTk.PhotoImage(img)
                    self.dev_photos.append(photo)  # Store reference
                    self.dev_photo_labels[i][j].config(image=photo)
                    self.dev_photo_labels[i][j].image = photo

    def show_description(self):
        """Displays system description in a new window"""
        description_window = Toplevel(self.root)
        description_window.title("Descripción del Sistema")
        Label(description_window, text="Este sistema permite administrar un casino con varias funcionalidades.", wraplength=400, padx=20, pady=20).pack()

    def cycle_p4_image(self, event=None):
        """Cycles images in P4 on hover"""
        self.current_p4_image_index = (self.current_p4_image_index + 1) % len(self.p4_images)
        self.load_p4_image()

    def load_p4_image(self):
        """Loads images dynamically for P4"""
        img_path = f"images/{self.p4_images[self.current_p4_image_index]}"
        if os.path.exists(img_path):
            img = Image.open(img_path).resize((150, 150))
            self.p4_photo = ImageTk.PhotoImage(img)  # Keep reference
            self.p4_label.config(image=self.p4_photo)
            self.p4_label.image = self.p4_photo

    def open_main_window(self):
        """Opens the main casino window without closing the current one"""
        new_window = Toplevel(self.root)
        new_window.title("Ventana Principal del Casino")
        Label(new_window, text="Bienvenido a la Ventana Principal del Casino", font=("Arial", 16)).pack(pady=20)
        new_window.geometry("800x600")

if __name__ == "__main__":
    root = tk.Tk()
    app = CasinoApp(root)
    root.mainloop()
