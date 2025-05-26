# Adapter for remindershow
from clio_sdk.models.remindershow import RemindershowIn, RemindershowOut, RemindershowUpdate, RemindershowDb
from clio_client.models import reminder_show

def convert_sdk_to_remindershowout(src: reminder_show) -> RemindershowOut:
    return RemindershowOut(**src.dict())

def convert_remindershowin_to_sdk(src: RemindershowIn) -> reminder_show:
    return reminder_show(**src.dict())
