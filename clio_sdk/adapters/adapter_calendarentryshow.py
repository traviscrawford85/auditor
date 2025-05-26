# Adapter for calendarentryshow
from clio_sdk.models.calendarentryshow import CalendarentryshowIn, CalendarentryshowOut, CalendarentryshowUpdate, CalendarentryshowDb
from clio_client.models import calendar_entry_show

def convert_sdk_to_calendarentryshowout(src: calendar_entry_show) -> CalendarentryshowOut:
    return CalendarentryshowOut(**src.dict())

def convert_calendarentryshowin_to_sdk(src: CalendarentryshowIn) -> calendar_entry_show:
    return calendar_entry_show(**src.dict())
