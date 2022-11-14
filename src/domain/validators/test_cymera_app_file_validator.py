from src.domain.validators.cymera_app_file_validator import CymeraFileValidator


class TestCymeraFileValidator:
    def test_returns_folder_name_with_valid_file_name_in_format_standard(self):
        assert (
            CymeraFileValidator("CYMERA_20150111_222759.jpg").validate()
            == "[2015.01.11]"
        )

    def test_returns_empty_string_for_invalid_file_names(self):
        cymera_file_validator_format_standard_with_letter = CymeraFileValidator(
            "CYMERA_201A0111_222759.jpg"
        )
        cymera_file_validator_format_standard_with_invalid_format = CymeraFileValidator(
            "CIMERA_20150111_222759.jpg"
        )
        cymera_file_validator_unknown_format = CymeraFileValidator(
            "Video-20111108-195333.mp4"
        )

        assert not cymera_file_validator_format_standard_with_letter.validate()
        assert not cymera_file_validator_format_standard_with_invalid_format.validate()
        assert not cymera_file_validator_unknown_format.validate()
