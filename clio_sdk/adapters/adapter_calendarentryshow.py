# Adapter for calendarentryshow
from clio_sdk.models.calendarentryshow import CalendarentryshowIn, CalendarentryshowOut, CalendarentryshowUpdate, CalendarentryshowDb
from clio_client.models.calendar_entry_show import CalendarEntryShow

def convert_sdk_to_calendarentryshowout(src: CalendarEntryShow) -> CalendarentryshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return CalendarentryshowOut(**src.model_dump())

def convert_calendarentryshowin_to_sdk(src: CalendarentryshowIn) -> CalendarEntryShow:
    """Converts a clio_sdk model to clio_client model."""
    return CalendarEntryShow(**src.model_dump())
