# Adapter for remindershow
from clio_sdk.models.remindershow import RemindershowIn, RemindershowOut, RemindershowUpdate, RemindershowDb
from clio_client.models.reminder_show import ReminderShow

def convert_sdk_to_remindershowout(src: ReminderShow) -> RemindershowOut:
    """Converts a clio_client model to clio_sdk model."""
    return RemindershowOut(**src.model_dump())

def convert_remindershowin_to_sdk(src: RemindershowIn) -> ReminderShow:
    """Converts a clio_sdk model to clio_client model."""
    return ReminderShow(**src.model_dump())
