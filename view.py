import tkinter as tk
from tkinter import ttk



class View(tk.Tk):

    def __init__(self, controller):
        self.controller = controller

        super().__init__()

        self.controller = controller

    def main(self):
        self.mainloop()

