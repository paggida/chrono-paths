import datetime


class DateTime(object):
    @staticmethod
    def is_valid_date(year: str, month: str, day: str):
        try:
            date = datetime.datetime(year=int(year), month=int(month), day=int(day))
        except Exception as e:
            return False
        else:
            return True
