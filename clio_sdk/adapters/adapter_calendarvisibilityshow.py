# Adapter for calendarvisibilityshow
from clio_sdk.models.calendarvisibilityshow import CalendarvisibilityshowIn, CalendarvisibilityshowOut, CalendarvisibilityshowUpdate, CalendarvisibilityshowDb
from clio_client.models import calendar_visibility_show

def convert_sdk_to_calendarvisibilityshowout(src: calendar_visibility_show) -> CalendarvisibilityshowOut:
    return CalendarvisibilityshowOut(**src.dict())

def convert_calendarvisibilityshowin_to_sdk(src: CalendarvisibilityshowIn) -> calendar_visibility_show:
    return calendar_visibility_show(**src.dict())
