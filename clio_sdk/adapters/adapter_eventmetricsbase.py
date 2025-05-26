# Adapter for eventmetricsbase
from clio_sdk.models.eventmetricsbase import EventmetricsbaseIn, EventmetricsbaseOut, EventmetricsbaseUpdate, EventmetricsbaseDb
from clio_client.models import event_metrics

def convert_sdk_to_eventmetricsbaseout(src: event_metrics) -> EventmetricsbaseOut:
    return EventmetricsbaseOut(**src.dict())

def convert_eventmetricsbasein_to_sdk(src: EventmetricsbaseIn) -> event_metrics:
    return event_metrics(**src.dict())
