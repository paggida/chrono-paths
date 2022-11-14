import os
import shutil

from src.application.usecases.get_file_destine_folder_usecase import (
    GetFileDestineFolderUseCase,
)
from src.infrastructure.logger import Logger

logger = Logger(__name__)


class OrganizeFilesUseCase(object):
    IGNORED_FILES_LIST = [".DS_Store"]

    def __init__(self, path, is_cut_request=False):
        self.is_cut_request: bool = is_cut_request
        self.path: str = path
        self.files_list: list[str] = self._get_files_list()

    def _get_files_list(self):
        files = os.listdir(self.path)
        return [
            file
            for file in files
            if os.path.isfile(f"{self.path}/{file}")
            and file not in self.IGNORED_FILES_LIST
        ]

    def _create_file_path(self, file_path):
        if not os.path.isdir(file_path):
            os.mkdir(file_path)

    def _organize_files(self):
        for filename in self.files_list:
            destination_folder = GetFileDestineFolderUseCase(
                self.path, filename
            ).execute()

            self._create_file_path(destination_folder)

            try:
                if self.is_cut_request:
                    shutil.move(
                        f"{self.path}/{filename}", f"{destination_folder}/{filename}"
                    )
                else:
                    shutil.copy2(f"{self.path}/{filename}", destination_folder)
            except shutil.SameFileError:
                logger.error(
                    "Source and destination represents the same file.",
                    f"File: { filename }",
                )
            except PermissionError:
                logger.error("Permission denied.")
            except Exception as e:
                logger.error("Error occurred while copying file.", e)

    def execute(self) -> dict:
        self._organize_files()
        return {
            "total_files": len(self.files_list),
        }
