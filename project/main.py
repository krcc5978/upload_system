
import tkinter as tk
from project.GUI_parts.init_parts import InitParts
from project.controller.upload_system_controller import execute_upload
from project.model.upload_system_model import UploadSystemModel


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.ulm = UploadSystemModel()

        self.master.geometry("640x380")
        self.master.title('ファイルアップロード')

        self.input = InitParts(self.master, '入力ファイル', 0, 0, (10, 0), (10, 0))
        self.config = InitParts(self.master, '設定ファイル', 3, 0, (10, 0), (10, 0))
        self.config.entry.insert(0, 'config.ini')

        self.counter_label = tk.Label(self.master, textvariable=self.ulm.counter_text, font=('Helvetica', 10))
        self.counter_label.grid(row=5, column=1, sticky=tk.E, padx=(10, 0))

        self.execute_button = tk.Button(self.master, text=u'実行', font=('Helvetica', 8),
                                        command=lambda: execute_upload(self.config.entry.get(),
                                                                       self.input.entry.get(),
                                                                       self.ulm,
                                                                       self.execute_button
                                                                       ))
        self.execute_button.grid(row=5, column=2, padx=(10, 0), sticky=tk.W)


def main():
    root = tk.Tk()
    app = Application(master=root)  # Inherit
    app.mainloop()


if __name__ == "__main__":
    main()
