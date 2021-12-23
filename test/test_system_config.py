from project.system_config import SystemConfig
from project.logger import Logger

logger = Logger()


def test_system_config1():
    config = SystemConfig(logger, 'config.ini')

    assert config.get_config('TEMP', 'path') == 'TEMP/'


def test_system_config2():
    config = SystemConfig(logger, 'config.ini')

    assert config.get_config('_TEMP', 'path') is None


def test_system_config3():
    config = SystemConfig(logger, 'config.ini')

    assert config.get_config('TEMP', '_path') is None


def test_system_config4():
    config = SystemConfig(logger, 'config.ini')

    assert config.get_config('TEMP')