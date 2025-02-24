from tkinter import Frame, Label, Entry, Button, StringVar


class FieldFrame(Frame):
    def __init__(self, parent, titulo_criterios, criterios, titulo_valores, valores=None, habilitados=None, ancho_entry=20, on_get_values=None):
        """
        Custom frame widget for structured input fields.

        Parameters:
            parent (tk.Widget): Parent Tkinter widget.
            titulo_criterios (str): Title for the criteria column.
            criterios (list of str): List of criteria labels.
            titulo_valores (str): Title for the values column.
            valores (list of str, optional): Initial values for input fields.
            habilitados (list of bool, optional): Boolean list indicating which fields are enabled.
            ancho_entry (int): Width of the Entry fields.
            on_get_values (function, optional): Callback function to execute when clicking the "Get Values" button.
        """
        super().__init__(parent, bg="lightgray")

        # Store criteria, values, and input fields
        self.criterios = criterios
        self.valores_vars = []  # List of StringVar for each Entry field
        self.entries = []  # List of Entry widgets

        # Titles for the columns
        Label(self, text=titulo_criterios, bg="gray", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=5)
        Label(self, text=titulo_valores, bg="gray", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10, pady=5)

        # Create rows of criteria and input fields
        for i, criterio in enumerate(criterios):
            Label(self, text=criterio, bg="lightgray", font=("Arial", 11)).grid(row=i + 1, column=0, padx=10, pady=5, sticky="w")

            var = StringVar()
            entry = Entry(self, textvariable=var, width=ancho_entry)

            # Insert default values if provided
            if valores and i < len(valores):
                var.set(valores[i])

            # Disable entry if specified
            if habilitados and i < len(habilitados) and not habilitados[i]:
                entry.config(state='readonly')

            entry.grid(row=i + 1, column=1, padx=10, pady=5, sticky="w")

            self.valores_vars.append(var)
            self.entries.append(entry)

        # Add action buttons
        Button(self, text="Limpiar", command=self.limpiar_entradas, font=("Arial", 10)).grid(row=len(criterios) + 1, column=0, padx=10, pady=5, sticky="w")

    def limpiar_entradas(self):
        """ Clears all input fields. """
        for var in self.valores_vars:
            var.set("")

    def obtener_valores(self):
        """ Returns the values entered by the user as a list. """
        return [var.get() for var in self.valores_vars]

    def obtener_valor_por_criterio(self, criterio):
        """
        Gets the value of a specific criterion.

        Parameters:
            criterio (str): The criterion name.

        Returns:
            str: The value of the corresponding field or None if not found.
        """
        if criterio in self.criterios:
            index = self.criterios.index(criterio)
            return self.valores_vars[index].get()
        return None

    def habilitar_entry(self, indice, habilitar=True):
        """
        Enables or disables a specific entry field.

        Parameters:
            indice (int): Index of the entry field (0-based).
            habilitar (bool): If True, enables the field; otherwise, disables it.
        """
        if 0 <= indice < len(self.entries):
            state = "normal" if habilitar else "readonly"
            self.entries[indice].config(state=state)
