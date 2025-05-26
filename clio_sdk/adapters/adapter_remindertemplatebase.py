# Adapter for remindertemplatebase
from clio_sdk.models.remindertemplatebase import RemindertemplatebaseIn, RemindertemplatebaseOut, RemindertemplatebaseUpdate, RemindertemplatebaseDb
from clio_client.models import reminder_template_base

def convert_sdk_to_remindertemplatebaseout(src: reminder_template_base) -> RemindertemplatebaseOut:
    return RemindertemplatebaseOut(**src.dict())

def convert_remindertemplatebasein_to_sdk(src: RemindertemplatebaseIn) -> reminder_template_base:
    return reminder_template_base(**src.dict())
