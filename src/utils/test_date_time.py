import datetime

from src.utils.date_time import DateTime


class TestDateTime:
    def test_return_true_for_a_valid_date(self):
        current_time = datetime.datetime.now()

        assert DateTime.is_valid_date(
            f"{current_time.year}", f"{current_time.month}", f"{current_time.day}"
        )
        assert DateTime.is_valid_date("2020", "02", "29")

    def test_return_false_for_an_invalid_date(self):
        assert not DateTime.is_valid_date("", "", "")
        assert not DateTime.is_valid_date("2022", "13", "01")
        assert not DateTime.is_valid_date("2022", "02", "31")
        assert not DateTime.is_valid_date("A", "02", "31")
