import time

import threading
from project.upload_vott import upload_vott



def check_flag(model, button):
    button['state'] = 'disable'
    model.counter_text.set('アップロード準備中')

    while model.flag.value:
        if model.total.value == 0:
            time.sleep(1 / 1000)
        if model.total.value != 0:
            model.counter_text.set(f'アップロード中　： ({str(model.count.value)} / {str(model.total.value)})')

    model.counter_text.set(f'アップロード完了')
    model.count.value = 0
    model.flag.value = True
    button['state'] = 'normal'


def execute_upload(config, input_path, model, button):

    upload_thread = threading.Thread(target=upload_vott,
                                     args=(config,
                                           input_path,
                                           model.flag,
                                           model.count,
                                           model.total),
                                     kwargs={'start_time': 10, 'skip_time': 10})
    upload_thread.start()

    check_thread = threading.Thread(target=check_flag,
                                    args=(model, button,)
                                    )
    check_thread.start()
