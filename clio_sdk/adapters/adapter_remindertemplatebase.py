# Adapter for remindertemplatebase
from clio_sdk.models.remindertemplatebase import RemindertemplateBaseIn, RemindertemplatebaseOut, RemindertemplatebaseUpdate, RemindertemplatebaseDb
from clio_client.models.reminder_template_base import ReminderTemplateBase

def convert_sdk_to_remindertemplatebaseout(src: ReminderTemplateBase) -> RemindertemplatebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return RemindertemplatebaseOut(**src.model_dump())

def convert_remindertemplatebasein_to_sdk(src: RemindertemplateBaseIn) -> ReminderTemplateBase:
    """Converts a clio_sdk model to clio_client model."""
    return ReminderTemplateBase(**src.model_dump())
