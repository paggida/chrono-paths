from src.domain.validators.android_mobile_file_validator import (
    AndroidMobileFileValidator,
)


class TestWhatsappFileValidator:
    def test_returns_folder_name_with_valid_file_name_in_format_one(self):
        assert (
            AndroidMobileFileValidator("20120927_165756.jpg").validate()
            == "[2012.09.27]"
        )

    def test_returns_folder_name_with_valid_file_name_in_format_two(self):
        assert (
            AndroidMobileFileValidator("20121003_165756_8.jpg").validate()
            == "[2012.10.03]"
        )

    def test_returns_folder_name_with_valid_file_name_in_format_three(self):
        assert (
            AndroidMobileFileValidator("20110417_165756_20.jpg").validate()
            == "[2011.04.17]"
        )

    def test_returns_folder_name_with_valid_file_name_in_format_four(self):
        assert (
            AndroidMobileFileValidator("20120322_165756_2_bestshot.jpg").validate()
            == "[2012.03.22]"
        )

    def test_returns_folder_name_with_valid_file_name_in_format_five(self):
        assert (
            AndroidMobileFileValidator("20000127_165756_Richtone(HDR).jpg").validate()
            == "[2000.01.27]"
        )

    def test_returns_folder_name_with_valid_file_name_in_format_six(self):
        assert (
            AndroidMobileFileValidator(
                "Screenshot_20220819-110618_Instagram.jpg"
            ).validate()
            == "[2022.08.19]"
        )

    def test_returns_empty_string_for_invalid_file_names(self):
        android_mobile_file_validator_format_one_with_letter = (
            AndroidMobileFileValidator("2012o927_165756.jpg")
        )
        android_mobile_file_validator_format_two = AndroidMobileFileValidator(
            "2x121003_165756_8.jpg"
        )
        android_mobile_file_validator_format_four_with_invalid_format = (
            AndroidMobileFileValidator("2012o322_165756_2_bestisot.jpg")
        )
        android_mobile_file_validator_format_five = AndroidMobileFileValidator(
            "20001327_165756_Richtone(HDD).jpg"
        )
        android_mobile_file_validator_format_six = AndroidMobileFileValidator(
            "Screenshot_20220819-110618Instagram.jpg"
        )

        assert not android_mobile_file_validator_format_one_with_letter.validate()
        assert not android_mobile_file_validator_format_two.validate()
        assert (
            not android_mobile_file_validator_format_four_with_invalid_format.validate()
        )
        assert not android_mobile_file_validator_format_five.validate()
        assert not android_mobile_file_validator_format_six.validate()
