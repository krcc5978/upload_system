import cv2
import pytest
import shutil
import datetime as dt
from test.test_const_value import *
from project.file_manager import FileManager
from project.logger import Logger


def now_time_str():
    now = dt.datetime.now()
    return '{0:%Y%m%d%H%M%S%f}'.format(now)


@pytest.fixture
def del_dst_test():
    if os.path.isdir(src_dir_path):
        shutil.rmtree(src_dir_path)
    if os.path.isdir(dst_dir_path):
        shutil.rmtree(dst_dir_path)
    if os.path.isdir(dummy_src_dir_path):
        shutil.rmtree(dummy_src_dir_path)
    if os.path.isdir(dummy_dst_dir_path):
        shutil.rmtree(dummy_dst_dir_path)

    os.makedirs(src_dir_path)


@pytest.fixture
def make_test_data():
    cap = cv2.VideoCapture(movie_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    start_time = 0
    skip_time = 10
    end_time = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # 最初何秒飛ばすか
    for _ in range(0, fps * start_time):
        ret = cap.grab()
        if ret is False:
            break

    if skip_time != 0:
        skip_frame = fps * skip_time
    else:
        skip_frame = 1

    for i in range(fps * start_time, end_time):  # フレーム数分回す

        # スキップするフレーム数によって保存するか決める
        if i % skip_frame is 0:
            ret, frame = cap.read()
            cv2.imwrite(f'{src_dir_path}/sparate_image_{str(i).zfill(digit)}.jpg', frame)
            if ret is False:
                break
        else:
            ret = cap.grab()
            if ret is False:
                break

    return True
