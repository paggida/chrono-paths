from src.domain.validators.mac_file_validator import MacFileValidator


class TestMacFileValidator:
    def test_returns_folder_name_with_valid_file_name_in_format_one(self):
        assert (
            MacFileValidator("Screen Shot 2022-08-19 at 11.06.18.jpg").validate()
            == "[2022.08.19]"
        )

    def test_returns_folder_name_with_valid_file_name_in_format_two(self):
        assert (
            MacFileValidator("Captura de Tela 2022-08-30 às 11.29.15.jpg").validate()
            == "[2022.08.30]"
        )

    def test_returns_empty_string_for_invalid_file_names(self):
        mac_file_validator_format_one_with_letter = MacFileValidator(
            "Screen Shot 2022-AB-19 at 11.06.18.jpg"
        )
        mac_file_validator_format_one_with_invalid_format = MacFileValidator(
            "Screen Shot-20220819_110618.jpg"
        )

        mac_file_validator_format_two_with_letter = MacFileValidator(
            "Captura de Tela 2022-0W-30 às 11.29.15.jpg"
        )
        mac_file_validator_format_two_with_invalid_format = MacFileValidator(
            "Captura_de_Tela 20220830 às 112915.jpg"
        )
        mac_file_validator_unknown_format = MacFileValidator("V-20111108-195333.mp4")

        assert not mac_file_validator_format_one_with_letter.validate()
        assert not mac_file_validator_format_one_with_invalid_format.validate()
        assert not mac_file_validator_format_two_with_letter.validate()
        assert not mac_file_validator_format_two_with_invalid_format.validate()
        assert not mac_file_validator_unknown_format.validate()
