# Adapter for attendeebase
from clio_sdk.models.attendeebase import AttendeebaseIn, AttendeebaseOut, AttendeebaseUpdate, AttendeebaseDb
from clio_client.models import attendee_base

def convert_sdk_to_attendeebaseout(src: attendee_base) -> AttendeebaseOut:
    return AttendeebaseOut(**src.dict())

def convert_attendeebasein_to_sdk(src: AttendeebaseIn) -> attendee_base:
    return attendee_base(**src.dict())
