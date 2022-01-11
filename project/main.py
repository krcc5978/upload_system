import tkinter as tk
import tkinter.ttk as ttk

from project.model.upload_system_model import UploadSystemModel
from project.view.download_system_view import DownloadSystemView
from project.view.upload_system_view import UploadSystemView
from project.view.config_system_view import ConfigSystemView


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        config_path = './config.ini'

        # self.ulm = UploadSystemModel()
        # self.dlm = UploadSystemModel()

        self.master.geometry("580x320")
        self.master.title('ファイルアップロード')
        self.master.resizable(width=False, height=False)

        # Notebookウィジェットの作成
        self.notebook = ttk.Notebook(self.master)

        # タブの作成
        self.tab_one = tk.Frame(self.notebook)
        # self.tab_two = tk.Frame(self.notebook)
        # self.tab_three = tk.Frame(self.notebook)

        # notebookにタブを追加
        self.notebook.add(self.tab_one, text="upload")
        # self.notebook.add(self.tab_two, text="download")
        # self.notebook.add(self.tab_three, text="config")

        self.upload_view = UploadSystemView(self.tab_one, config_path)
        # self.download_view = DownloadSystemView(self.tab_two, self.dlm)
        # self.config_view = ConfigSystemView(self.tab_three, config_path)

        # ウィジェットの配置
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)


def main():
    root = tk.Tk()
    app = Application(master=root)  # Inherit
    app.mainloop()


if __name__ == "__main__":
    main()
