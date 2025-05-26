# Adapter for calendarvisibilitylist
from clio_sdk.models.calendarvisibilitylist import CalendarvisibilitylistIn, CalendarvisibilitylistOut, CalendarvisibilitylistUpdate, CalendarvisibilitylistDb
from clio_client.models import calendar_visibility_list

def convert_sdk_to_calendarvisibilitylistout(src: calendar_visibility_list) -> CalendarvisibilitylistOut:
    return CalendarvisibilitylistOut(**src.dict())

def convert_calendarvisibilitylistin_to_sdk(src: CalendarvisibilitylistIn) -> calendar_visibility_list:
    return calendar_visibility_list(**src.dict())
