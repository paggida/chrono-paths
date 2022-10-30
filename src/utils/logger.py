import enum
import json
import logging
import os
from datetime import datetime


def _get_log_level():
    configured_level = os.environ.get("LOG_LEVEL", "INFO")
    return logging.getLevelName(configured_level)


class LogLevel(enum.Enum):
    EMERGENCY = 0
    ALERT = 1
    CRITICAL = 2
    ERROR = 3
    WARNING = 4
    NOTICE = 5
    INFO = 6
    DEBUG = 7


class Logger(object):
    def __init__(self, module):
        self.module = module
        logger = logging.getLogger(module)
        logger.setLevel(_get_log_level())
        self.logger = logger

    def info(self, operation, message, full_message=None):
        self._log(self.logger.info, LogLevel.INFO, operation, message, full_message)

    def error(self, operation, message, full_message=None):
        self._log(self.logger.error, LogLevel.ERROR, operation, message, full_message)

    def debug(self, operation, message, full_message=None):
        self._log(self.logger.debug, LogLevel.DEBUG, operation, message, full_message)

    def warn(self, operation,  message, full_message=None):
        self._log(self.logger.warn, LogLevel.WARNING, operation, message, full_message)

    def _log(
        self,
        log_level_function,
        log_level,
        operation,
        short_message,
        full_message=None
    ):
        log_data = {
            "version": "1.0",
            "host": "script",
            "short_message": short_message,
            "full_message": full_message if full_message else "",
            "timestamp": self._now_in_millis(),
            "level": log_level.value,
            "file": self.module,
            "operation": operation,
            "_log_type": "application",
        }
        log_level_function(json.dumps(log_data), exc_info=1)

    def _now_in_millis(self):
        epoch = datetime.utcfromtimestamp(0)
        return (datetime.utcnow() - epoch).total_seconds() * 1000.0
