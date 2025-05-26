# Adapter for calendarentrybase
from clio_sdk.models.calendarentrybase import CalendarentrybaseIn, CalendarentrybaseOut, CalendarentrybaseUpdate, CalendarentrybaseDb
from clio_client.models import calendar_entry

def convert_sdk_to_calendarentrybaseout(src: calendar_entry) -> CalendarentrybaseOut:
    return CalendarentrybaseOut(**src.dict())

def convert_calendarentrybasein_to_sdk(src: CalendarentrybaseIn) -> calendar_entry:
    return calendar_entry(**src.dict())
