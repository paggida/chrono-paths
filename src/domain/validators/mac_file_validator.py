import enum
import os

import unidecode

from src.domain.folder import Folder


class MacAcceptedFormats(enum.Enum):
    ONE = "Screen Shot 2022-08-19 at 11.06.18"
    TWO = "Captura de Tela 2022-08-30 às 11.29.15"
    WITHOUT_FORMAT = None


class MacFileValidator(object):
    def __init__(self, file_name):
        self.name: str = unidecode.unidecode(os.path.splitext(file_name)[0])
        self._format_functions: dict = {
            MacAcceptedFormats.ONE: self._get_date_to_format_one,
            MacAcceptedFormats.TWO: self._get_date_to_format_two,
            MacAcceptedFormats.WITHOUT_FORMAT: lambda: "",
        }

    def _is_valid_size_name(self) -> bool:
        return len(self.name) in [
            len(MacAcceptedFormats.ONE.value),
            len(MacAcceptedFormats.TWO.value),
        ]

    def _get_name_format(self) -> MacAcceptedFormats:
        if self.name[0:12] == "Screen Shot ":
            return MacAcceptedFormats.ONE

        if self.name[0:16] == "Captura de Tela ":
            return MacAcceptedFormats.TWO

        return MacAcceptedFormats.WITHOUT_FORMAT

    def _get_date_to_format_one(self) -> str:
        year = self.name[12:16]
        month = self.name[17:19]
        day = self.name[20:22]
        return Folder.get_folder_name(year, month, day)

    def _get_date_to_format_two(self) -> str:
        year = self.name[16:20]
        month = self.name[21:23]
        day = self.name[24:26]
        return Folder.get_folder_name(year, month, day)

    def validate(self) -> str:
        if self._is_valid_size_name():
            return self._format_functions[self._get_name_format()]()

        return ""
