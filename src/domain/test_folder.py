import datetime

from src.domain.folder import Folder


class TestFolder:
    def test_returns_folder_name(self):
        current_time = datetime.datetime.now()
        folder_name = Folder.get_folder_name(
            f"{current_time.year}", f"{current_time.month}", f"{current_time.day}"
        )

        assert (
                folder_name
                == f"[{current_time.year}.{current_time.month}.{current_time.day}]"
        )

    def test_returns_empty_name_for_invalid_dates_parameters(self):
        assert not Folder.get_folder_name("", "", "")
        assert not Folder.get_folder_name("2022", "13", "01")
        assert not Folder.get_folder_name("2022", "02", "31")
        assert not Folder.get_folder_name("A", "02", "31")
