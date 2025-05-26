# Adapter for attendeebase
from clio_sdk.models.attendeebase import AttendeeBaseIn, AttendeebaseOut, AttendeebaseUpdate, AttendeebaseDb
from clio_client.models.attendee_base import AttendeeBase

def convert_sdk_to_attendeebaseout(src: AttendeeBase) -> AttendeebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return AttendeebaseOut(**src.model_dump())

def convert_attendeebasein_to_sdk(src: AttendeeBaseIn) -> AttendeeBase:
    """Converts a clio_sdk model to clio_client model."""
    return AttendeeBase(**src.model_dump())
