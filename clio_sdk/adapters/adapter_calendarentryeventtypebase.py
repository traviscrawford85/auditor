# Adapter for calendarentryeventtypebase
from clio_sdk.models.calendarentryeventtypebase import CalendarentryeventtypeBaseIn, CalendarentryeventtypebaseOut, CalendarentryeventtypebaseUpdate, CalendarentryeventtypebaseDb
from clio_client.models.calendar_entry_event_type import CalendarEntryEventType

def convert_sdk_to_calendarentryeventtypebaseout(src: CalendarEntryEventType) -> CalendarentryeventtypebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return CalendarentryeventtypebaseOut(**src.model_dump())

def convert_calendarentryeventtypebasein_to_sdk(src: CalendarentryeventtypeBaseIn) -> CalendarEntryEventType:
    """Converts a clio_sdk model to clio_client model."""
    return CalendarEntryEventType(**src.model_dump())
