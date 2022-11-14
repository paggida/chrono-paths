from src.domain.validators.whatsapp_file_validator import WhatsappFileValidator


class TestWhatsappFileValidator:
    def test_returns_folder_name_with_valid_file_name_in_format_one(self):
        assert (
            WhatsappFileValidator("IMG-20130916-WA0015.jpg").validate()
            == "[2013.09.16]"
        )

    def test_returns_folder_name_with_valid_file_name_in_format_two(self):
        assert (
            WhatsappFileValidator(
                "WhatsApp Image 2018-09-16 at 12.21.27.jpeg"
            ).validate()
            == "[2018.09.16]"
        )

    def test_returns_folder_name_with_valid_file_name_in_format_three(self):
        assert (
            WhatsappFileValidator("VID-20150506-WA0047.mp4").validate()
            == "[2015.05.06]"
        )

    def test_returns_folder_name_with_valid_file_name_in_format_four(self):
        assert (
            WhatsappFileValidator("Video-2011-11-08-19-53-33.mp4").validate()
            == "[2011.11.08]"
        )

    def test_returns_empty_string_for_invalid_file_names(self):
        whatsapp_file_validator_format_one_with_letter = WhatsappFileValidator(
            "IMG-2013a916-WA0015.jpg"
        )
        whatsapp_file_validator_format_one_with_invalid_format = WhatsappFileValidator(
            "IMG-20130916-XX0015.jpg"
        )
        whatsapp_file_validator_format_two = WhatsappFileValidator(
            "Whats Image 2018-09-16.jpeg"
        )
        whatsapp_file_validator_format_three_with_letter = WhatsappFileValidator(
            "VID-2015o506-WA0047.mp4"
        )
        whatsapp_file_validator_format_three_with_invalid_format = (
            WhatsappFileValidator("VID-20150506-XX0047.mp4")
        )
        whatsapp_file_validator_format_four = WhatsappFileValidator(
            "Video-20111108-195333.mp4"
        )

        assert not whatsapp_file_validator_format_one_with_letter.validate()
        assert not whatsapp_file_validator_format_one_with_invalid_format.validate()
        assert not whatsapp_file_validator_format_two.validate()
        assert not whatsapp_file_validator_format_three_with_letter.validate()
        assert not whatsapp_file_validator_format_three_with_invalid_format.validate()
        assert not whatsapp_file_validator_format_four.validate()
