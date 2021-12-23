import threading
import project.upload_vott as m
from test.test_const_value import *
from project.file_manager import FileManager
from project.logger import Logger
from multiprocessing import Value

logger = Logger()
c = FileManager(logger)


def test_main1(del_dst_test):
    flag = Value('b')
    count = Value('i')
    total = Value('i')
    upload_thread = threading.Thread(target=m.upload_vott,
                                     args=('config.ini', dummy_movie_path, flag, count, total)
                                     )
    upload_thread.start()
    upload_thread.join()

    assert not flag.value


def test_main2(del_dst_test):
    flag = Value('b')
    count = Value('i')
    total = Value('i')
    upload_thread = threading.Thread(target=m.upload_vott,
                                     args=('config.ini', dummy_movie_path, flag, count, total)
                                     )
    upload_thread.start()
    upload_thread.join()
    file_name = c.get_file_name(movie_path)
    file_list = os.listdir(upload_path + file_name + '/input')
    output_list = os.listdir(upload_path + file_name + '/output')
    assert (len(file_list) == 600) and ('test_data.vott' in output_list)
