# Adapter for calendarentrybase
from clio_sdk.models.calendarentrybase import CalendarentryBaseIn, CalendarentrybaseOut, CalendarentrybaseUpdate, CalendarentrybaseDb
from clio_client.models.calendar_entry import CalendarEntry

def convert_sdk_to_calendarentrybaseout(src: CalendarEntry) -> CalendarentrybaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return CalendarentrybaseOut(**src.model_dump())

def convert_calendarentrybasein_to_sdk(src: CalendarentryBaseIn) -> CalendarEntry:
    """Converts a clio_sdk model to clio_client model."""
    return CalendarEntry(**src.model_dump())
