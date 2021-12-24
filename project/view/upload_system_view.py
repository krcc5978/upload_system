import tkinter as tk
from project.controller.upload_system_controller import execute_upload
from project.view.init_parts import InitParts


class UploadSystemView:

    def __init__(self, master, ulm):
        self.input = InitParts(master, '入力ファイル', 0, 0, (10, 0), (10, 0))
        self.config = InitParts(master, '設定ファイル', 3, 0, (10, 0), (10, 0))
        self.config.entry.insert(0, 'config.ini')

        self.counter_label = tk.Label(master, textvariable=ulm.counter_text, font=('Helvetica', 10))
        self.counter_label.grid(row=5, column=1, sticky=tk.E, padx=(10, 0))

        self.execute_button = tk.Button(master, text=u'実行', font=('Helvetica', 8),
                                        command=lambda: execute_upload(self.config.entry.get(),
                                                                       self.input.entry.get(),
                                                                       ulm,
                                                                       self.execute_button
                                                                       ))
        self.execute_button.grid(row=5, column=2, padx=(10, 0), sticky=tk.W)
