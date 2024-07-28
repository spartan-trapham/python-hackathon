import logging

import colorlog
from asgi_correlation_id import CorrelationIdFilter

CONSOLE_FORMATTER = (
    "%(asctime)s %(log_color)s%(levelname)-5s%(reset)s %(process)d --- [%(threadName)s]"
    " %(cyan)s%(name)s%(reset)s --- %(correlation_id)s: %(message)s"
)


def console_handler():
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(CONSOLE_FORMATTER))
    handler.addFilter(CorrelationIdFilter())
    return handler


def setup_logger(logger_name, level=logging.DEBUG):
    logger = logging.getLogger(logger_name)
    logger.setLevel(level=level)
    logger.propagate = False
    logger.addHandler(console_handler())
    return logger
