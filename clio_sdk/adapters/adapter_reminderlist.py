# Adapter for reminderlist
from clio_sdk.models.reminderlist import ReminderlistIn, ReminderlistOut, ReminderlistUpdate, ReminderlistDb
from clio_client.models import reminder_list

def convert_sdk_to_reminderlistout(src: reminder_list) -> ReminderlistOut:
    return ReminderlistOut(**src.dict())

def convert_reminderlistin_to_sdk(src: ReminderlistIn) -> reminder_list:
    return reminder_list(**src.dict())
