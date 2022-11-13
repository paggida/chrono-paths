from src.utils.date_time import DateTime


class Folder(object):

    @staticmethod
    def get_folder_name(year: str, month: str, day: str) -> str:
        return (
            f"[{year}.{month}.{day}]"\
            if DateTime.is_valid_date(year, month, day)
            else ""
        )
