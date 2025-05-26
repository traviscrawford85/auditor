# Adapter for eventbase
from clio_sdk.models.eventbase import EventbaseIn, EventbaseOut, EventbaseUpdate, EventbaseDb
from clio_client.models import my_event

def convert_sdk_to_eventbaseout(src: my_event) -> EventbaseOut:
    return EventbaseOut(**src.dict())

def convert_eventbasein_to_sdk(src: EventbaseIn) -> my_event:
    return my_event(**src.dict())
