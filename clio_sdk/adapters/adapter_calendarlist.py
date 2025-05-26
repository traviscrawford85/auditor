# Adapter for calendarlist
from clio_sdk.models.calendarlist import CalendarlistIn, CalendarlistOut, CalendarlistUpdate, CalendarlistDb
from clio_client.models.calendar_list import CalendarList

def convert_sdk_to_calendarlistout(src: CalendarList) -> CalendarlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return CalendarlistOut(**src.model_dump())

def convert_calendarlistin_to_sdk(src: CalendarlistIn) -> CalendarList:
    """Converts a clio_sdk model to clio_client model."""
    return CalendarList(**src.model_dump())
