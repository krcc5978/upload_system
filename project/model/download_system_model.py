import tkinter as tk
from multiprocessing import Value


class UploadSystemModel:

    def __init__(self):
        self.flag = Value('b', True)
        self.count = Value('i', 0)
        self.total = Value('i', 0)
        self.counter_text = tk.StringVar()
        self.counter_text.set('')
