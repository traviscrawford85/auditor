# Adapter for calendarvisibilitybase
from clio_sdk.models.calendarvisibilitybase import CalendarvisibilityBaseIn, CalendarvisibilitybaseOut, CalendarvisibilitybaseUpdate, CalendarvisibilitybaseDb
from clio_client.models.calendar_visibility import CalendarVisibility

def convert_sdk_to_calendarvisibilitybaseout(src: CalendarVisibility) -> CalendarvisibilitybaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return CalendarvisibilitybaseOut(**src.model_dump())

def convert_calendarvisibilitybasein_to_sdk(src: CalendarvisibilityBaseIn) -> CalendarVisibility:
    """Converts a clio_sdk model to clio_client model."""
    return CalendarVisibility(**src.model_dump())
