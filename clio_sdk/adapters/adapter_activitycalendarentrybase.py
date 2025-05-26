# Adapter for activitycalendarentrybase
from clio_sdk.models.activitycalendarentrybase import ActivitycalendarentryBaseIn, ActivitycalendarentrybaseOut, ActivitycalendarentrybaseUpdate, ActivitycalendarentrybaseDb
from clio_client.models.activity_calendar_entry import ActivityCalendarEntry

def convert_sdk_to_activitycalendarentrybaseout(src: ActivityCalendarEntry) -> ActivitycalendarentrybaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return ActivitycalendarentrybaseOut(**src.model_dump())

def convert_activitycalendarentrybasein_to_sdk(src: ActivitycalendarentryBaseIn) -> ActivityCalendarEntry:
    """Converts a clio_sdk model to clio_client model."""
    return ActivityCalendarEntry(**src.model_dump())
