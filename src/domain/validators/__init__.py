from src.domain.validators.android_mobile_file_validator import (
    AndroidMobileFileValidator,
)
from src.domain.validators.cymera_app_file_validator import CymeraFileValidator
from src.domain.validators.whatsapp_file_validator import WhatsappFileValidator


def get_validators_list():
    return [WhatsappFileValidator, AndroidMobileFileValidator, CymeraFileValidator]
