import cv2
import sys
from project.file_manager import FileManager
from project.logger import Logger
from test.test_const_value import *

logger = Logger()
c = FileManager(logger)


def test_file_dir_check1():
    logger.info(f'-------- {sys._getframe().f_code.co_name} --------')
    assert not c.file_dir_check('test_data/_test_img.png')


def test_file_dir_check2():
    logger.info(f'-------- {sys._getframe().f_code.co_name} --------')
    assert c.file_dir_check('./test_data/test_img.png')


def test_file_dir_check3():
    logger.info(f'-------- {sys._getframe().f_code.co_name} --------')
    assert not c.file_dir_check('test_data/_test_data.mp4')


def test_file_dir_check4():
    logger.info(f'-------- {sys._getframe().f_code.co_name} --------')
    assert c.file_dir_check('./test_data/test_data.mp4')


def test_load_config_file1():
    logger.info(f'-------- {sys._getframe().f_code.co_name} --------')
    assert not c.load_config_file('./_config.ini')


def test_load_config_file2():
    logger.info(f'-------- {sys._getframe().f_code.co_name} --------')
    assert c.load_config_file('./config.ini')


def test_get_file_type1():
    logger.info(f'-------- {sys._getframe().f_code.co_name} --------')
    assert c.get_file_type('test_data/_test_img.png') is None


def test_get_file_type2():
    logger.info(f'-------- {sys._getframe().f_code.co_name} --------')
    assert 'image' in c.get_file_type('test_data/test_img.png')


def test_get_file_type3():
    logger.info(f'-------- {sys._getframe().f_code.co_name} --------')
    assert 'video' in c.get_file_type('test_data/test_data.mp4')


def test_get_file_name():
    logger.info(f'-------- {sys._getframe().f_code.co_name} --------')
    file_path = base_path + '/test_data/test_img.png'
    assert c.get_file_name(file_path) == 'test_img'


def test_file_upload1(del_dst_test, make_test_data):
    logger.info(f'-------- {sys._getframe().f_code.co_name} --------')
    src_contains = os.listdir(src_dir_path)

    # ファイルアップロード処理
    path = c.upload_file_list(src_dir_path, dst_dir_path)
    dst_contains = os.listdir(dst_dir_path + '/input')

    assert (set(src_contains) == set(dst_contains)) and (path is not None)


def test_file_upload2(del_dst_test, make_test_data):
    logger.info(f'-------- {sys._getframe().f_code.co_name} --------')
    # ファイルアップロード処理
    path = c.upload_file_list(dummy_src_dir_path, dst_dir_path)
    assert path is None


def test_file_upload3(del_dst_test, make_test_data):
    logger.info(f'-------- {sys._getframe().f_code.co_name} --------')
    src_contains = os.listdir(src_dir_path)
    # ファイルアップロード処理
    path = c.upload_file_list(src_dir_path, dummy_dst_dir_path)
    dst_contains = os.listdir(dummy_dst_dir_path + '/input')

    assert (set(src_contains) == set(dst_contains)) and (path is not None)


def test_file_upload4(del_dst_test, make_test_data):
    logger.info(f'-------- {sys._getframe().f_code.co_name} --------')
    # ファイルアップロード処理
    path = c.upload_file_list(dummy_src_dir_path, dummy_dst_dir_path)

    assert path is None


def test_file_upload5(del_dst_test, make_test_data):
    logger.info(f'-------- {sys._getframe().f_code.co_name} --------')
    os.makedirs(dst_dir_path + '/input')

    # ファイルアップロード処理
    path = c.upload_file_list(src_dir_path, dst_dir_path)

    assert path is None


def test_save_img1(del_dst_test):
    logger.info(f'-------- {sys._getframe().f_code.co_name} --------')
    os.makedirs(dst_dir_path)
    flag = c.save_img('test_data/test_img.png', dst_dir_path)
    file_list = os.listdir(dst_dir_path)
    assert ('test_img.png' in file_list) and flag


def test_save_img2(del_dst_test):
    logger.info(f'-------- {sys._getframe().f_code.co_name} --------')
    flag = c.save_img('test_data/dummy_test_img.png', dst_dir_path)
    assert not flag


def test_save_img3(del_dst_test):
    logger.info(f'-------- {sys._getframe().f_code.co_name} --------')
    flag = c.save_img('test_data/test_img.png', dst_dir_path)
    assert not flag


def test_load_movie1(del_dst_test):
    logger.info(f'-------- {sys._getframe().f_code.co_name} --------')
    flag = c.load_movie(dummy_movie_path,
                        src_dir_path,
                        'sparate_image')
    assert not flag


def test_load_movie2(del_dst_test):
    logger.info(f'-------- {sys._getframe().f_code.co_name} --------')
    flag = c.load_movie(movie_path,
                        dummy_src_dir_path,
                        'sparate_image')
    assert not flag


def test_load_movie3(del_dst_test):
    logger.info(f'-------- {sys._getframe().f_code.co_name} --------')
    cap = cv2.VideoCapture(movie_path)
    total_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    c.load_movie(movie_path,
                 src_dir_path,
                 'sparate_image')
    assert total_frame == len(os.listdir(src_dir_path))


def test_load_movie4(del_dst_test):
    logger.info(f'-------- {sys._getframe().f_code.co_name} --------')
    cap = cv2.VideoCapture(movie_path)
    total_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    start_time = 10

    c.load_movie(movie_path,
                 src_dir_path,
                 'sparate_image',
                 start_time=start_time)

    assert (total_frame - start_time * fps) == len(os.listdir(src_dir_path))


def test_load_movie5(del_dst_test):
    logger.info(f'-------- {sys._getframe().f_code.co_name} --------')
    cap = cv2.VideoCapture(movie_path)
    total_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    skip_time = 10

    c.load_movie(movie_path,
                 src_dir_path,
                 'sparate_image',
                 skip_time=skip_time)

    assert total_frame / (fps * skip_time) == len(os.listdir(src_dir_path))


def test_load_movie6(del_dst_test):
    logger.info(f'-------- {sys._getframe().f_code.co_name} --------')
    cap = cv2.VideoCapture(movie_path)
    total_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    start_time = 10
    skip_time = 10

    c.load_movie(movie_path,
                 src_dir_path,
                 'sparate_image',
                 start_time=start_time,
                 skip_time=skip_time)

    assert (total_frame - start_time * fps) / (fps * skip_time) == len(os.listdir(src_dir_path))
