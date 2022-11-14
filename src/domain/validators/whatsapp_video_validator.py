import enum
import os

from src.domain.folder import Folder


class WhatsappVideoAcceptedFormats(enum.Enum):
    ONE = "VID-20150506-WA0047"
    TWO = "Video-2011-11-08-19-53-33"
    WITHOUT_FORMAT = None


class WhatsappVideoValidator(object):
    def __init__(self, file_name):
        self.name: str = os.path.splitext(file_name)[0]
        self._format_functions: dict = {
            WhatsappVideoAcceptedFormats.ONE: self._get_date_to_format_one,
            WhatsappVideoAcceptedFormats.TWO: self._get_date_to_format_two,
            WhatsappVideoAcceptedFormats.WITHOUT_FORMAT: lambda: "",
        }

    def _is_valid_size_name(self) -> bool:
        return len(self.name) in [
            len(WhatsappVideoAcceptedFormats.ONE.value),
            len(WhatsappVideoAcceptedFormats.TWO.value),
        ]

    def _get_name_format(self) -> WhatsappVideoAcceptedFormats:
        if self.name[0:4] == "VID-" and self.name[12:15] == "-WA":
            return WhatsappVideoAcceptedFormats.ONE

        if self.name[0:6] == "Video-":
            return WhatsappVideoAcceptedFormats.TWO

        return WhatsappVideoAcceptedFormats.WITHOUT_FORMAT

    def _get_date_to_format_one(self) -> str:
        year = self.name[4:8]
        month = self.name[8:10]
        day = self.name[10:12]
        return Folder.get_folder_name(year, month, day)

    def _get_date_to_format_two(self) -> str:
        year = self.name[6:10]
        month = self.name[11:13]
        day = self.name[14:16]
        return Folder.get_folder_name(year, month, day)

    def validate(self) -> str:
        if self._is_valid_size_name():
            return self._format_functions[self._get_name_format()]()

        return ""
