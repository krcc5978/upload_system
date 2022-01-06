import tkinter as tk
from project.controller.config_system_controller import update_config
from project.model.config_system_model import ConfigSystemModel


class InitParts:

    def __init__(self, master, text, row, col, padx, pady, default_entry):
        self.head = tk.Label(master, text=text, font=('Helvetica', 10))
        self.head.grid(row=row, column=col, rowspan=2, sticky=tk.NW, padx=padx, pady=pady)

        self.entry = tk.Entry(master, width=50)
        self.entry.grid(row=row, column=col + 1, padx=padx, pady=pady)
        self.entry.insert(0, default_entry)


class ConfigSystemView:

    def __init__(self, master, config_path):
        self.config = ConfigSystemModel(config_path)

        self.ip = InitParts(master, 'サーバIP', 0, 0, (10, 0), (10, 0), self.config.ip)
        self.pc_name = InitParts(master, 'PC名', 1, 0, (10, 0), (10, 0), self.config.pc_name)
        self.share_folder = InitParts(master, '共有フォルダ', 2, 0, (10, 0), (10, 0), self.config.share_folder)
        self.login_id = InitParts(master, 'ID', 3, 0, (10, 0), (10, 0), self.config.login_id)
        self.login_pass = InitParts(master, 'パスワード', 4, 0, (10, 0), (10, 0), self.config.login_pass)

        self.update_button = tk.Button(master, text=u'更新', font=('Helvetica', 8),
                                       command=lambda: update_config(self.config,
                                                                     self.ip.entry.get(),
                                                                     self.pc_name.entry.get(),
                                                                     self.share_folder.entry.get(),
                                                                     self.login_id.entry.get(),
                                                                     self.login_pass.entry.get(),
                                                                     ))
        self.update_button.grid(row=5, column=2, padx=(10, 0), sticky=tk.W)
