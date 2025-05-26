# Adapter for calendarbase
from clio_sdk.models.calendarbase import CalendarbaseIn, CalendarbaseOut, CalendarbaseUpdate, CalendarbaseDb
from clio_client.models import calendar

def convert_sdk_to_calendarbaseout(src: calendar) -> CalendarbaseOut:
    return CalendarbaseOut(**src.dict())

def convert_calendarbasein_to_sdk(src: CalendarbaseIn) -> calendar:
    return calendar(**src.dict())
