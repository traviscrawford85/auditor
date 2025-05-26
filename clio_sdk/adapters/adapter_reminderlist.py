# Adapter for reminderlist
from clio_sdk.models.reminderlist import ReminderlistIn, ReminderlistOut, ReminderlistUpdate, ReminderlistDb
from clio_client.models.reminder_list import ReminderList

def convert_sdk_to_reminderlistout(src: ReminderList) -> ReminderlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return ReminderlistOut(**src.model_dump())

def convert_reminderlistin_to_sdk(src: ReminderlistIn) -> ReminderList:
    """Converts a clio_sdk model to clio_client model."""
    return ReminderList(**src.model_dump())
