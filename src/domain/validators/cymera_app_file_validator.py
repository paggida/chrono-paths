import enum
import os

from src.domain.folder import Folder


class CymeraFileAcceptedFormats(enum.Enum):
    STANDARD = "CYMERA_20150111_222759"
    WITHOUT_FORMAT = None


class CymeraFileValidator(object):
    def __init__(self, file_name):
        self.name: str = os.path.splitext(file_name)[0]
        self._format_functions: dict = {
            CymeraFileAcceptedFormats.STANDARD: self._get_date_to_format_standard,
            CymeraFileAcceptedFormats.WITHOUT_FORMAT: lambda: "",
        }

    def _is_valid_size_name(self) -> bool:
        return len(self.name) == len(CymeraFileAcceptedFormats.STANDARD.value)

    def _get_name_format(self) -> CymeraFileAcceptedFormats:
        if self.name[0:7] == "CYMERA_" and len(self.name.split("_")) == 3:
            return CymeraFileAcceptedFormats.STANDARD

        return CymeraFileAcceptedFormats.WITHOUT_FORMAT

    def _get_date_to_format_standard(self) -> str:
        year = self.name[7:11]
        month = self.name[11:13]
        day = self.name[13:15]
        return Folder.get_folder_name(year, month, day)

    def validate(self) -> str:
        if self._is_valid_size_name():
            return self._format_functions[self._get_name_format()]()

        return ""
