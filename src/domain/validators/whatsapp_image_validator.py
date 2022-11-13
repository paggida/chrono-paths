import enum

from src.domain.folder import Folder


class WhatsappImageAcceptedFormats(enum.Enum):
    ONE = "IMG-20130916-WA0015.jpg"
    TWO = "WhatsApp Image 2018-09-16 at 12.21.27.jpeg"
    WITHOUT_FORMAT = None


class WhatsappImageValidator(object):
    def __init__(self, file_name):
        self.name: str = file_name
        self._format_functions: dict = {
            WhatsappImageAcceptedFormats.ONE: self._get_date_to_format_one,
            WhatsappImageAcceptedFormats.TWO: self._get_date_to_format_two,
            WhatsappImageAcceptedFormats.WITHOUT_FORMAT: lambda: "",
        }

    def _is_valid_size_name(self) -> bool:
        return len(self.name) in [
            len(WhatsappImageAcceptedFormats.ONE.value),
            len(WhatsappImageAcceptedFormats.TWO.value),
        ]

    def _get_name_format(self) -> WhatsappImageAcceptedFormats:
        if self.name[0:4] == "IMG-" and self.name[12:15] == "-WA":
            return WhatsappImageAcceptedFormats.ONE

        if self.name[0:15] == "WhatsApp Image ":
            return WhatsappImageAcceptedFormats.TWO

        return WhatsappImageAcceptedFormats.WITHOUT_FORMAT

    def _get_date_to_format_one(self) -> str:
        year = self.name[4:8]
        month = self.name[8:10]
        day = self.name[10:12]
        return Folder.get_folder_name(year, month, day)

    def _get_date_to_format_two(self) -> str:
        year = self.name[15:19]
        month = self.name[20:22]
        day = self.name[23:25]
        return Folder.get_folder_name(year, month, day)

    def validate(self) -> str:
        if self._is_valid_size_name():
            return self._format_functions[self._get_name_format()]()

        return ""
