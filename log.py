import sys
import logging

app_logger = logging.getLogger('app')
log_formatter = logging.Formatter(u"%(asctime)s [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S")
logging_console_handler = logging.StreamHandler(stream=sys.stdout)
logging_console_handler.setFormatter(log_formatter)
app_logger.setLevel(logging.DEBUG)
app_logger.addHandler(logging_console_handler)


def debug(msg, *args, **kwargs):
    app_logger.debug(msg, *args, **kwargs)


def info(msg, *args, **kwargs):
    app_logger.info(msg, *args, **kwargs)


def error(msg, *args, **kwargs):
    app_logger.error(msg, *args, **kwargs)


def warning(msg, *args, **kwargs):
    app_logger.warning(msg, *args, **kwargs)


def critical(msg, *args, **kwargs):
    app_logger.critical(msg, *args, **kwargs)
