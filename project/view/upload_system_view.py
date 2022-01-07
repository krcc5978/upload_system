import os
import re
import tkinter as tk
from tkinter import filedialog
from project.controller.upload_system_controller import execute_upload
from project.model.config_system_model import ConfigSystemModel


def num_check(S):
    if re.match(re.compile('[0-9]+'), S):
        return True
    else:
        return False


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

    def __init__(self, master, text, row, col, padx, pady, width=50, dir_flag=False, **kwargs):
        self.head = tk.Label(master, text=text, font=('Helvetica', 10))
        self.head.grid(row=row, column=col, rowspan=2, sticky=tk.NW, padx=padx, pady=pady)

        self.entry = tk.Entry(master, width=width)
        if kwargs.get('num_flag'):
            self.entry.insert(0, 0)
            vcmd = (self.entry.register(num_check), '%S')
            self.entry.configure(validate='key', vcmd=vcmd)
        self.entry.grid(row=row, column=col + 1, padx=padx, pady=pady, sticky=tk.NW)

        if kwargs.get('scroll'):
            self.scroll = tk.Scrollbar(master, orient=tk.HORIZONTAL, command=self.entry.xview)
            self.scroll.grid(row=row + 1, column=col + 1, padx=padx, sticky=tk.EW)
            # self.scroll.grid(row=row + 1, column=col + 1, padx=padx, sticky=tk.W + tk.E)
            self.entry.config(xscrollcommand=self.scroll.set)

        if kwargs.get('ref_button'):
            self.button = tk.Button(master, text=u'参照', font=('Helvetica', 8),
                                    command=lambda: changeText(self.entry, dir_flag))
            self.button.grid(row=row, column=col + 2, sticky=tk.W, padx=(padx[0], padx[1] + 10), pady=pady)


class UploadSystemView:

    def __init__(self, master, ulm, config_path):
        # self.config = ConfigSystemModel(config_path)

        self.input = InitParts(master, '入力ファイル', 0, 0, (10, 0), (10, 0), scroll=True, ref_button=True)
        self.output = InitParts(master, '出力先', 3, 0, (10, 0), (10, 0), dir_flag=True, scroll=True, ref_button=True)

        self.start_time = InitParts(master, '開始時間[s]', 5, 0, (10, 0), (10, 0), width=10, num_flag=True)
        self.skip_time = InitParts(master, 'スキップフレーム', 6, 0, (10, 0), (10, 0), width=10, num_flag=True)
        self.end_time = InitParts(master, '終了時間[s]', 7, 0, (10, 0), (10, 0), width=10, num_flag=True)

        self.counter_label = tk.Label(master, textvariable=ulm.counter_text, font=('Helvetica', 10))
        self.counter_label.grid(row=8, column=1, sticky=tk.E, padx=(10, 0))

        self.execute_button = tk.Button(master, text=u'実行', font=('Helvetica', 8),
                                        command=lambda: execute_upload(config_path,
                                                                       self.input.entry.get(),
                                                                       self.output.entry.get(),
                                                                       ulm,
                                                                       self.execute_button,
                                                                       self.start_time.entry.get(),
                                                                       self.skip_time.entry.get(),
                                                                       self.end_time.entry.get(),
                                                                       ))
        self.execute_button.grid(row=8, column=2, padx=(10, 0), sticky=tk.W)
