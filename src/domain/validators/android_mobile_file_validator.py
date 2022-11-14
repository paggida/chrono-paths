import enum
import os

from src.domain.folder import Folder


class AndroidMobileAcceptedFormats(enum.Enum):
    ONE = "20120927_165756"
    TWO = "20120927_165756_8"
    THREE = "20120927_165756_20"
    FOUR = "20120927_165756_2_bestshot"
    FIVE = "20120927_165756_Richtone(HDR)"
    SIX = "Screenshot_20220819-110618_Instagram"
    WITHOUT_FORMAT = None


class AndroidMobileFileValidator(object):
    def __init__(self, file_name):
        self.name: str = os.path.splitext(file_name)[0]
        self._format_functions: dict = {
            AndroidMobileAcceptedFormats.ONE: self._get_date_to_format_one_to_five,
            AndroidMobileAcceptedFormats.TWO: self._get_date_to_format_one_to_five,
            AndroidMobileAcceptedFormats.THREE: self._get_date_to_format_one_to_five,
            AndroidMobileAcceptedFormats.FOUR: self._get_date_to_format_one_to_five,
            AndroidMobileAcceptedFormats.FIVE: self._get_date_to_format_one_to_five,
            AndroidMobileAcceptedFormats.SIX: self._get_date_to_format_six,
            AndroidMobileAcceptedFormats.WITHOUT_FORMAT: lambda: "",
        }

    def _is_valid_size_name(self) -> bool:
        return len(self.name) in [
            len(AndroidMobileAcceptedFormats.ONE.value),
            len(AndroidMobileAcceptedFormats.TWO.value),
            len(AndroidMobileAcceptedFormats.THREE.value),
            len(AndroidMobileAcceptedFormats.FOUR.value),
            len(AndroidMobileAcceptedFormats.FIVE.value),
            len(AndroidMobileAcceptedFormats.SIX.value),
        ]

    def _get_name_format(self) -> AndroidMobileAcceptedFormats:
        if self.name[8:9] == "_":
            if self.name[15:16] == "_":
                if self.name[-9:] == "_bestshot":
                    return AndroidMobileAcceptedFormats.FOUR
                if self.name[-14:] == "_Richtone(HDR)":
                    return AndroidMobileAcceptedFormats.FIVE
                if len(self.name.split("_")[2]) == 1:
                    return AndroidMobileAcceptedFormats.TWO
                if len(self.name.split("_")[2]) == 2:
                    return AndroidMobileAcceptedFormats.THREE
            return AndroidMobileAcceptedFormats.ONE

        if self.name[0:11] == "Screenshot_" and len(self.name.split("_")) == 3:
            return AndroidMobileAcceptedFormats.SIX

        return AndroidMobileAcceptedFormats.WITHOUT_FORMAT

    def _get_date_to_format_one_to_five(self) -> str:
        year = self.name[0:4]
        month = self.name[4:6]
        day = self.name[6:8]
        return Folder.get_folder_name(year, month, day)

    def _get_date_to_format_six(self) -> str:
        year = self.name[11:15]
        month = self.name[15:17]
        day = self.name[17:19]
        return Folder.get_folder_name(year, month, day)

    def validate(self) -> str:
        if self._is_valid_size_name():
            return self._format_functions[self._get_name_format()]()

        return ""
