# Adapter for calendarvisibilitybase
from clio_sdk.models.calendarvisibilitybase import CalendarvisibilitybaseIn, CalendarvisibilitybaseOut, CalendarvisibilitybaseUpdate, CalendarvisibilitybaseDb
from clio_client.models import calendar_visibility

def convert_sdk_to_calendarvisibilitybaseout(src: calendar_visibility) -> CalendarvisibilitybaseOut:
    return CalendarvisibilitybaseOut(**src.dict())

def convert_calendarvisibilitybasein_to_sdk(src: CalendarvisibilitybaseIn) -> calendar_visibility:
    return calendar_visibility(**src.dict())
