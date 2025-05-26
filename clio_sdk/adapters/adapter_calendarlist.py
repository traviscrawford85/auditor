# Adapter for calendarlist
from clio_sdk.models.calendarlist import CalendarlistIn, CalendarlistOut, CalendarlistUpdate, CalendarlistDb
from clio_client.models import calendar_list

def convert_sdk_to_calendarlistout(src: calendar_list) -> CalendarlistOut:
    return CalendarlistOut(**src.dict())

def convert_calendarlistin_to_sdk(src: CalendarlistIn) -> calendar_list:
    return calendar_list(**src.dict())
