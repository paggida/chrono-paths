from src.domain.validators.whatsapp_image_validator import WhatsappImageValidator


class TestWhatsappImageValidator:
    def test_return_folder_name_with_valid_file_name(self):
        whatsapp_image_validator_format_one = WhatsappImageValidator(
            "IMG-20130916-WA0015.jpg"
        )
        whatsapp_image_validator_format_two = WhatsappImageValidator(
            "WhatsApp Image 2018-09-16 at 12.21.27.jpeg"
        )

        assert whatsapp_image_validator_format_one.validate() == "[2013.09.16]"
        assert whatsapp_image_validator_format_two.validate() == "[2018.09.16]"

    def test_return_empty_string_with_invalid_file_name(self):
        whatsapp_image_validator_format_one_with_letter = WhatsappImageValidator(
            "IMG-2013a916-WA0015.jpg"
        )
        whatsapp_image_validator_format_one_with_invalid_format = (
            WhatsappImageValidator("IMG-20130916-XX0015.jpg")
        )
        whatsapp_image_validator_format_two = WhatsappImageValidator(
            "Whats Image 2018-09-16.jpeg"
        )

        assert not whatsapp_image_validator_format_one_with_letter.validate()
        assert not whatsapp_image_validator_format_one_with_invalid_format.validate()
        assert not whatsapp_image_validator_format_two.validate()
