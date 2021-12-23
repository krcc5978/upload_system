import threading
import time
import tkinter as tk
from multiprocessing import Value
from project.GUI_parts.init_parts import InitParts
from project.upload_vott import upload_vott


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.flag = Value('b', True)
        self.count = Value('i', 0)
        self.total = Value('i', 0)

        self.counter_text = tk.StringVar()
        self.counter_text.set('')

        self.master.geometry("640x380")
        self.master.title('ファイルアップロード')

        self.input = InitParts(self.master, '入力ファイル', 0, 0, (10, 0), (10, 0))
        self.config = InitParts(self.master, '設定ファイル', 3, 0, (10, 0), (10, 0))
        self.config.entry.insert(0, 'config.ini')

        self.counter_label = tk.Label(self.master, textvariable=self.counter_text, font=('Helvetica', 10))
        self.counter_label.grid(row=5, column=1, sticky=tk.E, padx=(10, 0))

        self.execute_button = tk.Button(self.master, text=u'実行', font=('Helvetica', 8), command=self.execute_upload)
        self.execute_button.grid(row=5, column=2, padx=(10, 0), sticky=tk.W)

    def execute_upload(self):
        upload_thread = threading.Thread(target=upload_vott,
                                         args=(self.config.entry.get(),
                                               self.input.entry.get(),
                                               self.flag,
                                               self.count,
                                               self.total),
                                         kwargs={'start_time': 10, 'skip_time': 10})
        upload_thread.start()

        check_thread = threading.Thread(target=self.check_flag)
        check_thread.start()

    def check_flag(self):
        self.execute_button['state'] = 'disable'
        self.counter_text.set('アップロード準備中')

        while self.flag.value:
            if self.total.value == 0:
                time.sleep(1 / 1000)
            if self.total.value != 0:
                self.counter_text.set(f'アップロード中　： ({str(self.count.value)} / {str(self.total.value)})')

        self.counter_text.set(f'アップロード完了')
        self.count.value = 0
        self.flag.value = True
        self.execute_button['state'] = 'normal'


def main():
    root = tk.Tk()
    app = Application(master=root)  # Inherit
    app.mainloop()


if __name__ == "__main__":
    main()
