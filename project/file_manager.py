import os
import cv2
import shutil
import mimetypes
from tqdm import tqdm
from project.system_config import SystemConfig


def get_value(movie_option, key, default):
    if movie_option.get(key) is None:
        return default
    else:
        return movie_option.get(key)


class FileManager:

    def __init__(self, log):
        self.log = log
        pass

    def file_dir_check(self, path):
        if os.path.isfile(path):
            self.log.info(f'>> Exist file : {path}')
            return True
        elif os.path.isdir(path):
            self.log.info(f'>> Exist directory : {path}')
            return True
        else:
            self.log.error(f'>> {path} is not found')
            return False

    def load_config_file(self, config_path):
        self.log.info(f'>> load config file : {config_path}')
        if not self.file_dir_check(config_path):
            return False

        config = SystemConfig(self.log, config_path)
        # 設定ファイル読み込み
        if not config:
            self.log.error(f'>> {config_path} is not found')
            return None
        return config

    def get_file_type(self, path):
        self.log.info(f'>> check file type : {path}')
        if self.file_dir_check(path):
            mime = mimetypes.guess_type(path)
            self.log.info(f'>> file type : {mime[0]}')
            return mime[0]
        else:
            return None

    def get_file_name(self, file_path):
        replace_file_path = file_path.replace('\\', '/')
        file_name = replace_file_path.split('/')[-1]
        except_file_name = file_name.split('.')[0]
        self.log.info(f'>> except file name : {except_file_name}')
        return except_file_name

    def upload_file_list(self, src_path, dst_path):
        new_input_upload_path = dst_path + '/input'

        try:
            self.log.info(f'>> {src_path} to {new_input_upload_path}')
            shutil.copytree(src_path, new_input_upload_path)
        except Exception as e:
            self.log.error(e)
            return None

        return new_input_upload_path

    def save_img(self, total, image_path, save_path):
        if not self.file_dir_check(image_path):
            return False

        if not self.file_dir_check(save_path):
            return False

        total.value = 1
        shutil.copy(image_path, save_path)
        self.load_config_file(f'>> {image_path} to {save_path}')
        return True

    def load_movie(self, count, total, movie_path, tmp_path, file_name='tmp_name', **kwargs):
        if not self.file_dir_check(movie_path):
            return False

        if not self.file_dir_check(tmp_path):
            self.log.error(f'>> {tmp_path} is not found')
            return False

        cap = cv2.VideoCapture(movie_path)
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

        start_time = get_value(kwargs, 'start_time', 0)
        skip_time = get_value(kwargs, 'skip_time', 0)
        end_time = get_value(kwargs, 'end_time', int(cap.get(cv2.CAP_PROP_FRAME_COUNT) / fps))

        self.log.info(f'>> start time : {str(fps * start_time)} \t skip time : {fps * skip_time}')

        total.value = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # 最初何秒飛ばすか
        for _ in tqdm(range(0, fps * start_time)):
            ret = cap.grab()
            count.value += 1
            if ret is False:
                break

        if skip_time != 0:
            skip_frame = fps * skip_time
        else:
            skip_frame = 1

        for i in tqdm(range(fps * start_time, fps * end_time)):  # フレーム数分回す
            count.value += 1
            # スキップするフレーム数によって保存するか決める
            if i % skip_frame is 0:
                ret, frame = cap.read()
                cv2.imwrite(f'{tmp_path}/{file_name}_{str(i).zfill(digit)}.jpg', frame)
                if ret is False:
                    break
            else:
                ret = cap.grab()
                if ret is False:
                    break

        return True
