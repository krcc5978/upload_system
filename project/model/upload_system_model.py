import tkinter as tk
from multiprocessing import Value


class UploadSystemModel:

    def __init__(self):
        self.flag = Value('b', True)
        self.message = tk.StringVar()
        self.message.set('')
