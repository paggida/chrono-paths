import sys

from src.application.usecases.organize_files_usecase import OrganizeFilesUseCase
from src.domain.argument import Argument
from src.infrastructure.logger import Logger

logger = Logger(__name__)

if __name__ == "__main__":
    app_arguments = Argument(sys.argv)

    if app_arguments.is_valid:
        organize_images_use_case = OrganizeFilesUseCase(
            app_arguments.path, app_arguments.is_cut_request
        )
        logger.log("Processing...")
        file_processing_counters = organize_images_use_case.execute()
        logger.log("Organization complete!")
        logger.log(f"Total files: {file_processing_counters['total_files']}")
    else:
        logger.error(app_arguments.errors)
