# Adapter for reminderbase
from clio_sdk.models.reminderbase import ReminderBaseIn, ReminderbaseOut, ReminderbaseUpdate, ReminderbaseDb
from clio_client.models.reminder import Reminder

def convert_sdk_to_reminderbaseout(src: Reminder) -> ReminderbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return ReminderbaseOut(**src.model_dump())

def convert_reminderbasein_to_sdk(src: ReminderBaseIn) -> Reminder:
    """Converts a clio_sdk model to clio_client model."""
    return Reminder(**src.model_dump())
