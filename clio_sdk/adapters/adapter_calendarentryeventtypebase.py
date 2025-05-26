# Adapter for calendarentryeventtypebase
from clio_sdk.models.calendarentryeventtypebase import CalendarentryeventtypebaseIn, CalendarentryeventtypebaseOut, CalendarentryeventtypebaseUpdate, CalendarentryeventtypebaseDb
from clio_client.models import calendar_entry_event_type

def convert_sdk_to_calendarentryeventtypebaseout(src: calendar_entry_event_type) -> CalendarentryeventtypebaseOut:
    return CalendarentryeventtypebaseOut(**src.dict())

def convert_calendarentryeventtypebasein_to_sdk(src: CalendarentryeventtypebaseIn) -> calendar_entry_event_type:
    return calendar_entry_event_type(**src.dict())
