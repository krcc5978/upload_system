import os
from project.utils import now_time_str
from logging import Formatter, handlers, StreamHandler, getLogger, DEBUG


class Logger:
    def __init__(self, log_file_name=now_time_str(), dir_path='Log'):
        self.logger = getLogger(log_file_name)
        self.logger.setLevel(DEBUG)
        formatter = Formatter("[%(asctime)s] [%(process)d] [%(name)s] [%(levelname)s] %(message)s")

        # stdout
        handler = StreamHandler()
        handler.setLevel(DEBUG)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        os.makedirs(dir_path, exist_ok=True)

        # file
        handler = handlers.RotatingFileHandler(filename=f'{dir_path}/{log_file_name}.log',
                                               maxBytes=1048576,
                                               backupCount=3)
        handler.setLevel(DEBUG)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg, exc_info=True)

    def critical(self, msg):
        self.logger.critical(msg, exc_info=True)
