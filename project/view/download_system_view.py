import tkinter as tk
from project.view.init_parts import InitParts
from project.controller.download_system_controller import execute_download


class DownloadSystemView:

    def __init__(self, master, dlm):
        self.input_dir = InitParts(master, 'ダウンロード元', 0, 0, (10, 0), (10, 0), True)
        self.output_dir = InitParts(master, 'ダウンロード先', 3, 0, (10, 0), (10, 0), True)

        self.counter_label = tk.Label(master, textvariable=dlm.counter_text, font=('Helvetica', 10))
        self.counter_label.grid(row=5, column=1, sticky=tk.E, padx=(10, 0))

        self.execute_button = tk.Button(master, text=u'実行', font=('Helvetica', 8),
                                        command=lambda: execute_download(self.output_dir.entry.get(),
                                                                         self.input_dir.entry.get(),
                                                                         dlm,
                                                                         self.execute_button))
        self.execute_button.grid(row=5, column=2, padx=(10, 0), sticky=tk.W)
