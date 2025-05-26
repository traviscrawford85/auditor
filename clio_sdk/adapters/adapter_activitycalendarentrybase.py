# Adapter for activitycalendarentrybase
from clio_sdk.models.activitycalendarentrybase import ActivitycalendarentrybaseIn, ActivitycalendarentrybaseOut, ActivitycalendarentrybaseUpdate, ActivitycalendarentrybaseDb
from clio_client.models import activity_calendar_entry

def convert_sdk_to_activitycalendarentrybaseout(src: activity_calendar_entry) -> ActivitycalendarentrybaseOut:
    return ActivitycalendarentrybaseOut(**src.dict())

def convert_activitycalendarentrybasein_to_sdk(src: ActivitycalendarentrybaseIn) -> activity_calendar_entry:
    return activity_calendar_entry(**src.dict())
