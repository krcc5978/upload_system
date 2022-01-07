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


def execute_upload(config_path, input_path, output_path, model, button, *args):
    if input_path == '':
        model.counter_text.set(f'アップロードファイルが選択されていません')
        return

    if output_path == '':
        model.counter_text.set(f'出力先ディレクトリが選択されていません')
        return

    time_conf_dict = {}
    if 0 < int(args[0]):
        time_conf_dict['start_time'] = int(args[0])
    if 0 < int(args[1]):
        time_conf_dict['skip_time'] = int(args[1])
    if 0 < int(args[2]):
        time_conf_dict['end_time'] = int(args[2])

    upload_thread = threading.Thread(target=upload_vott,
                                     args=(config_path,
                                           input_path,
                                           output_path,
                                           model.flag,
                                           model.count,
                                           model.total,),
                                     kwargs=time_conf_dict)
    upload_thread.start()

    check_thread = threading.Thread(target=check_flag,
                                    args=(model, button,)
                                    )
    check_thread.start()
