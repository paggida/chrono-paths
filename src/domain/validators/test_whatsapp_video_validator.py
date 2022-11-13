from src.domain.validators.whatsapp_video_validator import WhatsappVideoValidator


class TestWhatsappVideoValidator:
    def test_returns_folder_name_with_valid_file_name(self):
        whatsapp_video_validator_format_one = WhatsappVideoValidator(
            "VID-20150506-WA0047.mp4"
        )
        whatsapp_video_validator_format_two = WhatsappVideoValidator(
            "Video-2011-11-08-19-53-33.mp4"
        )

        assert whatsapp_video_validator_format_one.validate() == "[2015.05.06]"
        assert whatsapp_video_validator_format_two.validate() == "[2011.11.08]"

    def test_returns_empty_string_with_invalid_file_name(self):
        whatsapp_video_validator_format_one_with_letter = WhatsappVideoValidator(
            "VID-2015o506-WA0047.mp4"
        )
        whatsapp_video_validator_format_one_with_invalid_format = (
            WhatsappVideoValidator("VID-20150506-XX0047.mp4")
        )
        whatsapp_video_validator_format_two = WhatsappVideoValidator(
            "Video-20111108-195333.mp4"
        )

        assert not whatsapp_video_validator_format_one_with_letter.validate()
        assert not whatsapp_video_validator_format_one_with_invalid_format.validate()
        assert not whatsapp_video_validator_format_two.validate()
