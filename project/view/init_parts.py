import os
import tkinter as tk
from tkinter import filedialog


def changeText(entry, dir_flag=False):
    fTyp = [("", "*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    if dir_flag:
        path = filedialog.askdirectory()
    else:
        path = filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)

    if path != '':
        entry.delete(0, tk.END)
        entry.insert(0, path)


class InitParts:

    def __init__(self, master, text, row, col, padx, pady, dir_flag=False):
        self.head = tk.Label(master, text=text, font=('Helvetica', 10))
        self.head.grid(row=row, column=col, rowspan=2, sticky=tk.NW, padx=padx, pady=pady)

        self.entry = tk.Entry(master, width=50)
        self.entry.grid(row=row, column=col + 1, padx=padx, pady=pady)

        self.scroll = tk.Scrollbar(master, orient=tk.HORIZONTAL, command=self.entry.xview)
        self.scroll.grid(row=row + 1, column=col + 1, padx=padx, sticky=tk.W + tk.E)
        self.entry.config(xscrollcommand=self.scroll.set)

        self.button = tk.Button(master, text=u'参照', font=('Helvetica', 8),
                                command=lambda: changeText(self.entry, dir_flag))
        self.button.grid(row=row, column=col + 2, sticky=tk.W, padx=(padx[0], padx[1] + 10), pady=pady)
