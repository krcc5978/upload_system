import tkinter as tk
from project.view.init_parts import InitParts


class DownloadSystemView:

    def __init__(self, master, ulm):
        self.input = InitParts(master, 'ダウンロード元', 0, 0, (10, 0), (10, 0), True)
        self.output = InitParts(master, 'ダウンロード先', 3, 0, (10, 0), (10, 0), True)

        self.counter_label = tk.Label(master, textvariable=ulm.counter_text, font=('Helvetica', 10))
        self.counter_label.grid(row=5, column=1, sticky=tk.E, padx=(10, 0))

        self.execute_button = tk.Button(master, text=u'実行', font=('Helvetica', 8))
        self.execute_button.grid(row=5, column=2, padx=(10, 0), sticky=tk.W)
