# Adapter for eventmetricsshow
from clio_sdk.models.eventmetricsshow import EventmetricsshowIn, EventmetricsshowOut, EventmetricsshowUpdate, EventmetricsshowDb
from clio_client.models import event_metrics_show

def convert_sdk_to_eventmetricsshowout(src: event_metrics_show) -> EventmetricsshowOut:
    return EventmetricsshowOut(**src.dict())

def convert_eventmetricsshowin_to_sdk(src: EventmetricsshowIn) -> event_metrics_show:
    return event_metrics_show(**src.dict())
