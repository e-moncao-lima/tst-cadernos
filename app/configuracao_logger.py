import os
import logging
from logging.handlers import TimedRotatingFileHandler


ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
LOG_FORMAT = '[%(asctime)s] - %(levelname)s - Line %(lineno)s on function %(funcName)s from %(filename)s: %(message)s'
DATE_FORMAT = '%a, %d %b %Y %H:%M:%S'


def get_cmd_handler() -> logging.StreamHandler:
    cmd_handler = logging.StreamHandler()
    cmd_handler.setLevel(logging.DEBUG)
    cmd_format = logging.Formatter(LOG_FORMAT, DATE_FORMAT)
    cmd_handler.setFormatter(cmd_format)
    return cmd_handler


def get_file_handler() -> TimedRotatingFileHandler:
    file_handler = TimedRotatingFileHandler(os.path.join(ROOT_DIR, 'logs', 'tst-cadernos.log'), 
                                            when='midnight', backupCount=30, encoding='utf-8')
    file_handler.suffix = "%d-%m-%Y"
    file_handler.setLevel(logging.INFO)
    file_format = logging.Formatter(LOG_FORMAT, DATE_FORMAT)
    file_handler.setFormatter(file_format)
    return file_handler


def get_custom_logger() -> logging.Logger:
    logger = logging.getLogger(__file__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_cmd_handler())
    logger.addHandler(get_file_handler())
    logger.propagate = False
    return logger