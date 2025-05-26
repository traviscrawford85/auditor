# Adapter for eventmetricsbase
from clio_sdk.models.eventmetricsbase import EventmetricsBaseIn, EventmetricsbaseOut, EventmetricsbaseUpdate, EventmetricsbaseDb
from clio_client.models.event_metrics import EventMetrics

def convert_sdk_to_eventmetricsbaseout(src: EventMetrics) -> EventmetricsbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return EventmetricsbaseOut(**src.model_dump())

def convert_eventmetricsbasein_to_sdk(src: EventmetricsBaseIn) -> EventMetrics:
    """Converts a clio_sdk model to clio_client model."""
    return EventMetrics(**src.model_dump())
