from src.domain.validators.whatsapp_image_validator import WhatsappImageValidator
from src.domain.validators.whatsapp_video_validator import WhatsappVideoValidator


def get_validators_list():
    return [WhatsappImageValidator, WhatsappVideoValidator]
