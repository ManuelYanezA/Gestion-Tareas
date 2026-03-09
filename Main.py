import tkinter as tk
from tkinter import ttk

class GestionTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.root.geometry("800x600")

        self.setup_ui()

    def setup_ui(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = GestionTareas(root)
    root.mainloop()