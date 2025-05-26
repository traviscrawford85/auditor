# Adapter for reminderbase
from clio_sdk.models.reminderbase import ReminderbaseIn, ReminderbaseOut, ReminderbaseUpdate, ReminderbaseDb
from clio_client.models import reminder

def convert_sdk_to_reminderbaseout(src: reminder) -> ReminderbaseOut:
    return ReminderbaseOut(**src.dict())

def convert_reminderbasein_to_sdk(src: ReminderbaseIn) -> reminder:
    return reminder(**src.dict())
