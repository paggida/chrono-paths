import logging
import os


def _get_log_level():
    configured_level = os.environ.get("LOG_LEVEL", "INFO")
    return logging.getLevelName(configured_level)


class Logger(object):
    def __init__(self, module):
        self.module = module
        logger = logging.getLogger(module)
        logging.basicConfig(level=_get_log_level())
        self.logger = logger

    def log(self, message, full_message=None, operation=None):
        print(self._get_log_message(message, full_message, operation))

    def error(self, message, full_message=None, operation=None):
        self._log(self.logger.error, message, full_message, operation)

    def warn(self, message, full_message=None, operation=None):
        self._log(self.logger.warning, message, full_message, operation)

    def _log(
        self,
        log_level_function,
        short_message,
        full_message=None,
        operation=None,
    ):
        log_data = self._get_log_message(short_message, full_message, operation)

        log_level_function(log_data, exc_info=1)

    def _get_log_message(
        self,
        short_message,
        full_message=None,
        operation=None,
    ):
        operation_msg = f"({operation if operation else ''}): " if operation else ""
        return f"{operation_msg if operation_msg else ''}{short_message}{f' - {full_message}' if full_message else ''}"
