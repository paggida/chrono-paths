import os
import shutil

from src.application.usecases.organize_files_usecase import OrganizeFilesUseCase

MOVE_FOLDER_PATH = f"{os.getcwd()}/move"
COPY_FOLDER_PATH = f"{os.getcwd()}/copy"
FILENAME = "IMG-20130916-WA0015.txt"


class TestOrganizeFilesUseCase:
    @classmethod
    def setup_class(cls):
        os.mkdir(MOVE_FOLDER_PATH)
        os.mkdir(COPY_FOLDER_PATH)

        open(f"{MOVE_FOLDER_PATH}/{FILENAME}", "w").close()
        open(f"{COPY_FOLDER_PATH}/{FILENAME}", "w").close()

    @classmethod
    def teardown_class(cls):
        shutil.rmtree(MOVE_FOLDER_PATH)
        shutil.rmtree(COPY_FOLDER_PATH)

    def test_organize_files_by_moving(self):
        organize_files_use_case = OrganizeFilesUseCase(MOVE_FOLDER_PATH, True).execute()

        assert organize_files_use_case.get("total_files", 0) == 1
        files_in_move_folder = os.listdir(MOVE_FOLDER_PATH)
        assert len(files_in_move_folder) == 1
        assert "[2013.09.16]" in files_in_move_folder
        assert os.path.isfile(f"{MOVE_FOLDER_PATH}/[2013.09.16]/{FILENAME}")

    def test_organize_files_by_coping(self):
        organize_files_use_case = OrganizeFilesUseCase(COPY_FOLDER_PATH).execute()

        assert organize_files_use_case.get("total_files", 0) == 1
        files_in_copy_folder = os.listdir(COPY_FOLDER_PATH)
        assert len(files_in_copy_folder) == 2
        assert "[2013.09.16]" in files_in_copy_folder
        assert os.path.isfile(f"{COPY_FOLDER_PATH}/[2013.09.16]/{FILENAME}")
