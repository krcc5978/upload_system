import os
import sys
import shutil
from project import vott as v
from project.file_manager import FileManager
from project.logger import Logger

logger = Logger()


def system_finish(flag):
    flag.value = False
    sys.exit(1)


def upload_vott(config_path, input_path, output_path, finish_flag, count, total, **kwargs):
    logger.info(f'>> start upload system')

    fm = FileManager(logger)

    # configファイル読み込み
    conf = fm.load_config_file(config_path)
    if conf is None:
        system_finish(finish_flag)

    # 拡張子除くファイル名取得
    mime = fm.get_file_type(input_path)
    if mime is None:
        system_finish(finish_flag)
    file_name = fm.get_file_name(input_path)

    # TEMPディレクトリの作成
    # このTEMPディレクトリは最後に削除される
    if conf.get_config("TEMP", "path") is None:
        system_finish(finish_flag)
    temp_path = f'{conf.get_config("TEMP", "path")}{file_name}/'
    os.makedirs(temp_path, exist_ok=True)

    # ファイル形式によって分岐
    if 'video' in mime:
        fm.load_movie(count, total, input_path, temp_path, file_name, **kwargs)
    elif 'image' in mime:
        fm.save_img(total, input_path, temp_path)
    else:
        logger.error(f'>> file type is not image or movie')
        system_finish(finish_flag)

    # vottファイルの作成
    # アップロードがあるものがあれば.vottまで作成し、
    # アップロードするものがない場合はエラー出力をして終了
    if conf.get_config("VOTT") is None:
        system_finish(finish_flag)
    upload_path = f'{output_path}/{file_name}'
    vott_input_path = fm.upload_file_list(temp_path, upload_path)
    if vott_input_path:
        flag = v.make_vott_file(logger, conf, file_name, upload_path, vott_input_path)
        if not flag:
            logger.error('.vott file creation failed')
            system_finish(finish_flag)
    else:
        logger.error('Upload image file is failed')
        system_finish(finish_flag)

    shutil.rmtree(temp_path)
    system_finish(finish_flag)


if __name__ == '__main__':
    from multiprocessing import Value
    f = Value('b')
    c = Value('i')
    t = Value('i')
    upload_vott('config.ini',
                "\\\\192.168.2.129\\camera_data\\test_data\\CAM-J-01\\CAM-J-01_high_place2.mp4",
                f,
                c,
                t,
                start_time=600,
                skip_time=60
                )
