import enum
import os

from src.domain.folder import Folder


class WhatsappFileAcceptedFormats(enum.Enum):
    ONE = "IMG-20130916-WA0015"
    TWO = "WhatsApp Image 2018-09-16 at 12.21.27"
    THREE = "VID-20150506-WA0047"
    FOUR = "Video-2011-11-08-19-53-33"
    WITHOUT_FORMAT = None


class WhatsappFileValidator(object):
    def __init__(self, file_name):
        self.name: str = os.path.splitext(file_name)[0]
        self._format_functions: dict = {
            WhatsappFileAcceptedFormats.ONE: self._get_date_to_format_one_and_three,
            WhatsappFileAcceptedFormats.TWO: self._get_date_to_format_two,
            WhatsappFileAcceptedFormats.THREE: self._get_date_to_format_one_and_three,
            WhatsappFileAcceptedFormats.FOUR: self._get_date_to_format_four,
            WhatsappFileAcceptedFormats.WITHOUT_FORMAT: lambda: "",
        }

    def _is_valid_size_name(self) -> bool:
        return len(self.name) in [
            len(WhatsappFileAcceptedFormats.ONE.value),
            len(WhatsappFileAcceptedFormats.TWO.value),
            len(WhatsappFileAcceptedFormats.THREE.value),
            len(WhatsappFileAcceptedFormats.FOUR.value),
        ]

    def _get_name_format(self) -> WhatsappFileAcceptedFormats:
        if self.name[0:4] == "IMG-" and self.name[12:15] == "-WA":
            return WhatsappFileAcceptedFormats.ONE

        if self.name[0:15] == "WhatsApp Image ":
            return WhatsappFileAcceptedFormats.TWO

        if self.name[0:4] == "VID-" and self.name[12:15] == "-WA":
            return WhatsappFileAcceptedFormats.THREE

        if self.name[0:6] == "Video-":
            return WhatsappFileAcceptedFormats.FOUR

        return WhatsappFileAcceptedFormats.WITHOUT_FORMAT

    def _get_date_to_format_one_and_three(self) -> str:
        year = self.name[4:8]
        month = self.name[8:10]
        day = self.name[10:12]
        return Folder.get_folder_name(year, month, day)

    def _get_date_to_format_two(self) -> str:
        year = self.name[15:19]
        month = self.name[20:22]
        day = self.name[23:25]
        return Folder.get_folder_name(year, month, day)

    def _get_date_to_format_four(self) -> str:
        year = self.name[6:10]
        month = self.name[11:13]
        day = self.name[14:16]
        return Folder.get_folder_name(year, month, day)

    def validate(self) -> str:
        if self._is_valid_size_name():
            return self._format_functions[self._get_name_format()]()

        return ""
