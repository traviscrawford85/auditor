# Adapter for calendarentrylist
from clio_sdk.models.calendarentrylist import CalendarentrylistIn, CalendarentrylistOut, CalendarentrylistUpdate, CalendarentrylistDb
from clio_client.models.calendar_entry_list import CalendarEntryList

def convert_sdk_to_calendarentrylistout(src: CalendarEntryList) -> CalendarentrylistOut:
    """Converts a clio_client model to clio_sdk model."""
    return CalendarentrylistOut(**src.model_dump())

def convert_calendarentrylistin_to_sdk(src: CalendarentrylistIn) -> CalendarEntryList:
    """Converts a clio_sdk model to clio_client model."""
    return CalendarEntryList(**src.model_dump())
