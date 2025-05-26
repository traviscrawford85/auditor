# Adapter for calendarvisibilitylist
from clio_sdk.models.calendarvisibilitylist import CalendarvisibilitylistIn, CalendarvisibilitylistOut, CalendarvisibilitylistUpdate, CalendarvisibilitylistDb
from clio_client.models.calendar_visibility_list import CalendarVisibilityList

def convert_sdk_to_calendarvisibilitylistout(src: CalendarVisibilityList) -> CalendarvisibilitylistOut:
    """Converts a clio_client model to clio_sdk model."""
    return CalendarvisibilitylistOut(**src.model_dump())

def convert_calendarvisibilitylistin_to_sdk(src: CalendarvisibilitylistIn) -> CalendarVisibilityList:
    """Converts a clio_sdk model to clio_client model."""
    return CalendarVisibilityList(**src.model_dump())
