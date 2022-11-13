from src.domain.validators import get_validators_list


class GetFileDestineFolderUseCase(object):
    UNCLASSIFIED_FILES_FOLDER = "[Unclassified]"

    def __init__(self, path, file_name):
        self.path: str = path
        self.name: str = file_name

    def _get_full_path_destination_folder(self, folder):
        return f"{self.path}/{folder}"

    def execute(self) -> str:
        for validator_class in get_validators_list():
            file_destination_folder = validator_class(self.name).validate()
            if file_destination_folder:
                return self._get_full_path_destination_folder(file_destination_folder)

        return self._get_full_path_destination_folder(self.UNCLASSIFIED_FILES_FOLDER)
