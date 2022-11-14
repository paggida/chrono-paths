import enum
import os

from src.domain.folder import Folder


class CamAcceptedFormats(enum.Enum):
    ONE = "31102008710"
    TWO = "20120927165756"
    THREE = "2011-04-28 20.29.56"
    WITHOUT_FORMAT = None


class CamFileValidator(object):
    def __init__(self, file_name):
        self.name: str = os.path.splitext(file_name)[0]
        self._format_functions: dict = {
            CamAcceptedFormats.ONE: self._get_date_to_format_one,
            CamAcceptedFormats.TWO: self._get_date_to_format_two,
            CamAcceptedFormats.THREE: self._get_date_to_format_three,
            CamAcceptedFormats.WITHOUT_FORMAT: lambda: "",
        }

    def _is_valid_size_name(self) -> bool:
        return len(self.name) in [
            len(CamAcceptedFormats.ONE.value),
            len(CamAcceptedFormats.TWO.value),
            len(CamAcceptedFormats.THREE.value),
        ]

    def _get_name_format(self) -> CamAcceptedFormats:
        if "-" not in self.name and "_" not in self.name and " " not in self.name:
            if len(self.name) == 11:
                return CamAcceptedFormats.ONE
            if len(self.name) == 14:
                return CamAcceptedFormats.TWO

        if self.name[4:5] == "-" and self.name[7:8] == "-" and self.name[10:11] == " ":
            return CamAcceptedFormats.THREE

        return CamAcceptedFormats.WITHOUT_FORMAT

    def _get_date_to_format_one(self) -> str:
        year = self.name[4:8]
        month = self.name[2:4]
        day = self.name[0:2]
        return Folder.get_folder_name(year, month, day)

    def _get_date_to_format_two(self) -> str:
        year = self.name[0:4]
        month = self.name[4:6]
        day = self.name[6:8]
        return Folder.get_folder_name(year, month, day)

    def _get_date_to_format_three(self) -> str:
        year = self.name[0:4]
        month = self.name[5:7]
        day = self.name[8:10]
        return Folder.get_folder_name(year, month, day)

    def validate(self) -> str:
        if self._is_valid_size_name():
            return self._format_functions[self._get_name_format()]()

        return ""
