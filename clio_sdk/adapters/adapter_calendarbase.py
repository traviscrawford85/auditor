# Adapter for calendarbase
from clio_sdk.models.calendarbase import CalendarBaseIn, CalendarbaseOut, CalendarbaseUpdate, CalendarbaseDb
from clio_client.models.calendar import Calendar

def convert_sdk_to_calendarbaseout(src: Calendar) -> CalendarbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return CalendarbaseOut(**src.model_dump())

def convert_calendarbasein_to_sdk(src: CalendarBaseIn) -> Calendar:
    """Converts a clio_sdk model to clio_client model."""
    return Calendar(**src.model_dump())
