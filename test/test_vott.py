from project.logger import Logger
from project.system_config import SystemConfig
from project.vott import make_vott_file
from test.test_const_value import *


def test_make_vott_file(del_dst_test):
    logger = Logger()
    config = SystemConfig('config.ini')
    os.makedirs(dst_dir_path)
    make_vott_file(logger, config, 'vott_test', dst_dir_path, src_dir_path)
    assert os.path.exists(dst_dir_path+'/output/vott_test.vott')
