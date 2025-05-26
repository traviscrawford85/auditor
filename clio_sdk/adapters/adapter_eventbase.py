# Adapter for eventbase
from clio_sdk.models.eventbase import EventBaseIn, EventbaseOut, EventbaseUpdate, EventbaseDb
from clio_client.models.my_event import MyEvent

def convert_sdk_to_eventbaseout(src: MyEvent) -> EventbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return EventbaseOut(**src.model_dump())

def convert_eventbasein_to_sdk(src: EventBaseIn) -> MyEvent:
    """Converts a clio_sdk model to clio_client model."""
    return MyEvent(**src.model_dump())
