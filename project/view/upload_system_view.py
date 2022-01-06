import os
import tkinter as tk
from tkinter import filedialog
from project.controller.upload_system_controller import execute_upload


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


class UploadSystemView:

    def __init__(self, master, ulm):
        self.input = InitParts(master, '入力ファイル', 0, 0, (10, 0), (10, 0))
        self.config = InitParts(master, '設定ファイル', 3, 0, (10, 0), (10, 0))
        self.config.entry.insert(0, 'config.ini')

        self.start_time = tk.Label(master, text='開始時間', font=('Helvetica', 10))
        self.start_time.grid(row=5, column=0, rowspan=2, sticky=tk.NW, padx=(10, 0), pady=(10, 0))
        self.start_time_entry = tk.Entry(master, width=10)
        self.start_time_entry.grid(row=5, column=1, sticky=tk.NW, padx=(10, 0), pady=(10, 0))
        self.start_time_entry.insert(0, 0)

        self.skip_time = tk.Label(master, text='スキップフレーム', font=('Helvetica', 10))
        self.skip_time.grid(row=6, column=0, rowspan=2, sticky=tk.NW, padx=(10, 0), pady=(10, 0))
        self.skip_time = tk.Entry(master, width=10)
        self.skip_time.grid(row=6, column=1, sticky=tk.NW, padx=(10, 0), pady=(10, 0))
        self.skip_time.insert(0, 0)

        self.counter_label = tk.Label(master, textvariable=ulm.counter_text, font=('Helvetica', 10))
        self.counter_label.grid(row=7, column=1, sticky=tk.E, padx=(10, 0))

        self.execute_button = tk.Button(master, text=u'実行', font=('Helvetica', 8),
                                        command=lambda: execute_upload(self.config.entry.get(),
                                                                       self.input.entry.get(),
                                                                       ulm,
                                                                       self.execute_button
                                                                       ))
        self.execute_button.grid(row=7, column=2, padx=(10, 0), sticky=tk.W)
