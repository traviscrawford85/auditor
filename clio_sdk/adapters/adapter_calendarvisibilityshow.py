# Adapter for calendarvisibilityshow
from clio_sdk.models.calendarvisibilityshow import CalendarvisibilityshowIn, CalendarvisibilityshowOut, CalendarvisibilityshowUpdate, CalendarvisibilityshowDb
from clio_client.models.calendar_visibility_show import CalendarVisibilityShow

def convert_sdk_to_calendarvisibilityshowout(src: CalendarVisibilityShow) -> CalendarvisibilityshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return CalendarvisibilityshowOut(**src.model_dump())

def convert_calendarvisibilityshowin_to_sdk(src: CalendarvisibilityshowIn) -> CalendarVisibilityShow:
    """Converts a clio_sdk model to clio_client model."""
    return CalendarVisibilityShow(**src.model_dump())
