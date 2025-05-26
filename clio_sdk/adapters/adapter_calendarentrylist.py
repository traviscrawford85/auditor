# Adapter for calendarentrylist
from clio_sdk.models.calendarentrylist import CalendarentrylistIn, CalendarentrylistOut, CalendarentrylistUpdate, CalendarentrylistDb
from clio_client.models import calendar_entry_list

def convert_sdk_to_calendarentrylistout(src: calendar_entry_list) -> CalendarentrylistOut:
    return CalendarentrylistOut(**src.dict())

def convert_calendarentrylistin_to_sdk(src: CalendarentrylistIn) -> calendar_entry_list:
    return calendar_entry_list(**src.dict())
