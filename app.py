import sys

from src.infrastructure.logger import Logger
from src.domain.argument import Argument

logger = Logger(__name__)

if __name__ == "__main__":
    app_arguments = Argument(sys.argv)

    if app_arguments.is_valid:
        logger.log(f"Iupi, we get arguments: {app_arguments.argument_list}")
    else:
        logger.error(app_arguments.errors)
