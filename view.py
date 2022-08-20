import tkinter as tk
from tkinter import ttk



class View(tk.Tk):

    PAD = 10

    MAX_BUTTONS_PER_ROW = 4

    button_captions = [
        'C', '+/-', '%', '/', 
        7, 8, 9, '*',
        4, 5, 6, '+',
        1, 2, 3, '+',
        0, '.', '='
    ]

    def __init__(self, controller):

        # CONSTRUCTOR

        super().__init__()

        self.title('Tkinter Calculator')

        self.controller = controller

        self.value_var = tk.StringVar()

        

        self._make_main_frame()
        self._make_entry()
        self._make_buttons()


    def main(self):
        self.mainloop()

    def _make_main_frame(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx=self.PAD, pady=self.PAD)
         

    def _make_entry(self):
        ent = ttk.Entry(self.main_frame, justify='right', textvariable = self.value_var)
        ent.pack()


    def _make_buttons(self):
        frm = ttk.Frame(self.main_frame)
        frm.pack()

        for caption in self.button_captions:
            btn = ttk.Button(frm, text=caption)
            btn.pack()
