import os
import time
import shutil
import threading


def download_system(output_path, dir_path, model, button):
    button['state'] = 'disable'
    model.counter_text.set(f'ダウンロード中')
    dir_name = dir_path.split('/')[-1]
    shutil.make_archive(f'{output_path}/{dir_name}', 'zip', root_dir=dir_path)
    model.counter_text.set(f'ダウンロード完了')
    button['state'] = 'normal'


def execute_download(output_path, input_path, model, button):
    download_thread = threading.Thread(target=download_system,
                                       args=(output_path,
                                             input_path,
                                             model,
                                             button)
                                       )

    download_thread.start()
