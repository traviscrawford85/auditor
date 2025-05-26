# Adapter for calendarshow
from clio_sdk.models.calendarshow import CalendarshowIn, CalendarshowOut, CalendarshowUpdate, CalendarshowDb
from clio_client.models import calendar_show

def convert_sdk_to_calendarshowout(src: calendar_show) -> CalendarshowOut:
    return CalendarshowOut(**src.dict())

def convert_calendarshowin_to_sdk(src: CalendarshowIn) -> calendar_show:
    return calendar_show(**src.dict())
