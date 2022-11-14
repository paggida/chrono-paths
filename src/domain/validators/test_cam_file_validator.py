from src.domain.validators.cam_file_validator import CamFileValidator


class TestCamFileValidator:
    def test_returns_folder_name_with_valid_file_name_in_format_one(self):
        assert CamFileValidator("31102008710.jpg").validate() == "[2008.10.31]"

    def test_returns_folder_name_with_valid_file_name_in_format_two(self):
        assert CamFileValidator("20120927165756.jpg").validate() == "[2012.09.27]"

    def test_returns_folder_name_with_valid_file_name_in_format_three(self):
        assert CamFileValidator("2011-04-28 20.29.56.jpg").validate() == "[2011.04.28]"

    def test_returns_empty_string_for_invalid_file_names(self):
        cam_file_validator_format_one_with_letter = CamFileValidator("311O2008710.jpg")
        cam_file_validator_format_one_with_invalid_format = CamFileValidator(
            "312008710.jpg"
        )
        cam_file_validator_format_two_with_letter = CamFileValidator(
            "2012O927165756.jpg"
        )
        cam_file_validator_format_two_with_invalid_format = CamFileValidator(
            "20120927165756367.jpg"
        )
        cam_file_validator_format_three_with_letter = CamFileValidator(
            "2011-04-A8 20.29.56.jpg"
        )
        cam_file_validator_format_three_with_invalid_format = CamFileValidator(
            "2011.04.28.20.29.56.jpg"
        )
        cam_file_validator_unknown_format = CamFileValidator("V-20111108-195333.mp4")

        assert not cam_file_validator_format_one_with_letter.validate()
        assert not cam_file_validator_format_one_with_invalid_format.validate()
        assert not cam_file_validator_format_two_with_letter.validate()
        assert not cam_file_validator_format_two_with_invalid_format.validate()
        assert not cam_file_validator_format_three_with_letter.validate()
        assert not cam_file_validator_format_three_with_invalid_format.validate()
        assert not cam_file_validator_unknown_format.validate()
