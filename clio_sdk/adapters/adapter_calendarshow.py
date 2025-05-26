# Adapter for calendarshow
from clio_sdk.models.calendarshow import CalendarshowIn, CalendarshowOut, CalendarshowUpdate, CalendarshowDb
from clio_client.models.calendar_show import CalendarShow

def convert_sdk_to_calendarshowout(src: CalendarShow) -> CalendarshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return CalendarshowOut(**src.model_dump())

def convert_calendarshowin_to_sdk(src: CalendarshowIn) -> CalendarShow:
    """Converts a clio_sdk model to clio_client model."""
    return CalendarShow(**src.model_dump())
