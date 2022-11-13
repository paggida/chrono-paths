import os

from faker import Faker

from src.application.usecases.get_file_destine_folder_usecase import (
    GetFileDestineFolderUseCase,
)

fake = Faker(locale="pt-BR")


class TestGetFileDestineFolderUseCase:
    def test_returns_the_destination_folder_name_when_some_validator_recognizes_the_filename(
        self,
    ):
        path = os.path.dirname(fake.file_path(depth=3))
        file = "IMG-20130916-WA0015.jpg"

        destination_folder_name = GetFileDestineFolderUseCase(path, file).execute()
        assert destination_folder_name == f"{path}/[2013.09.16]"

    def test_returns_an_empty_folder_name_when_no_validator_recognizes_the_filename(
        self,
    ):
        path = os.path.dirname(fake.file_path(depth=3))
        file = fake.pystr()

        destination_folder_name = GetFileDestineFolderUseCase(path, file).execute()
        assert destination_folder_name == f"{path}/[Unclassified]"
